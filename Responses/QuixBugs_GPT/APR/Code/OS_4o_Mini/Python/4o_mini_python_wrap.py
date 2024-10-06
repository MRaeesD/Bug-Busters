def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        line, text = text[:end], text[end:]
        lines.append(line)
    
    # Adding the remaining text as the last line if any
    if text:
        lines.append(text)  # Change made here

    return lines
