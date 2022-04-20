"""

THE SINGLY LINKED LIST:

This code implements a singly linked list in python.
It is part of a project in which I implemented several fundamental datastructures mostly by using only tha standard library.
Linked lists are common data structures and very efficient in space complexity compared to arrays for example.
On the other hand they are more slowly than othe datastructures.
This linked list is used for the hash table implementation in this project.
The content can be printed by print(name_of_ll_instance)
The linked list can be used as an iterable: see __next__ and __iter__
It contains several methods to append new elemnts, print the elemt a specific position, erase elements, print the lentgh of a the linked list or search for one scecial element.
Further there are exceptions if a method is used in a wrong way. For example if someone tries to delete an element at a position that exceeds the legth of the linked list.
Author: Raphael Lermer

"""


#Implementation of Node
class Node:
    #Node is fundamental to the linked list. Nodes are the small elements which build the linked list. 
    def __init__(self, data=None):
        
        self.data = data #data represents the stored data of the Node. This can be any data type in python. For example a 
        self.next = None

class LinkedList:
    
    def __init__(self):
        
        self.head = Node()
        self.ground_index = -1
        self.pointer_for_iteration = self.head
        self.len = 0
        #self.last = self.head
        
    def __str__(self):
        
        s = '('
        
        c = self.ground_index
        
        current_node = self.head
        
        while current_node != None:
            
            if c >= 0:
                
                if c > 0:
                 
                    s += ','
                
                s = s + str(current_node.data)
            
            current_node = current_node.next
            c += 1
        
        s += ')'
        return s
        
    def __next__(self):
        
        #current = self.head
        #while current.next != None:
            
         #   yield current
          #  current = current.next
        
        self.pointer_for_iteration = self.pointer_for_iteration.next
        
        if self.pointer_for_iteration == None:
            self.pointer_for_iteration = self.head
            raise StopIteration
        
        value = self.pointer_for_iteration.data
        
        return value
    
    def __iter__(self):    
         return self
        
    def append(self, data):
        
        new_node = Node(data)
        
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        
        current_node.next = new_node
        self.len += 1
        
        #self.tail.data = data
        
        #return 0
        
    def length(self):
        """
        length = 0
        current_node = self.head
        
        
        while current_node.next != None:
            current_node = current_node.next
            length += 1
            
        if length == self.len:
            print('worked')
        else:
            print('fail')
        """
        return self.len
    
    
    def get(self,index):
        
        if index > self.len:
            
            raise ValueError('Position exceeds length of list')
            return None
        
        i = self.ground_index
        
        current_node = self.head
        
        #while current_node.next != None:
        while i != index:
            current_node = current_node.next
            i += 1
            
            if current_node == None:
                raise 'overflow error'
            
        return current_node.data
    
    def paste(self,new_element,position):
        
        if position > self.len:
            
            raise ValueError('Position of insertion exceeds length of list')
            return None    
        
        current_node = self.head
        topical_position = self.ground_index +1
        
        while topical_position != position:
            
            try:
            #if current_node.next == None:
            
                current_node = current_node.next 
                topical_position += 1
            
            except AttributeError:
                print('to high position to insert')
                return 0
            
        new_node = Node(new_element)
        new_node.next = current_node.next
        
        current_node.next = new_node
        self.len += 1
        
        return 0
    
    def erase(self, position):
        
        if position > self.len:
            
            raise ValueError('Position of deletion exceeds length of list')
            return None 
        
        current_node = self.head
        topical_position = self.ground_index +1 
        
        while topical_position != position:
            
            current_node = current_node.next
            topical_position += 1
            
            
        current_node.next = current_node.next.next
        self.len -= 1
                
    def search(self, element):
        
        i = self.ground_index
        current_node = self.head
            
        while current_node.data != element:
            current_node = current_node.next
            i += 1
            
            if current_node  == None:
                raise OverflowError('Element not in List')
                return None
            
        return i


if __name__ == '__main__':
        

    N1 = Node(4)

    List1 = LinkedList()
    print(List1.length())
    List1.append(5)
    print(List1.length())
    List1.append(3)
    List1.append(8)
    List1.append('c')
    List1.append(2)
    List1.append(1)
    print(List1.length())
        
    print(List1)
    print(List1.length())
    print(List1.length())

    print(List1.get(3))

    print(List1.get(0))
    print(List1.length())
    List1.paste(9,2)
    print(List1)
    print(List1.length())


    List1.erase(1)
    print(List1)

    print(List1.search(2))
    List1.paste(2, 2)
    print(List1)
    #print(List1.search(10))
    
    for n in List1:
        if n == 8:
            print('break')
            break
            
        print(n)
        print(List1.length())
        
    for n in List1:
        print(n)
        print(List1.length())
        
    
