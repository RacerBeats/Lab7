# Dillan Desai, ID: 10629536
# Group Members: Ryan Cheung, Francisco Ortega
# CS 031
# Prof. Ashraf
# 4/6/25
# Week 7 Lab: Implementing Stacks and Queues

#import Node and LinkedList classes
#from Node import Node
#from LinkedList import LinkedList

#Temp fix: have node and linked list classes in same file
class Node:
    """A node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A linked list implementation."""
    def __init__(self):
        self.head = None
        self.size = 0
    
    def prepend(self, new_node):
        """Add a node to the beginning of the list."""
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    def remove_after(self, prev_node):
        """Remove the node after prev_node. If prev_node is None, remove the head."""
        if self.head is None:
            return
        
        if prev_node is None:
            # Remove the head
            self.head = self.head.next
        elif prev_node.next is not None:
            # Remove the node after prev_node
            prev_node.next = prev_node.next.next
        
        self.size -= 1

"""
Stack class: This is a stack implementation using a linked list. It simulates a stack of customer cancellation details.
"""
class Stack:
    """A stack class using a linked list."""
    def __init__(self):
        """Initialize the stack using an empty linked list."""
        self.list = LinkedList()
    
    def push(self, cancellation_details):
        """Push a new cancellation detail to the front of the stack, using the prepend method of the linked list."""
        new_node = Node(cancellation_details)
        self.list.prepend(new_node)

    def pop(self):
        """Pop the top cancellation detail from the stack, using the remove_after method of the linked list.
        Remove the head of the linked list and return its data. Also check if the stack is empty before popping."""
        if self.list.head is None:
            raise IndexError('Incorrect attempt to pop from an empty stack.')
        # Store the data of the head node to return it later
        item_to_pop = self.list.head.data
        self.list.remove_after(None)
        return item_to_pop
    
    def peek(self):
        """Peek at the top cancellation detail of the stack without removing it. 
        Checks if the stack is empty first."""
        if self.list.head is None:
            raise IndexError('Incorrect attempt to peek from an empty stack.')
        return self.list.head.data
    
    def is_empty(self):
        """Check if the stack is empty by checking if the head of the linked list is None."""
        if self.list.head is None:
            return True
        else:
            return False
        
    def get_size(self):
        """Get the size of the stack by returning the size of the linked list."""
        return self.list.size
    
class Queue:
    """ A queue class using an array based implementation."""
    def __init__(self, capacity=5):
        """Initialize the queue with an empty array of specified capacity."""
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
        self.front_index = 0
        self.rear_index = -1

    def front(self):
        """Return the customer call at the front of the queue without removing it.
        Raise an error if the queue is empty."""
        if self.is_empty():
            raise IndexError('Cannot access front of an empty queue.')
        return self.array[self.front_index]
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0
    
    def get_size(self):
        """Return the current number of calls in the queue."""
        return self.size

    def enqueue(self, call_details):
        """Add a new customer call to the rear of the queue.
        If the queue is full, resize the array to double its capacity."""
        #if max size, return False
        if self.size == self.capacity:
            self.resize()
        
        #resize if size = allocation size
        if self.size == self.capacity:
            self.resize()
        
        #enqueue the item
        self.rear_index = (self.rear_index + 1) % self.capacity
        self.array[self.rear_index] = call_details
        self.size += 1

    def dequeue(self):
        #raise error if empty
        if self.is_empty():
            raise IndexError('Cannot dequeue from an empty queue.')

        #get the front item
        call = self.array[self.front_index]

        # Set the front position to None
        self.array[self.front_index] = None

        #decremement size, advance front index
        self.front_index = (self.front_index + 1) % self.capacity
        self.size -= 1

        #return front item
        return call
    
    def resize(self):
        """double capacity of array when it becomes full"""
        #create new list and copy existing items
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        #copy items to new list
        current_index = self.front_index
        for i in range(self.size):
            new_array[i] = self.array[current_index]
            current_index = (current_index + 1) % self.capacity
        
        # Update the queue attributes
        self.array = new_array
        self.capacity = new_capacity
        self.front_index = 0
        self.rear_index = self.size - 1

