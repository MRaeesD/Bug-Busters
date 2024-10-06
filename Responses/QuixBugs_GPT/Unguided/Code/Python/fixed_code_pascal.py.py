def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        for c in range(0, r + 1):  # Fix the loop to range up to r + 1
            upleft = rows[r - 1][c - 1] if c > 0 else 1  # Set first element to 1
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows