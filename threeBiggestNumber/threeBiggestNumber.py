# encoding: utf-8
import re
import sys

def fileChangeToNumberArray(fileName):
    numberPattern = re.compile('\d+')
    with open(inputFileName, 'r') as f:
        read_data = f.read()
    f.closed
    numberArray = re.findall(numberPattern, read_data)
    for x in range(len(numberArray)):
        numberArray[x] = (int)(numberArray[x])
    return numberArray

def sort(numberArray):
    biggestNumber=numberArray[0]
    smallestNumber=numberArray[0]
    for number in numberArray:
        if number > biggestNumber:
            biggestNumber=number
        elif number < smallestNumber:
            smallestNumber=number

    sortedNumber = []
    for x in range(smallestNumber, biggestNumber+1):
        if (x in numberArray):
            sortedNumber.append(x)
            
    return sortedNumber

def writeThreeBiggestNumberIntoFile(sortedArray, outputFileName='answer.dat'):
    f = open(outputFileName, 'w')
    f.write((str)(sortedArray.pop())+'\n')
    f.write((str)(sortedArray.pop())+'\n')
    f.write((str)(sortedArray.pop())+'\n')
    f.closed

if __name__ == '__main__':
    inputFileName = sys.argv[1]
    numberArray = fileChangeToNumberArray(inputFileName)
    print numberArray
    sortedNumber = sort(numberArray)
    print sortedNumber
    outputFileName = 'answer_'+inputFileName
    writeThreeBiggestNumberIntoFile(sortedNumber, outputFileName)
    with open(outputFileName, 'r') as f:
        for line in f:
            print line
    f.closed
    
