def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        line, text = text[:end], text[end:]
        lines.append(line)

    if text:  # Add this line to include any remaining text
        lines.append(text)  # This line is where the change is made

    return lines
