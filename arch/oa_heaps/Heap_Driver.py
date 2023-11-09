'''
Created on Mar 13, 2022

@author: Jennifer Becker
'''

from Heap import MinHeap


def main():
    # pass input file to readfile function
    readFile('1')
    readFile('2')
    readFile('3')
    readFile('4')
    #readFile('Example_input', 11, 7)


def readFile(filenum):
    # set infile and outfile paths
    infile = f'in{filenum}.txt'
    outfile = f'out{filenum}.txt'

    # read infile and convert to list
    f = open(infile, 'r')
    txt = f.read()
    f.close()
    indata = txt.split('\n')
    indata = ' '.join(indata).split(' ')

    # remove empty strings left behind by whitespace in original string
    while '' in indata:
        indata.remove('')

    # convert list to numeric and pass to heap testing function
    numbers = [int(x) for x in indata]

    global fout
    fout = open(outfile, 'w')
    testData(numbers)
    fout.close()


def testData(indata):
    # initialize heap
    hp = MinHeap()

    # insert data into heap while verifying that is a min heap on each insert
    for x in indata:
        MinHeap.insert(hp, x)
        checkHeap(hp)

    # print heap contents
    #fout.write('Heap\n')
    printHeap('Heap', hp)

    # insert 31
    insertOne(hp, 31)

    # insert 14
    insertOne(hp, 14)

    # delete all data
    size = MinHeap.size(hp)
    for x in range(0, size):
        deleteOne(hp)


def areHeapElementsOrdered(hp, parentIndex, childIndex):
    # considers heap contents ordered if parent is less than child or if child or parent index is empty
    return parentIndex >= MinHeap.size(hp) or childIndex >= MinHeap.size(hp) or MinHeap.getElement(hp, parentIndex) <= MinHeap.getElement(hp, childIndex)


def checkHeap(hp):
    for parentIndex in range(0, MinHeap.size(hp)):
        # raise error if heap is out of order
        if not (areHeapElementsOrdered(hp, parentIndex, (2*parentIndex)+1) and areHeapElementsOrdered(hp, parentIndex, (2*parentIndex)+2)):
            printHeap('Corrputed', hp)
            wr = f'Error: heap violation at index {parentIndex}' \
                 f', heap[{parentIndex}] = {MinHeap.getElement(hp, parentIndex)}' \
                 f', heap[{(2*parentIndex)+1}] = {MinHeap.getElement(hp, (2*parentIndex)+1)}' \
                 f', heap [{(2*parentIndex)+2}] = {MinHeap.getElement(hp, (2*parentIndex)+2)}\n'
            fout.write(wr)
            fout.close()
            raise RuntimeError('Not a heap')


def printHeap(description, hp):
    # write [heap size] and contents to outfile
    fout.write(f'{description}\n')
    wr = f'[{MinHeap.size(hp)}] '
    fout.write(wr)
    for x in range(0, MinHeap.size(hp)):
        wr = f'{MinHeap.getElement(hp, x)} '
        fout.write(wr)
    fout.write('\n\n')


def insertOne(hp, value):
    # write inserted value to outfile
    wr = f'Insert {value}\n'
    fout.write(wr)
    # insert value into heap and verify heap
    MinHeap.insert(hp, value)
    checkHeap(hp)
    # print heap contents
    printHeap(f'Heap after insert {value}', hp)


def deleteOne(hp):
    # write minimum to outfile
    min = MinHeap.getElement(hp, 0)
    wr = f'Delete {min}\n'
    fout.write(wr)
    # insert minimum from heap and verify heap
    MinHeap.deleteMin(hp)
    checkHeap(hp)
    # print heap contents
    printHeap(f'Heap after Delete {min}', hp)
    # if heap


if __name__ == '__main__':
    main()
