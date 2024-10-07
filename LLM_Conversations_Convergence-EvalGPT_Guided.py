import os
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union
import sys

from dotenv import load_dotenv
import pandas as pd
import random

import autogen
from autogen import Agent, AssistantAgent, ConversableAgent, UserProxyAgent
from autogen.code_utils import DEFAULT_MODEL, UNKNOWN, content_str, execute_code, extract_code, infer_lang


load_dotenv()

input_csv = './EvalGPTFix_Extracted/ExtractedEvalGPTFix.csv'

# random_seed = random.randint(0, 10000)
random_seed = 44

config_list_gemini_1_5_flash = autogen.config_list_from_json(
    "OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gemini-1.5-flash"],
    },
)

config_list_gemini_1_5_pro = autogen.config_list_from_json(
    "OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gemini-1.5-pro"],
    },
)

config_list_gpt_4o_mini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gpt-4o-mini"],
    },
)

config_list_gpt_4o = autogen.config_list_from_json(
    "OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gpt-4o"],
    },
)

gpt_4o_mini_config = {
    "cache_seed": random_seed, "temperature":0.5, "config_list": config_list_gpt_4o_mini, "timeout": 120,
}

gpt_4o_config = {
    "cache_seed": random_seed,"temperature":0.5, "config_list": config_list_gpt_4o, "timeout": 120,
}

gemini_flash_config ={
    "config_list": config_list_gemini_1_5_flash, "seed": random_seed
}

gemini_pro_config ={
    "config_list": config_list_gemini_1_5_pro, "seed": random_seed
}


initializer = autogen.UserProxyAgent(
    name="Init",
    code_execution_config={
        "use_docker": False,
    },
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
)



APR_debugger_1 = autogen.AssistantAgent(
    name="APR_debugger_1",
    llm_config=gpt_4o_config,
    system_message="""You are an automatic program repair agent. Your task is to fix the bugs identified by the fault localisation debuggers. Follow these steps:

Bug fixing: Review the bugs identified by the fault localization agents. Propose fixes for these bugs. Provide explanations for your chosen fixes.
Analysis: Ensure that the proposed fixes address the bugs while maintaining the intended functionality of the code. Reference the code's functionality to justify your fixes.
Turn-based Discussion: You must engage in a turn-based discussion with an external debugging agent in the group chat. Wait for the other agent's input before responding. Discuss the proposed bug fixes, and both agents must contribute to the final decision. Before agreeing and accepting the other agent's repair and feedback, scrutinize and question it's reasoning and provide constructive feedback. Try to achieve a convergence score of 1.0.
Do not finalize the decision until both agents have exchanged input multiple times.
Ask the next agent to propose what they think is the correct fix and wait for the other agent to propose its repair response and thereafter compare your proposed fixes with theirs and ask for feedback. Wait for their response before moving forward.
Code Annotation: After discussion is complete and a mutual agreement is reached, wrap the full code in a code block (specify the script type) and add a comment at the bug location.
""",
)

APR_debugger_2 = autogen.AssistantAgent(
    name="APR_debugger_2",
    llm_config=gemini_pro_config,
    system_message="""You are an automatic program repair agent. Your task is to independently fix the bugs identified by the fault localising agents, then collaborate with another repair agent to finalize the bug repairs. Follow these steps:

Independent Bug fixing: Initially when you are first called, ignore the previous response from APR_debugger_1. Review the bugs identified by the fault localization agents. Please ensure that you propose your own unique full code fixes for the bugs identified before engaging in a turn-based discussion with the second APR debugger. Provide explanations for your chosen fixes.
Analysis: Ensure that the proposed fixes address the bugs while maintaining the intended functionality of the code. Reference the code's functionality to justify your fixes.
Turn-based Discussion: You must engage in a turn-based discussion with an external debugging agent in the group chat. Wait for the other agent's input before responding. Discuss each of your proposed bug fixes, and both agents must contribute to the final decision. 
Ensure both agents exchange feedback multiple times before finalizing the decision.
Code Annotation: After discussion is complete and a mutual agreement is reached, wrap the full code in a code block (specify the script type) and add a comment at the bug location.
Ask for feedback from the other agent and wait for their response before moving forward.
Reply DONE_REPAIRING once both agents have exchanged input multiple times and reached consensus.
""",
)

reporting_agent = autogen.AssistantAgent(
    name="reporting_agent",
    llm_config=gpt_4o_config,
    system_message="""
You are the reporting agent. Provide a comprehensive summary of the debugging process and the final results.

Summarize the Buggy Lines: Clearly state the lines of code identified as containing bugs, listed in descending order of average probability, along with the reasons for each bug.

Format:
Line(s) of code with bug: <code line(s)>
Reason: <reason for the bug>
Wrap the Agreed Fix: Include the full code sample with the agreed-upon fix in a code block , specifying the script type.

Explain the Fix: Provide a brief explanation of the fix and why it is necessary for the code's functionality.

Conclude your report with the word TERMINATE.
    """
)


