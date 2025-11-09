# Queue DSA.

def enqueue(queue, item):
    """Adds an item to the end of the queue."""
    queue.append(item)  # Append item to the back of the queue

def dequeue(queue):
    """Removes and returns the front item from the queue."""
    if not queue:       # Check if queue is empty
        return None
    return queue.pop(0) # Remove and return the first item (FIFO)

# ---------------- MAIN PROGRAM ---------------- #

print("=== QUEUE ===")
print("This program lets you enqueue or dequeue items interactively.\n")

queue = [] # init the queue array

# Menu system for user to choose operation.
while True:
    print("\nCurrent queue:", queue)
    print("Choose an operation:")
    print("1 - Enqueue")
    print("2 - Dequeue")
    print("3 - Exit")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    # Enqueue.
    if choice == "1":
        item = input("Enter item to enqueue: ")
        enqueue(queue, item)
        print("Item enqueued successfully.")
        
    # Dequeue.
    elif choice == "2":
        deq_item = dequeue(queue)
        if deq_item is not None:
            print(f"Dequeued item: {deq_item}")
        else:
            print("Queue is empty, nothing to dequeue.")
            
    # Exit.
    elif choice == "3":
        print("\nExiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("\nFinal state of queue:", queue)
print("\n--- Complete ---")
