# Linear Search.

def linear_search(arr, target):
    """Search for an element in the list using linear search."""
    print("\nRunning Linear Search...\n")
    
    for i in range(len(arr)):                      # Visit each index
        print(f"Checking index {i}: {arr[i]}")     # Show progress
        
        if arr[i] == target:                       # Match found
            return i
    
    return -1                                      # Target not found


# ---------------- MAIN PROGRAM ---------------- #

print("=== LINEAR SEARCH ===")
print("This program will show how linear search finds a value.\n")

# Ask user for list input
user_input = input("Enter numbers separated by commas (e.g., 5, 2, 9, 1, 7): ")
arr = [int(x.strip()) for x in user_input.split(",")]   # Convert input to list of ints

# Ask user for target value
target = int(input("Enter a number to search for: "))

# Run search
result = linear_search(arr, target)

# Output result
if result != -1:
    print(f"\n Target found at index {result}!")
else:
    print("\n Target NOT found in the list.")

print("\n--- Complete ---")
