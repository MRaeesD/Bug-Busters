def pascal(n):
        rows = [[1]]
        for r in range(1, n):
            row = []
            for c in range(0, r + 1):  # Bug fix: Changed 'r' to 'r + 1'
                upleft = rows[r - 1][c - 1] if c > 0 else 0
                # Bug fix: Changed 'c < r' to 'c < r' to access the last element
                upright = rows[r - 1][c] if c < r else 0 
                row.append(upleft + upright)
            rows.append(row)

        return rows
