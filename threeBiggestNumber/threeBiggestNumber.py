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

def findThreeBiggestNumber(numberArray):
    biggestNumber=numberArray[0]
    for number in numberArray:
        if number > biggestNumber:
            biggestNumber=number

    threeBiggestNumber = [biggestNumber]
    numberArray.remove(biggestNumber)

    index = biggestNumber
    while(len(threeBiggestNumber) < 3):
        if(index in numberArray):
            threeBiggestNumber.append(index)
            numberArray.remove(index)
        else:
            index-=1

    return threeBiggestNumber

def writeThreeBiggestNumberIntoFile(threeBiggestNumber, outputFileName='answer.dat'):
    f = open(outputFileName, 'w')
    threeBiggestNumber.reverse()
    f.write((str)(threeBiggestNumber.pop())+'\n')
    f.write((str)(threeBiggestNumber.pop())+'\n')
    f.write((str)(threeBiggestNumber.pop())+'\n')
    f.closed

if __name__ == '__main__':
    inputFileName = sys.argv[1]
    numberArray = fileChangeToNumberArray(inputFileName)
    outputFileName = 'answer_'+inputFileName
    threeBiggestNumber = findThreeBiggestNumber(numberArray)
    writeThreeBiggestNumberIntoFile(threeBiggestNumber, outputFileName)
    with open(outputFileName, 'r') as f:
        for line in f:
            print line
    f.closed

