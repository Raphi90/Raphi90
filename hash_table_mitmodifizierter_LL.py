
import linked_list as ll


class Adapted_LinkedList(ll.Linked_List):
    
    def search4content(self, key = None, content = None):
        
        i = self.ground_index
        current_node = self.head
        
        if key == None and content == None:
            raise  'unvalid input'
            
        if content == None:
            
            while list(current_node.data.keys())[0] != key:
                current_node = current_node.next
                i += 1
                
                if current_node  == None:
                    
                    return 0
            
        if key == None:
                
            while current_node.data[key] != content:
                current_node = current_node.next
                i += 1
                
                if current_node  == None:
                    
                    return 0
        
        
        if key != None and content != None:
            
            element = {key: word}
            
            while current_node.data != element:
                current_node = current_node.next
                i += 1
                
                if current_node  == None:
                    
                    return 0    
    


class HashTable:
    
    def __init__(self,size):
        
        self.size = size
        self.primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
        self.array = [None] * self.size
        
    def hash(self,input):
        
        counter = 1
        hash_code = 0
        
        for char in input:
            
            ascii_value = ord(char)
            hashValue = self.primes[ascii_value + 30]*self.primes[counter]
            hash_code += hashValue
            counter += 1
        
        return hash_code
    
    def mapp(self,hash_code):
        
        index = hash_code % self.size
        
        return index

    def inclose(self,value,word):
        key = self.hash(word)
        index = self.mapp(key)
        
        if self.array[index] == None:
            self.array[index] =  {word: value}
            
        elif type(self.array[index]) == Adapted_LinkedList:
            print('mehrfachkollision!')
            self.array[index].append({word: value})

        else:
            print('collision!')
            #print(value)
            L = Adapted_LinkedList()
            L.append(self.array[index])
            L.append({word: value})
            self.array[index] = L
            
    def read(self, word):
        
        key = self.hash(word)
        index = self.mapp(key)
        
        if type(self.array[index]) == dict:
            value = self.array[index][word]
            #print('int')
            
        else:
            #print(self.pointer_for )
            #print(word)
            #print(type(self.array[index]))
            #print(self.array[index])
            
            for n in self.array[index]:
                superkey = list(n.keys())[0] #dict key
                #print(word)
                #print(superkey)
                #print(key)
                
                if superkey == word:
                    value = n[superkey]
                    #print('!!')
                    #print(value)
                    #return value
                    self.array[index].pointer_for_iteration = self.array[index].head
                    break
        
        return value
    
    #def delete(self,value,word):
    def delete(self, word):
        
        key = self.hash(word)
        index = self.mapp(key)
        
        if type(self.array[index]) == dict:
            self.array[index] = None
        else:
            #ll.Linked_List.search(element)
            print(self.array[index])
            pos = self.array[index].search4content(word)
            #pos = self.array[index].search({word: value})
            self.array[index].erase(pos)
        
        return 0      
    
    
F = HashTable(30)
values = [3,    4,    5,   6,     7]
words = ['hi', 'I', 'am','new', 'ma']
c = 0

for word in words:
    
    value = values[c]
    F.inclose(value,word)
    c += 1


print(F.array)

for word in words:
    
    print(F.read(word))
    #print(code)

F.inclose(8,'ih')

print(F.read('hi'))
print(F.read('am'))
print(F.read('ma'))

#print(F.array)
#F.delete('am')
#print(F.read('am'))


