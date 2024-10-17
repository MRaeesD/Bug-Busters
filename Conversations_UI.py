import autogen
import panel as pn
import openai
import os
import time
from dotenv import load_dotenv
import random
import os
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union
from dotenv import load_dotenv
import pandas as pd
import random
from PIL import Image
from termcolor import colored
import autogen
from autogen import Agent, AssistantAgent, ConversableAgent, UserProxyAgent
from autogen.code_utils import DEFAULT_MODEL, UNKNOWN, content_str, execute_code, extract_code, infer_lang


load_dotenv()

random_seed = 42

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

APR_initializer = autogen.UserProxyAgent(
    name="Init_2",
    code_execution_config={
        "use_docker": False,
    },
    human_input_mode="NEVER",
    is_termination_msg=lambda x: content_str(x.get("content")).find("TERMINATE") >= 0,
)

fault_localisation_debugger_1 = autogen.AssistantAgent(
    name="fault_localisation_debugger_1",
    llm_config=gpt_4o_config,
    system_message="""You are a fault localization debugger. Your task is to identify the most likely bug(s) in a given code sample. Follow these steps:

Bug Identification: Identify the bug(s) in the code. Justify why each is a bug.
Analysis: Use the provided explanation of the code's intended functionality to support your analysis.
Confidence Ranking: Rank the identified bugs by likelihood and provide a confidence percentage for each.
Turn-based Discussion: You must engage in a turn-based discussion with an external debugging agent in the group chat. Wait for the other agent's input before responding. Discuss the identified bugs, and both agents must contribute to the final decision. Before agreeing and accepting the other agent's fault localisation and feedback, scrutinize and question it's reasoning and provide constructive feedback. Try to achieve a convergence score of 1.0.
Do not finalize the decision until both agents have exchanged input multiple times.
Ask for feedback from the other agent and wait for their response before moving forward.
Code Annotation: After mutual agreement, wrap the code in a code block (specify the script type) and add a comment at the bug location. Do not provide a fix—only mark the location of the bug.
Reply DONE_LOCALISING once both agents have exchanged input multiple times and reached consensus.
After receiving feedback from the judge, only adjust your own response. Do not adjust the other agent's response.
""",
)

fault_localisation_debugger_2 = autogen.AssistantAgent(
    name="fault_localisation_debugger_2",
    llm_config=gemini_pro_config,
    system_message="""You are a fault localization debugger. Your task is to independently identify the bug(s) in a given code sample, then collaborate with another debugging agent to finalize the bug locations. Follow these steps:

Independent Bug Identification:

Initially, ignore the input from the first debugging agent. Identify the bug(s) you believe are present in the code. Justify your selections without referencing the first agent's findings.
Analysis: Use the explanation of the code's intended functionality to support your analysis.

Confidence Ranking: Rank your identified bugs by likelihood and provide a confidence percentage for each.

Turn-based Discussion: After independently identifying the bugs, review the first agent's findings and engage in a turn-based discussion. Compare your analysis with the first agent's, provide feedback, and discuss differences. Both agents must contribute to the final decision. Scrutinize each other's reasoning and provide constructive feedback.

Wait for the other agent's input before responding.
Ensure both agents exchange feedback multiple times before finalizing the decision.
Code Annotation: After mutual agreement with the other agent, wrap the code in a code block (specify the script type) and add a comment at the bug location. Do not provide a fix—only mark the location of the bug.

Reply DONE_LOCALISING once both agents have exchanged input multiple times and reached consensus.
After receiving feedback from the judge, only adjust your own response. Do not adjust the other agent's response.

""",
)

