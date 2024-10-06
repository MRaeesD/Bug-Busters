def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        else:
            end += 1  # Include space to not leave it at the start
        line, text = text[:end], text[end:]
        lines.append(line)

    # Append the remaining text if any
    if text:
        lines.append(text)
    
    return lines