if __name__ == '__main__':
    """Testing the Stack class"""
    print("Testing Ticket Management System Stack")
    print("===================================")

    #instantiate a Stack object
    customer = Stack()

    #testing certain operations on an empty stack
    print('Is the stack empty?')
    print(customer.is_empty())
    print('Size of stack:', customer.get_size())

    #test the peek method on an empty stack
    print('Peeking at the top cancellation detail:')
    try:
        print(customer.peek())
    except IndexError as e:
        print(e)

    #test the pop method on an empty stack
    print('Popping cancellation details from the stack:')
    try:
        print(customer.pop())
    except IndexError as e:
        print(e)

    #test the push method with 4 cancellation details
    print()
    print('Pushing cancellation details onto the stack:')
    customer.push("Order 1: Cancelled - customer was not available")
    customer.push("Order 2: Cancelled - customer changed mind")
    customer.push("Order 3: Cancelled - customer found a better price")
    customer.push("Order 4: Cancelled - customer moved")

    #print the stack after pushing the cancellation details
    print('Stack after push:')
    node = customer.list.head
    while node != None:
       print(node.data)
       node = node.next
    print()

    #test the pop method
    print('Popping cancellation details from the stack:')
    print(customer.pop())
    print(customer.pop())
    print()

    #test the peek method
    print('Peeking at the top cancellation detail:')
    print(customer.peek())
    print()

    #test the is_empty method
    print('Is the stack empty?')
    print(customer.is_empty())
    print()

    #test the get_size method
    print('Size of stack:', customer.get_size())

    print("\n\nTesting Customer Service Call Queue")
    print("===================================")
    
    # Instantiate a Queue object
    call_queue = Queue()
    
    # Testing operations on an empty queue
    print('Is the queue empty?')
    print(call_queue.is_empty())
    print('Size of queue:', call_queue.get_size())
    print('Verification - Array state:', call_queue.array)

    # Test the front method on an empty queue
    print('Checking the front call in the queue:')
    try:
        print(call_queue.front())
    except IndexError as e:
        print(e)
    
    # Test the dequeue method on an empty queue
    print('Dequeuing a call from the queue:')
    try:
        print(call_queue.dequeue())
    except IndexError as e:
        print(e)
    
    # Test the enqueue method with several calls
    print('\nEnqueuing customer service calls:')
    call_queue.enqueue("Call 1: Customer needs help with ticket transfer")
    call_queue.enqueue("Call 2: Customer requesting refund information")
    call_queue.enqueue("Call 3: Customer inquiring about event details")
    call_queue.enqueue("Call 4: Customer reporting website issues")
    call_queue.enqueue("Call 5: Customer needs assistance with seating arrangements")
    
    # Print the queue after enqueuing calls
    print('Queue after enqueuing calls:')
    for i in range(call_queue.get_size()):
        index = (call_queue.front_index + i) % call_queue.capacity
        print(call_queue.array[index])
    print()
    
    # Verify queue size and contents
    print('Verification:')
    print('Reported size:', call_queue.get_size())
    print('Capacity:', call_queue.capacity)
    print('Front index:', call_queue.front_index)
    print('Rear index:', call_queue.rear_index)
    print('Full array state:', call_queue.array)
    print()

    # Test the front method
    print('Checking the front call in the queue:')
    print(call_queue.front())
    print()
    
    # Test the dequeue method
    print('Dequeuing calls from the queue:')
    print(call_queue.dequeue())
    print(call_queue.dequeue())
    print()
    
    # Verify queue size after dequeuing
    print('Verification after dequeuing:')
    print('Reported size:', call_queue.get_size())
    print('Capacity:', call_queue.capacity)
    print('Front index:', call_queue.front_index)
    print('Rear index:', call_queue.rear_index)
    print('Full array state:', call_queue.array)
    print()

    # Check the front call after dequeuing
    print('Checking the front call after dequeuing:')
    print(call_queue.front())
    print()
    
    # Test the is_empty method
    print('Is the queue empty?')
    print(call_queue.is_empty())
    print()
    
    # Test the get_size method
    print('Size of queue:', call_queue.get_size())
    print()
    
    # Test resizing by adding more calls
    print('Testing queue resizing by adding more calls:')
    call_queue.enqueue("Call 6: Customer needs help with group booking")
    call_queue.enqueue("Call 7: Customer inquiring about parking options")
    call_queue.enqueue("Call 8: Customer requesting accessibility information")
    
    # Print the queue after resizing
    print('Queue after adding more calls (should resize):')
    print('New capacity:', call_queue.capacity)
    print('Current size:', call_queue.get_size())

    # Verify queue size and contents after resizing
    print('Verification after resizing:')
    print('Reported size:', call_queue.get_size())
    print('Capacity:', call_queue.capacity)
    print('Front index:', call_queue.front_index)
    print('Rear index:', call_queue.rear_index)
    print('Full array state:', call_queue.array)
    print()
    
    # Print all calls in the queue
    print('All calls in the queue:')
    for i in range(call_queue.get_size()):
        index = (call_queue.front_index + i) % call_queue.capacity
        print(call_queue.array[index])