APR_debugger_1 = autogen.AssistantAgent(
    name="APR_debugger_1",
    llm_config=gpt_4o_config,
    system_message="""You are an automatic program repair agent. Your task is to fix the bugs identified by the fault localisation debuggers. Follow these steps:

Bug fixing: Review the bugs identified by the fault localization agents. Propose fixes for the top 3 bugs. Provide explanations for your chosen fixes.
Analysis: Ensure that the proposed fixes address the bugs while maintaining the intended functionality of the code. Reference the code's functionality to justify your fixes.
Turn-based Discussion: You must engage in a turn-based discussion with an external debugging agent in the group chat. Wait for the other agent's input before responding. Discuss the proposed bug fixes, and both agents must contribute to the final decision. Before agreeing and accepting the other agent's repair and feedback, scrutinize and question it's reasoning and provide constructive feedback. Try to achieve a convergence score of 1.0.
Do not finalize the decision until both agents have exchanged input multiple times.
Ask the next agent to propose what they think is the correct fix and wait for the other agent to propose its repair response and thereafter compare your proposed with theirs and ask for feedback. Wait for their response before moving forward.
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
    llm_config=gpt_4o_mini_config,
    system_message="""
You are the reporting agent. Provide a comprehensive summary of the debugging process and the final results.

Summarize the Buggy Lines: Clearly state the lines of code identified as containing bugs, listed in descending order of average probability, along with the reasons for each bug.

Format:
Line(s) of code with bug: <code line(s)>
Reason: <reason for the bug>
Wrap the Agreed Fix: Include the agreed-upon fix in a code block, specifying the script type.

Explain the Fix: Provide a brief explanation of the fix and why it is necessary for the code's functionality.

    """
)

convergence_judge_1 = autogen.AssistantAgent(
    name="convergence_judge_1",
    llm_config=gpt_4o_mini_config,
    system_message=""" You are tasked with evaluating the similarity between two sets of bug identification results provided by two independent fault localisation agents. Each agent has identified potential bugs in a given code snippet.

Your goal is to iteratively assess the convergence between these two sets of results. Start by comparing the identified bugs based on factors such as location, type of issue, and any specific descriptions provided. Based on this comparison, ensure that you provide an initial Convergence Score between 0 and 1 (mandatory), where:

0 indicates no overlap between the two agents' responses
1 indicates a complete match between the two agents' responses.
After each iteration:

Adjust the score by evaluating the areas of divergence or partial agreement between the agents' responses.
Refine the responses of the fault localisation agents (if needed) by providing feedback to bring their results closer. Do not provide any code blocks.
Repeat the process until you determine that the responses fully converge and the score reaches 1.
For each iteration, provide:

The current Convergence Score.
A brief explanation of how you arrived at the score.
Any feedback or adjustments for the agents to achieve better convergence.
Continue iterating until the responses reach full similarity (Convergence Score = 1).
If the convergence is 1.0 say GOOD otherwise say BAD.
""",
)

convergence_judge_2 = autogen.AssistantAgent(
    name="convergence_judge_2",
    llm_config=gpt_4o_mini_config,
    system_message=""" You are tasked with evaluating the similarity between two sets of bug repair results provided by two independent Automated Program Repair (APR) agents. Each agent has proposed fixes for the identified bugs in a given code snippet.

Your goal is to iteratively assess the convergence between these two sets of repairs. Start by comparing the proposed fixes based on factors such as the correctness of the fix, location of changes, type of repairs made, and any specific descriptions provided. Based on this comparison, ensure that you provide an initial Convergence Score between 0 and 1 (mandatory), where:

0 indicates no overlap or similarity between the two agents' proposed repairs.
1 indicates a complete match between the two agents' proposed repairs.
After each iteration:

Adjust the score by evaluating the areas of divergence or partial agreement between the agents' proposed repairs.
Provide feedback to guide the refinement of the repair proposals (if necessary) to bring their results closer to alignment.
Repeat the process until you determine that the responses fully converge and the score reaches 1.
For each iteration, provide:

The current Convergence Score as a number between 0 and 1.
A brief explanation of how you arrived at the score.
Any feedback or adjustments for the agents to achieve better convergence but do not correct the agents' responses directly.
Continue iterating until the responses reach full similarity (Convergence Score = 1). If the convergence is 1.0, say GOOD_REPAIR, otherwise say BAD_REPAIR.
    """,
)

tracking_agent = autogen.AssistantAgent(
    name="tracking_agent",
    llm_config=gpt_4o_mini_config,
    system_message="""You are responsible for keeping track of the judges responses. If the judge says 'GOOD', reply with 'BUG FOUND' to end the fault localisation process. 
    Otherwise reply with 'REDO' to restart the fault localisation debugging process. 
    """
)

tracking_agent_2 = autogen.AssistantAgent(
    name="tracking_agent_2",
    llm_config=gpt_4o_mini_config,
    system_message=""" When the bug in the programme has been repaired, and if atleast two of the three judges say 'GOOD REPAIR' reply with 'BUG_FIXED' to end the repair process.
    Otherwise reply with 'REDO_REPAIR' to restart the repair process. """
)

terminating_agent = autogen.AssistantAgent(
    name="terminating_agent",
    llm_config=gpt_4o_mini_config,
    system_message="""Say TERMINATE. """
)

def state_transition(last_speaker, groupchat):
    messages = groupchat.messages
    
    if any("TERMINATE" in message["content"] for message in messages):
        return None  

    if last_speaker is initializer:
        return fault_localisation_debugger_1
    elif last_speaker is fault_localisation_debugger_1:
        return fault_localisation_debugger_2
    elif last_speaker is fault_localisation_debugger_2:
        return convergence_judge_1
    elif last_speaker is convergence_judge_1:
        if "GOOD" in messages[-1]["content"]:
            return tracking_agent
        return fault_localisation_debugger_1
    elif last_speaker is tracking_agent:
        if "BUG FOUND" in messages[-1]["content"]:
            APR_initializer.send(message="Fix the identified bug in the code based on the previous discussion", recipient=manager)
            return APR_debugger_1
        if "BUG FOUND" in messages[-1]["content"]:
            return fault_localisation_debugger_1 
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
        return terminating_agent
    elif last_speaker is terminating_agent:
        return None
    
    return None


groupchat = autogen.GroupChat(
        agents=[initializer, fault_localisation_debugger_1, fault_localisation_debugger_2, reporting_agent, 
                convergence_judge_1,convergence_judge_2, tracking_agent, tracking_agent_2, APR_initializer, APR_debugger_1, 
                APR_debugger_2, terminating_agent],
        messages=[],
        max_round=20,
        speaker_selection_method=state_transition,
    )
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt_4o_mini_config)


pn.extension(design="material")

def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    initializer.initiate_chat(manager, message=contents)

chat_interface = pn.chat.ChatInterface(callback=callback)               
chat_interface.send("Send us code to debug! \n Ensure that your code is put in a code markdown block.", user="System", respond=False)
chat_interface.servable()

avatar = {initializer.name:"👨‍💼", fault_localisation_debugger_1.name:"👩‍💻",fault_localisation_debugger_2.name:"👩‍💻", 
          APR_debugger_1.name:"👩‍🔬",APR_debugger_2.name:"👩‍🔬", reporting_agent.name:"🗓", tracking_agent.name:"🛠",
          tracking_agent_2.name:"🛠", convergence_judge_1.name:'📝', convergence_judge_2.name:'📝'}

def print_messages(recipient, messages, sender, config):

    chat_interface.send(messages[-1]['content'], user=messages[-1]['name'], avatar=avatar[messages[-1]['name']], respond=False)
    print(f"Messages from: {sender.name} sent to: {recipient.name} | num messages: {len(messages)} | message: {messages[-1]}")
    return False, None  # required to ensure the agent communication flow continues


# Register reply functions for each agent
initializer.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

APR_initializer.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

fault_localisation_debugger_1.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

fault_localisation_debugger_2.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

APR_debugger_1.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

APR_debugger_2.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

reporting_agent.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

convergence_judge_1.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

convergence_judge_2.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

tracking_agent.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

tracking_agent_2.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

terminating_agent.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)