def pascal(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n: The number of rows to generate.

    Returns:
        A list of lists representing Pascal's Triangle.
    """
    rows = [[1]]  # Initialize with the first row
    for r in range(1, n):
        row = []
        for c in range(0, r + 1):  # Fixed range to r + 1 to include all elements in the row
            if c == 0 or c == r:
                row.append(1)  # Edge elements are always 1
            else:
                upleft = rows[r - 1][c - 1] 
                upright = rows[r - 1][c]
                row.append(upleft + upright)  # Calculate inner element by summing the two above
        rows.append(row)

    return rows