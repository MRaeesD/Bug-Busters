def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        for c in range(0, r + 1):  # Adjusted to iterate correctly for each row length
            upleft = rows[r - 1][c - 1] if c > 0 else 1  # Corrected to handle the edge value
            upright = rows[r - 1][c] if c < len(rows[r - 1]) else 0  # Corrected to ensure bounds check
            row.append(upleft + upright)
        rows.append(row)

    return rows