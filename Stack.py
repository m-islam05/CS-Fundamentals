# Stack
# Implements a simple stack using a Python list

def push(stack, item):
    """Adds an item to the top of the stack."""
    stack.append(item)  # Append item to the end (top) of the stack

def pop(stack):
    """Removes and returns the top item from the stack."""
    if not stack:       # Check if stack is empty
        return None
    return stack.pop()  # Remove and return the last item (top of stack)

# ---------------- MAIN ---------------- #

print("=== STACK ===")
print("This program demonstrates push and pop operations.\n")

stack = [] # init the stack for data


# Menu system for user interaction and choice.
while True:
    print("\nCurrent stack:", stack)
    print("Choose an operation:")
    print("1 - Push")
    print("2 - Pop")
    print("3 - Exit")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    # pushing onto stack.
    if choice == "1":
        item = input("Enter item to push: ")
        push(stack, item)
        print("Item pushed successfully.")
        
    # popping off the stack (no data needs to be supplied as LIFO).
    elif choice == "2":
        popped_item = pop(stack)
        if popped_item is not None:
            print(f"Popped item: {popped_item}")
        else:
            print("Stack is empty, nothing to pop.")
            
    # Exit script.
    elif choice == "3":
        print("\nExiting.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Produce result of final output of state of stack.
print("\nFinal state of stack:", stack)
print("\n--- Complete ---")
