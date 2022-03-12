'''
Created on Mar 11, 2022

@author: Jennie

counting sort algorithms. 
NumberCountingSort takes list of negative and non-numbers as inlist
ABCCountingSort takes list of strings as inlist
'''

def NumberCountingSort(inlist):
    # find min and max values
    min_k, max_k = 0, 0
    for x in range(0, len(inlist)):
        min_k = inlist[x] if inlist[x] < min_k else min_k
        max_k = inlist[x] if inlist[x] > max_k else max_k
    k = abs(min_k) + max_k
        
    # intialize empty count and output arrays
    size = len(inlist)
    output = [0] * size
    count = [0] * (k + 1)
    
    # in the count array, count the amount of each item from the original array
    for x in range(0, size):
        count[inlist[x] + abs(min_k)] += 1
        
    # reset values in count to match actual positional (index) values 
    for x in range(1, len(count)):
        count[x] += count[x - 1]
                
    # find index of each member in original array and place values into output array
    i = size - 1
    while i >= 0:
        output[count[inlist[i] + abs(min_k)] - 1] = inlist[i]
        count[inlist[i] + abs(min_k)] -= 1
        i -= 1
    
    # copy the sorted items back into the original array
    for i in range(0, size):
        inlist[i] = output[i]
        
    return inlist


def StringCountingSort(inlist):

    # parse list into numeric values
    k = 0
    inlist_num = []
    for string in inlist:
        string_num = ''
        for ch in string:
            # convert character to unicode decimal
            num = ord(ch)
            # subtract to set numeric range where a = 1 and Z = 56
            num = num - 38 if num < 97 else num - 96
            # append to string, adding a preceding 0 for values less than 10
            if num < 10 and num > 0:
                string_num += '0' + str(num)
            else:
                string_num += str(num)
        # set max to current character if it is the max
        if int(string_num) > k:
            k = int(string_num)        
        inlist_num.append(string_num)

    # intialize empty count and output arrays
    size = len(inlist)
    output = [0] * size
    count = [0] * (k + 1)
    
    # in the count array, count the amount of each item from the numbers array
    for x in range(0, size):
        count[int(inlist_num[x])] += 1


    # reset values in count to match actual positional (index) values 
    # starts at 1 to prevent negative indexing
    for x in range(1, len(count)):
        count[x] += count[x - 1]
        
    # find index of each member in original array and place values into output array
    i = size - 1
    while i >= 0:
        output[count[int(inlist_num[i])] - 1] = inlist[i]
        count[int(inlist_num[i])] -= 1
        i -= 1
    
    # copy the sorted items back into the original array
    for i in range(0, size):
        inlist[i] = output[i]
        
    return inlist
