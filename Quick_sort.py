# Quick Sort Algorithm.


# function for quick sort.
def quick_sort(arr):
    """Sorts a list using quick sort."""
    if len(arr) <= 1:  # Base case: a list with 0 or 1 element is already sorted.
        return arr

    pivot_value = arr[len(arr) // 2]  # Choose middle element as pivot.

    smaller_elements = [current_element for current_element in arr if current_element < pivot_value]   # Elements less than pivot
    equal_elements = [current_element for current_element in arr if current_element == pivot_value]    # Elements equal to pivot
    larger_elements = [current_element for current_element in arr if current_element > pivot_value]    # Elements greater than pivot

    # Recursively sort smaller and larger elements and combine all.
    return quick_sort(smaller_elements) + equal_elements + quick_sort(larger_elements)


# ---------------- MAIN ---------------- #

print("=== QUICK SORT ===")
print("This program sorts a list using quick sort.\n")

# Ask user for list input
user_input = input("Enter numbers separated by commas (e.g., 3, 6, 8, 10, 1, 2): ")
arr = [int(x.strip()) for x in user_input.split(",")]  # Convert input to list of ints

# Sort the list using quick sort
sorted_arr = quick_sort(arr)

# Display the sorted result
print("\n Sorted array:", sorted_arr)
print("\n--- Complete ---")
