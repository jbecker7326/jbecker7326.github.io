'''
Created on Jan 30, 2022

@author: Jennifer Becker

Program for heapsort algorithm
'''

def heapify(sequence, n, i):
    # initialize max value as the passed root
    maxval = i 

    # initialize left and right child node index values
    left = 2 * i + 1
    right = 2 * i + 2
    
    # if left child node exists and is greater than root, set max value to left
    if left < n and sequence[maxval] < sequence[left]:
        maxval = left  
        
    # if right child node exists and is greater than root, set max value to right
    if right < n and sequence[maxval] < sequence[right]:
        maxval = right
        
    # swap root to new value if needed
    if maxval != i:
        sequence[i], sequence[maxval] = sequence[maxval], sequence[i]
        
        # recursively send sequence and root back to heapify
        heapify(sequence, n, maxval)
        

def heapsort(sequence):  
    # get length of sequence
    n = len(sequence)     
    
    # transform sequence into a max heap, assuming that the root is at n//2
    for i in range(n//2 - 1, -1, -1):
        heapify(sequence, n, i)
        
    # convert max heap to sorted list
    for i in range(n - 1, 0, -1):
        sequence[i], sequence[0] = sequence[0], sequence[i]
        heapify(sequence, i, 0)
        
    return sequence
    