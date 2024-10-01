# Python code

def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:q
            end = cols
        line, text = text[:end], text[end:]
        lines.append(line)
    
    # Ensure the final segment of text is included
    if text:
        lines.append(text)  # BUG FIX: Append remaining text to lines
    
    return lines