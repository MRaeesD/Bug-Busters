def find_duplicates(arr):
    """
    Finds and returns a list of duplicate elements in an array.

    Args:
        arr: A list of elements.

    Returns:
        A new list containing only the duplicate elements from the input array, 
        preserving their original order of appearance.
    """
    if not arr:  # Explicitly handle empty input
        return []
    
    seen = {}
    duplicates = []

    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen[num] = True

    return duplicates

# Example usage
print(find_duplicates([1, 2, 3, 4, 5, 1, 2, 3]))  # Expected output: [1, 2, 3]

def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # Collect lengths of subsequences that can be extended by val
        # Fix: Check if key 'j' exists in 'ends' before accessing 
        prefix_lengths = [j for j in range(1, longest + 1) if j in ends and arr[ends[j]] < val] 

        length = max(prefix_lengths) if prefix_lengths else 0

        # Fix: Ensure the subsequence is increasing and handle potential KeyError
        if length == longest or (length + 1 not in ends or val < arr[ends[length + 1]]):  
            ends[length + 1] = i
            # Fix: Update 'longest' correctly
            longest = max(longest, length + 1) 

    return longest