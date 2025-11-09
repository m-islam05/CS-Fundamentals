# Merge Sort.
# Sort a list of elements in an array through the Merge Sort algorithm.
def merge_sort(arr):
    """Sorts a list using merge sort."""
    if len(arr) <= 1:               # Base case: a list of 0 or 1 element is already sorted
        return arr

    mid = len(arr) // 2              # Find middle index to split list
    left = merge_sort(arr[:mid])     # Recursively sort left half
    right = merge_sort(arr[mid:])    # Recursively sort right half

    return merge(left, right)        # Merge the sorted halves

def merge(left, right):
    """Merges two sorted lists into one sorted list."""
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):  # Compare elements from both lists
        if left[left_index] < right[right_index]:
            result.append(left[left_index])        # Take element from left if smaller
            left_index += 1
        else:
            result.append(right[right_index])      # Take element from right if smaller
            right_index += 1

    result.extend(left[left_index:])               # Add remaining elements from left
    result.extend(right[right_index:])             # Add remaining elements from right
    return result

# ---------------- MAIN PROGRAM ---------------- #

print("=== MERGE SORT ===")
print("This program enables Merge Sort Operations.\n")

# Ask user for list input
user_input = input("Enter numbers separated by commas (e.g., 12, 5, 7, 3, 8): ")
arr = [int(x.strip()) for x in user_input.split(",")]   # Convert input to list of ints

# Sort the list using merge sort
sorted_arr = merge_sort(arr)

# Display the sorted result
print("\n Sorted array:", sorted_arr)
print("\n--- Complete ---")
