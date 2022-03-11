'''
Created on Jan 30, 2022

@author: Jennifer Becker

This program reads any number of input files with a target value and sequence of values.
It will check the sequence for two numbers that sum to the target value or one number that
can be doubled to the target value.
'''

from heapsort import heapsort

def main():
    
    # pass each text file to sum of k function
    sumofk('in.txt')
        
def sumofk(infile):
    
    # read second and third lines of input file to target and sequence variables
    f = open(infile, 'r')
    txt = f.read()
    f.close()
    target = txt.split('\n')[1]
    sequence_orig = txt.split('\n')[2]
    sequence = sequence_orig.split(' ')
    
    # remove empty strings if present (created from whitespace at end of number list in1.txt, in4.txt, in5.txt)
    if '' in sequence:
        sequence.remove('')

    # convert target and sequence to int
    target = int(target)
    sequence = list(map(int, sequence))

    # pass sequence to heap sort for sorting
    sequence = heapsort(sequence)
  
    # initialize pointers 1 and 2 for starting off sum of K loop
    p1 = 0
    p2 = len(sequence) - 1
    
    # initialize sum of k boolean to false and begin loop
    # if a sum of k is found, loop breaks. if not, it breaks when p1 > p2
    sumofk_yn = False
    while p1 <= p2:
        # if values sum to target, return true and equation string
        if sequence[p1] + sequence[p2] == target:
            sumofk = f'{sequence[p1]} + {sequence[p2]} = {target}'
            sumofk_yn = True
            break

        elif sequence[p1] + sequence[p2] > target:
            p2 -= 1

        elif sequence[p1] + sequence[p2] < target:
            p1 += 1         
     
    # convert sequence back to string
    sequence = ' '.join(map(str,sequence))  
     
    # write target value to first line of output, sequence to second line of output
    f = open('out.txt', 'w')
    f.write(f'{target}\n{sequence_orig}\n{sequence}')

    #if boolean is true, write yes to third line and string to fourth line of output
    if sumofk_yn:
        f.write(f'\nYes\n{sumofk}')
    else:
        f.write('\nNo')

    f.close()
    return()


if __name__ == '__main__':
    main()
