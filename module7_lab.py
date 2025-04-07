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