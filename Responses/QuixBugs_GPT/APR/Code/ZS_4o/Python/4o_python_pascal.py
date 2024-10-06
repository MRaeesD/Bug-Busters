def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = [1]  # Starting each row with 1
        for c in range(1, r):  # Corrected iteration to start from 1 and end at r-1
            upleft = rows[r - 1][c - 1]
            upright = rows[r - 1][c]
            row.append(upleft + upright)
        row.append(1)  # Ending each row with 1
        rows.append(row)

    return rows
