'''
Created on Mar 6, 2022

@author: Jennifer Becker

open address hash table super-class with sub-classes for linear, quadratic and double hash probing methods.
'''

class HashTable():
    # initialize class
    def __init__(self, size):
        self.size = size
        self.hashtable = [None] * self.size
        self.collisions = 0

    # put operation throws error if table is full
    def put(self, key, value):
        index = self.probing(key)
        if index > self.size:
            raise Exception('Table is full!')
        
        p = self.hashtable[index]
        if p == None:
            self.hashtable[index] = [key, value]

    # get operation returns value if key is present. if not, returns null.
    def getValue(self, key):
        index = self.probing(key)

        if index > self.size:
            return None
        elif self.hashtable[index][0] == key:
            return self.hashtable[index][1]
        elif self.hashtable[index] != None:
            return self.hashtable[index][1]
        else:    
            return None    

    # get operation returns key if index is present. if not, returns none.
    def get(self, index):

        if index > self.size:
            return None
        if self.hashtable[index] == None:
            return None
        else:    
            return self.hashtable[index]
                               
    # returns number of collisions
    def getCollisions(self):
        return self.collisions
    
class LinearHashTable(HashTable):
    
    # initialize with superclass ProbingHash
    def __init__(self, size):
        super().__init__(size)
 
    # define linear probing function
    def probing(self, key):
        index = int(key) % self.size
        
        # use suggested index if spot is available
        if self.hashtable[index] == None or self.hashtable[index][0] == key:       
            return index
        # if not available, implement linear probe
        else:
            j = 1
            index2 = index                                   
            while self.hashtable[index2] != None and self.hashtable[index2][0] != key:
                self.collisions += 1            # increment collisions
                index2 = (index + j) % self.size
                j += 1
                
            return index2


class QuadraticHashTable(HashTable):
    
    # initialize with superclass ProbingHash
    def __init__(self, size):
        super().__init__(size)

    # define quadratic probing function    
    def probing(self, key):

        index = int(key) % self.size
        
        # use suggested index if spot is available
        if self.hashtable[index] == None or self.hashtable[index][0] == key:       
            return index
        # if not available, implement quadratic probe
        else:
            j = 1
            index2 = index                                   
            while self.hashtable[index2] != None and self.hashtable[index2][0] != key:
                self.collisions += 1            # increment collisions
                index2 = (index + (j*j)) % self.size
                j += 1
    
            return index2
            
            
class DoubleHashTable(HashTable):

    # initialize with superclass ProbingHash with additional input parameter doubleFactor 
    def __init__(self, size, doubleFactor):
        super().__init__(size)    
        self.doubleFactor = doubleFactor

    # define secondary hash for double probing hashing
    def doubleHash(self, key):
        return(self.doubleFactor - (key % self.doubleFactor))       

    # define double hash probing function
    def probing(self, key):
        index = int(key) % self.size
        
        # use suggested index if spot is available
        if self.hashtable[index] == None or self.hashtable[index][0] == key:       
            return index
        # if not available, implement double hash probe
        else:
            j = 1
            hash2index = self.doubleHash(key)  
            index2 = index                                 
            while self.hashtable[index2] != None and self.hashtable[index2][0] != key:
                self.collisions += 1            # increment collisions
                index2 = (index + (hash2index * j)) % self.size   # calculate double hash probe index
                j += 1
    
            return index2
