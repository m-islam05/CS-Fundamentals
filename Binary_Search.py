# Binary Search.

# Binary search implementation (works on sorted lists)

def binary_search(arr, target):
    """Performs binary search on a sorted list."""
    left, right = 0, len(arr) - 1   # Set search boundaries (start and end)
    
    while left <= right:           # Continue while valid search range exists
        mid = (left + right) // 2  # Find middle index
        
        if arr[mid] == target:     # Check if mid is target
            return mid             # Return index if found
        
        elif arr[mid] < target:    # If target is greater, search right half
            left = mid + 1
        
        else:                      # If target is smaller, search left half
            right = mid - 1
    
    return -1  # Target not found in list


# Example usage
arr = [5, 10, 15, 20, 25]  # Sorted list to search

target = int(input("Enter a number to search for: "))  # Get target from user

result = binary_search(arr, target) # call the function.


# Identification if Value Found.
if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found")
