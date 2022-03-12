'''
Created on Mar 11, 2022

@author: Jennie

driver for counting sort algorithm that creates list of random input values,
passes to counting sort algorithm for sorting, and prints contents to terminal
with options for numeric or alphabetic counting sort

length: length of list
k: max value (for alphabetic, this is max number of characters)
type: 'num' or 'str'

'''

import random
import string

from countingsort import NumberCountingSort
from countingsort import StringCountingSort

def main():
    # pass type 
    CountingSortDriver('10', '25', 'num')
    CountingSortDriver('10', '4', 'str')
        

def CountingSortDriver(length, k, dtype):
    
    # convert length and max value to int if needed
    try:
        length = int(length)
        k = int(k)
    except:
        raise ValueError('input length and max value must be numbers. please update to number input and try again.')
    
    if dtype == 'num':
        # create random list of numbers and pass to number counting sort
        inlist = [random.randint(-k, k) for x in range(0, length)] 
        
        # print input contents to terminal
        print('%%%%% Number List Counting Sort %%%%%\n'
        f'Length: {length}\n'
        f'Max Numeric Bounds: {k}\n'
        f'Unsorted List: {inlist}')
                
        # sort list using counting sort
        NumberCountingSort(inlist)
                  
    elif dtype == 'str':
        # create random list of non-empty strings and pass to string counting sort
        inlist = [(
                ''.join(random.choice(string.ascii_letters) 
                for i in range(0, random.randint(1, k)))
            ) for x in range(0, length)]

        # print input contents to terminal
        print('%%%%% Number List Counting Sort %%%%%\n'
        f'Length: {length}\n'
        f'Max String Length: {k}\n'
        f'Unsorted List: {inlist}')

        # sort list using counting sort        
        StringCountingSort(inlist)
        
    else:
        raise ValueError('incorrect type input. please choose num or abc and try again.')
    

    print(f'Sorted List: {inlist}\n')

    return()

if __name__ == '__main__':
    main()