convergence_judge_2 = autogen.AssistantAgent(
    name="convergence_judge_2",
    llm_config=gpt_4o_config,
    system_message=""" You are tasked with evaluating the similarity between two sets of bug repair results provided by two independent Automated Program Repair (APR) agents. Each agent has proposed fixes for the identified bugs in a given code snippet.

Your goal is to iteratively assess the convergence between these two sets of repairs. Start by comparing the proposed fixes based on factors such as the correctness of the fix, location of changes, type of repairs made, and any specific descriptions provided. Based on this comparison, ensure that you provide an initial Convergence Score between 0 and 1 (mandatory), where:

0 indicates no overlap or similarity between the two agents' proposed repairs.
1 indicates a complete match between the two agents' proposed repairs.
After each iteration:

Adjust the score by evaluating the areas of divergence or partial agreement between the agents' proposed repairs.
Provide feedback to guide the refinement of the repair proposals (if necessary) to bring their results closer to alignment. Do not provide any code blocks.
Repeat the process until you determine that the responses fully converge and the score reaches 1.
For each iteration, provide:

The current Convergence Score as a number between 0 and 1.
A brief explanation of how you arrived at the score.
Any feedback or adjustments for the agents to achieve better convergence but do not correct the agents' responses directly.
Continue iterating until the responses reach full similarity (Convergence Score = 1). If the convergence is 1.0, specify the score and say GOOD_REPAIR, otherwise say BAD_REPAIR.
    """,
)

tracking_agent_2 = autogen.AssistantAgent(
    name="tracking_agent_2",
    llm_config=gpt_4o_mini_config,
    system_message=""" You are responsible for keeping track of the judges responses. If the judge says 'GOOD_REPAIR', reply with 'BUG_FIXED' to end the Automatic Program Repair process. 
    Otherwise reply with 'REDO_REPAIR' to restart the automatic program repair process. """
)

def state_transition(last_speaker, groupchat):
    messages = groupchat.messages
    
    if any("TERMINATE" in message["content"] for message in messages):
        return None  

    if last_speaker is initializer:
        return APR_debugger_1 
    elif last_speaker is APR_debugger_1:
        return APR_debugger_2
    elif last_speaker is APR_debugger_2:
            return convergence_judge_2
    elif last_speaker is convergence_judge_2:
        if "GOOD_REPAIR" in messages[-1]["content"]:
            return tracking_agent_2
        return APR_debugger_1
    elif last_speaker is tracking_agent_2:
        if "REDO_REPAIR" in messages[-1]["content"]:
            return APR_debugger_1
        if "BUG_FIXED" in messages[-1]["content"]:
            return reporting_agent 
    elif last_speaker is reporting_agent:
        return None  # Terminate the process after reporting_agent completes its task
    return None
    
# files_to_process = [
#     "file_0", "file_1", "file_2", "file_3", "file_4", "file_5", "file_6", "file_7", "file_8", "file_9", "file_10",
#     "file_11", "file_12", "file_13", "file_14", "file_15", "file_16", "file_17", "file_18", "file_21",
#     "file_23", "file_25", "file_26", "file_27", "file_28", "file_30", "file_31", "file_35", "file_36",
#     "file_38", "file_39", "file_40"
# ]

files_to_process = [f"file_{i}" for i in range(101, 151)]

data_zs = []
data_os = []

df_input = pd.read_csv(input_csv, encoding="utf-8")

df_filtered = df_input[df_input.iloc[:, 0].isin(files_to_process)]

for row, col in df_filtered.iterrows():
    file_name = col[0]
    code_content = col[2]
    error_code = col[4]
    explanation = col[5]

    print(f"Processing {file_name}")

    base_prompt = f"""Topic: Debug the following Java code snippet, consider the error in the code, and the specified location of the bug."""

    # one-shot prompting
    if error_code == 'CE':
        prompt = base_prompt + '\n\n' + '\n\nCode Context: There is a ' + explanation + ' in the code' + '\n\nCode:' + code_content
    elif error_code == 'TLE':
        prompt = base_prompt + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:' + code_content
    elif error_code == 'MLE':
        prompt = base_prompt + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:' + code_content
    elif error_code == 'RE':
        prompt = base_prompt + '\n\n' + '\n\nCode Context: The input triggers a ' + explanation + ' error' + '\n\nCode:' + code_content
    elif error_code == 'WA':
        prompt = base_prompt + '\n\n' + '\n\nCode Context: The output provides the ' + explanation + '\n\nCode:' + code_content

    groupchat = autogen.GroupChat(
        agents=[initializer, reporting_agent,convergence_judge_2, tracking_agent_2, APR_debugger_1, APR_debugger_2],
        messages=[],
        max_round=20,
        speaker_selection_method=state_transition,
    )
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt_4o_config)


    chatResult = initializer.initiate_chat(
        manager, message=prompt, summary_method="reflection_with_llm" )

    chat_history_list = chatResult.chat_history

    chat_history_string = '\n\n-------------------------------------------------------\n\n'.join(
        f"{item['role']} ({item['name']}): {item['content']}" 
        for item in chat_history_list 
        if 'role' in item and 'name' in item and 'content' in item
    )

    total_cost = chatResult.cost['usage_including_cached_inference']['total_cost']

    chat_history_string += f"\nTotal Cost: ${total_cost:.6f}"


    # save the conversation to a file
    with open(f"Conversation_Outputs/EvalGPTFix/Guided_APR/conversation_{file_name}.txt", 'w', encoding="utf-8") as file:
        file.write(chat_history_string)

    # extract final fixed code from the conversation
    with open(f"Conversation_Outputs/EvalGPTFix/Guided_APR/conversation_{file_name}.txt", 'r', encoding="utf-8") as file:
        chat_history_string = file.read()

    lines = chat_history_string.split('\n')

    inside_code_block = False
    code_lines = []

    for line in reversed(lines):
        if '```' in line.strip():
            if inside_code_block:
                break
            inside_code_block = True
            continue
        elif '```java' in line.strip():
            inside_code_block = False
            continue
        if inside_code_block:
            code_lines.append(line)

    if code_lines:

        code_lines.reverse()

        fixed_code = '\n'.join(code_lines)

        with open(f"Conversation_Outputs/EvalGPTFix/Guided_APR/Code/{file_name}.txt", 'w', encoding="utf-8") as file:
            file.write(fixed_code)