'''
Created on Mar 6, 2022

@author: Jennifer Becker

driver functions for using open address hash table classes.
exports text files with collisions for each input key and hash table format.
function readFile() takes txt input file (without extension), int table size and int double factor

'''

from hashtable import LinearHashTable, QuadraticHashTable, DoubleHashTable

def main():
    # pass input file to readfile function. must be txt file without file extension.
    readFile('numbers', 11, 7)

def readFile(file, tableSize, doubleFactor):
    # set infile and outfile paths
    infile = f'{file}.txt'
    outfile1 = f'{file}_out_collisions.txt'
    outfile2 = f'{file}_out_probing.txt'
    
    # read infile and convert to list
    f = open(infile, 'r')
    txt = f.read()
    f.close()
    lines = txt.split('\n')
    nums = ' '.join(lines).split(' ')
    
    # remove empty strings left behind by whitespace in original string
    while '' in nums:
        nums.remove('')
        
    # convert to int
    nums = list(map(int, nums))
    
    # open collisions outfile and write header
    f1 = open(outfile1, 'w')
    f1.write('Format of output \nkey: value -> retrievedValue, collisions number Collisions \n\nLinear total number Collisions \nQuadratic total number Collisions \nDouble hashing total number Collisions\n\n')

    # pass to hash table driver function
    lph, qph, dph = sendToHash(nums, tableSize, doubleFactor, f1)
    f1.close()

    # print linear probing hash table contents to probing outfile
    f2 = open(outfile2, 'w')
    f2.write(f'*** Linear Probing Random Order Start *** \n\nprint table.size() = {tableSize}\n')
    for i in (range(0, tableSize)):
        keyval = LinearHashTable.get(lph, i)

        if keyval != None:
            key = keyval[0]
            val = keyval[1]
            f2.write(f'index = {i} key = {key} value = {val}\n')
    f2.write(f'\n*** Linear Probing Random Order End *** \n\n')

    # print quadratic probing hash table contents to probing outfile
    f2.write(f'*** Quadratic Probing Random Order Start *** \n\nprint table.size() = {tableSize}\n')
    for i in (range(0, tableSize)):
        keyval = QuadraticHashTable.get(qph, i)

        if keyval != None:
            key = keyval[0]
            val = keyval[1]
            f2.write(f'index = {i} key = {key} value = {val}\n')
    f2.write(f'\n*** Quadratic Probing Random Order End *** \n\n')

    # print double hash probing hash table contents to probing outfile
    f2.write(f'*** Double Hashing Probing Random Order Start *** \n\nprint table.size() = {tableSize}\n')
    for i in (range(0, tableSize)):
        keyval = DoubleHashTable.get(dph, i)

        if keyval != None:
            key = keyval[0]
            val = keyval[1]
            f2.write(f'index = {i} key = {key} value = {val}\n')
    
    f2.write(f'\n*** Double Hashing Probing Random Order End *** \n\n')
    f2.close()
    
    print('Done!')



def sendToHash(nums, tableSize, doubleFactor, f1):
    
    # write order
    f1.write(f'*** Random Order Start ***\n\n')
        
    # initialize hash table class objects
    lph = LinearHashTable(tableSize)
    qph = QuadraticHashTable(tableSize)
    dph = DoubleHashTable(tableSize, doubleFactor)
    
    # insert numbers into each hash table class object, pull them out and write to output file
    for key in nums:
        value = key * 2

        # *** Linear Probing ***
        previousCollisions = LinearHashTable.getCollisions(lph)        
        LinearHashTable.put(lph, key, value)
        retrievedValue = LinearHashTable.getValue(lph, key)
        collisions = LinearHashTable.getCollisions(lph) - previousCollisions  
        f1.write(f'{key} : {value} -> {retrievedValue}, collisions {collisions} \n')

        # raise exception if value != key * 2
        if value != retrievedValue:
            raise ValueError('incorrect value!')
 
        # *** Quadratic Probing ***
        previousCollisions = QuadraticHashTable.getCollisions(qph)        
        QuadraticHashTable.put(qph, key, value)
        retrievedValue = QuadraticHashTable.getValue(qph, key)
        collisions = QuadraticHashTable.getCollisions(qph) - previousCollisions
        f1.write(f'{key} : {value} -> {retrievedValue}, collisions {collisions} \n')

        # raise exception if value != key * 2
        if value != retrievedValue:
            raise ValueError('incorrect value!')

        # *** Double Hash Probing *** 
        previousCollisions = DoubleHashTable.getCollisions(dph)        
        DoubleHashTable.put(dph, key, value)
        retrievedValue = DoubleHashTable.getValue(dph, key)
        collisions = DoubleHashTable.getCollisions(dph) - previousCollisions
        f1.write(f'{key} : {value} -> {retrievedValue}, collisions {collisions} \n\n')

        # raise exception if value != key * 2
        if value != retrievedValue:
            raise ValueError('incorrect value!')

    collisions = LinearHashTable.getCollisions(lph)        
    f1.write(f'Linear: {collisions} \n')
    collisions = QuadraticHashTable.getCollisions(qph)        
    f1.write(f'Quadratic: {collisions} \n')
    collisions = DoubleHashTable.getCollisions(dph)        
    f1.write(f'Double Hash: {collisions} \n\n')

    f1.write(f'*** Random Order End ***\n\n')
    
    return lph, qph, dph
    

if __name__ == '__main__':
    main()