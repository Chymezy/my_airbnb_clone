#!/usr/bin/python3

'''
    Write a class Node that defines a node of a singly linked list by:

    Private instance attribute: data:
    property def data(self): to retrieve it
    property setter def data(self, value): to set it:
    data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
    Private instance attribute: next_node:
    property def next_node(self): to retrieve it
    property setter def next_node(self, value): to set it:
    next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
    Instantiation with data and next_node: def __init__(self, data, next_node=None):
    And, write a class SinglyLinkedList that defines a singly linked list by:

    Private instance attribute: head (no setter or getter)
    Simple instantiation: def __init__(self):
    Should be printable:
    print the entire list in stdout
    one node number by line
    Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)
    You are not allowed to import any module
'''
class Node:
   
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self._data = value
    @property
    def next_node(self):
        return self._next_node
 
    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self._next_node = value

    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

class SinglyLinkedList:
    def __init__(self):
        self._head = None
    
    def sorted_insert(self, value):
        
        new = Node(value)
        
        if self._head is None:
            new.next_node = None
            self._head = new
        
        elif self._head.data > value:
            new.next_node = self._head
            self._head = new
        else:
            temp = self._head 
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node 
            new.next_node = temp.next_node 
            temp.next_node = new 
    
    def __str__(self):
        items = []
        temp = self._head
        while temp is not None:
            items.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(items))

    