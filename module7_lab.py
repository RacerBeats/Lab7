# Dillan Desai, ID: 10629536
# Group Members: Ryan Cheung, Francisco Ortega
# CS 031
# Prof. Ashraf
# 4/6/25
# Week 7 Lab: Implementing Stacks and Queues

#import Node and LinkedList classes
from Node import Node
from LinkedList import LinkedList

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
    
class ArrayQueue:
    """ A queue class using an array based implementation."""
    def __init__(self, max_length=-1):
        """Initialize the queue with an empty array of specified capacity."""
        self.queue_list = [0]
        self.front_index = 0
        self.length = 0
        self.max_length = max_length

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
        #if max length, return False
        if self.length == self.max_length:
            return False
        
        #resize if length = allocation size
        if self.length == len(self.queue_list):
            self.resize()
        
        #enqueue the item
        item_index = (self.front_index + self.length) % len(self.queue_list)
        self.queue_list[item_index] = call_details
        self.length += 1
        return True

    def dequeue(self):
        #raise error if empty
        if self.is_empty():
            raise IndexError('Cannot dequeue from an empty queue.')

        #get the front item
        call = self.array[self.front_index]

        # Set the front position to None
        self.array[self.front_index] = None

        #decremement length, advance front index
        self.front_index = (self.front_index + 1) % len(self.queue_list)
        self.length -= 1

        #return front item
        return call
    
    def resize(self):
        """double capacity of array when it becomes full"""
        #create new list and copy existing items
        new_size = len(self.queue_list) * 2
        new_list = [0] * new_size

        #copy items to new list
        if self.max_length >= 0 and new_size > self.max_length:
            new_size = max_length
        
        current_index = self.front_index
        for i in range(self.length):
            item_index = (current_index + i) % len(self.queue_list)
            new_list[i] = self.array[item_index]
        
        #assign new list and reset front index to 0
        self.queue_list = new_list
        self.front_index = 0
        self.array = new_array
        self.capacity = new_capacity
        self.rear_index = self.length - 1

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
    
    # Test the front method
    print('Checking the front call in the queue:')
    print(call_queue.front())
    print()
    
    # Test the dequeue method
    print('Dequeuing calls from the queue:')
    print(call_queue.dequeue())
    print(call_queue.dequeue())
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
    
    # Print all calls in the queue
    print('All calls in the queue:')
    for i in range(call_queue.get_size()):
        index = (call_queue.front_index + i) % call_queue.capacity
        print(call_queue.array[index])