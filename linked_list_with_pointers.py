
class Node:
    
    def __init__(self, data = None):
        
        self.previous = None
        self.following = None
        self.data = data


class LinkedList:
    

    def __init__(self):
        

        self.head_pointer = Node()
        self.tail_pointer = Node()
        
        #self.current_pointer = Node()
        self.head_pointer.following = self.tail_pointer
        self.tail_pointer.following = self.head_pointer
        
        
                
    def pushhead(self, x):
        #Pushhead inserts the element x to the head of the list
        newNode = Node(x)
        newNode.following = self.head_pointer.following
        self.head_pointer.following = newNode
        #print(self.tail_pointer.following.following.data)
        #self.tail_pointer = self.tail_pointer.following.following
        if self.head_pointer.following.following == self.tail_pointer:
            self.tail_pointer.following = self.tail_pointer.following.following
        
        return 0
    
    def __str__(self):
        
        s = '('
        #s += str(self.head_pointer.data)
        current_node = self.head_pointer.following
        
        while current_node != self.tail_pointer:
            
            s += str(current_node.data)
            
            
            if current_node.following != self.tail_pointer:
                s += ','
            current_node = current_node.following
            
        s += ')'

        return s
    
    def search(self,x):
        
        current_node = self.head_pointer#.following
        position = 0
        
        while current_node != self.tail_pointer:
            
            current_node = current_node.following
            
            
            if current_node.data == x:
                
                return position
                break
                
            position += 1    
            
        if current_node == self.tail_pointer:
            print("Element not in list!")
            position = -1
            
        return position
    
    def insert_at(self, x, position):
        
        current_node = self.head_pointer
        topical_position = 0
        newNode = Node(x)
        
        while current_node != self.tail_pointer:
            
            if topical_position == position:
                
                if current_node == self.tail_pointer.following:
                    self.tail_pointer.following = newNode
                
                newNode.following = current_node.following
                current_node.following = newNode
                
                break
                
            topical_position += 1
            current_node = current_node.following
    
        
        return 0
    
    
    def delete(self,x):
        
        current_node = self.head_pointer
        
        #topical_position = 0
        #newNode = Node(x)
        
       #if current_node.data == x:
        #   print("yeah!")
         #  self.head_pointer.following = current_node.following.following
       #else:
        
        while current_node != self.tail_pointer:
            
            if current_node.following.data == x:
                
                 if current_node.following.following == self.tail_pointer:
                     #the one that gets deleted is the one before final gets deleted
                     self.tail_pointer.following = current_node
                     print('yes')
                     
                 #print(current_node.following.following.data)
                 current_node.following = current_node.following.following
                 break
                
            current_node = current_node.following
        
        if current_node == self.tail_pointer:
            print("Element not in list!")
            position = -1
        
        #    raise "Element not in list!"
        
        return 0
    """
    def copy(self):
        
        current_node = self.head_pointer
        
        copy = LinkedList()
        current_node_copy = Node()
        
        while current_node != self.tail_pointer:
            
            current_node_copy.following = Node()
            current_node_copy.data = current_node.data
            
            current_node_copy = current_node_copy.following
            
            #if current_node.following.data == :
                 #print(current_node.following.following.data)
             #    current_node.following = current_node.following.following
              #   break
            
            current_node = current_node.following
            
        #current_node_copy.following = copy.head_pointer
        copy.head_pointer.following = current_node_copy
        
        return copy


    def __mul__(self, n):
        
        new = LinkedList()
        c = self.copy(self)
        counterc = c
        
        for n in range(1,n):
            
            counterc.tail_pointer.following.following = c.head_pointer.following
        #    counterc.tail_pointer = 
            
        #new.tail_pointer.following.following = 
                        
            #self.head_pointer = c
                      
        return new
    """
    
    def __add__(self, other):
        
       
        new = self
        
        
        
        
        current_node = self.head_pointer
        """
        if self == other:
            
            print("yes")
            while current_node.following != self.tail_pointer:
                current_node = current_node.following
                print(current_node.data)
            
            copy = self.head_pointer.following
            current_node.following = copy
            print('f')
            return self
            """
    
        while True:#current_node != self.tail_pointer:
                
            if current_node.following == new.tail_pointer:
                current_node.following = other.head_pointer.following
                #print('#')
                break
            
            current_node = current_node.following
        new.tail_pointer = other.tail_pointer
        #new.tail_pointer.following = self.head_pointer
        
        
        return new
    
    
    def print_final(self):
        
        print(self.tail_pointer.following.data)
        
        return self.tail_pointer.following.data
        
        
            
            
L = LinkedList()
print(L)
L.print_final()

L.pushhead(4)
print(L)
L.print_final()

L.pushhead(5)
print(L)
L.print_final()

L.pushhead(0)
print(L)
L.print_final()

L.pushhead(20)
print(L)
L.print_final()


print(L.search(20))
print(L.search(5))
print(L.search(25))

L.insert_at(2, 2)
print(L)
L.insert_at(88,0)
print(L)
L.print_final()

L.insert_at(88,5)
print(L)
L.print_final()

L.insert_at(88,7)
print(L)
L.print_final()

L.insert_at(88,10)
print(L)

L.delete(20)
print(L)
L.delete(88)
print(L)
L.delete(7)
print(L)
L.print_final()

L.delete(88)
print(L)
L.delete(88)
print(L)
L.print_final()

print('xx')


L1 = LinkedList()

L1.pushhead(14)
L1.pushhead(53)
L1.pushhead(50)
L1.pushhead(2)
print(L1)


L2 = L+L1

print(L2)
Lx = L1


L4 = LinkedList()

L4.pushhead(14)
L4.pushhead(53)
L4.pushhead(50)
L4.pushhead(2)

print(L4)
print(L2)
print(Lx)
L3 = L4 + Lx

print(L3)

L3.print_final()

#Ly = Lx + Lx
#print(Ly)


