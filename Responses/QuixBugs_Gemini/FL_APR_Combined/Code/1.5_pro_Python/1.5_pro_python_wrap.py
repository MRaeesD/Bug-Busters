def wrap(text, cols):
        lines = []
        while len(text) > cols:
            # Find the last space within the allowed column width
            end = text.rfind(' ', 0, cols) 
            if end == -1:
                end = cols
            # Exclude the space at 'end' from the next line
            line, text = text[:end], text[end + 1:] 
            lines.append(line)
        if text:  # Add any remaining text
            lines.append(text)
        return lines
