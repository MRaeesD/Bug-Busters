length_by_path[i, j] = min(length_by_path[i, j], length_by_path[i, k] + length_by_path[j, k])  # Change: `k` to `k` in `length_by_path[j,k]`
