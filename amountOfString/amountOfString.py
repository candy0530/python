# encoding: utf-8
import re
import sys

def fileChangeToStringArray(fileName):
    alphabetPattern = re.compile('[A-Z]+')
    with open(inputFileName, 'r') as f:
        read_data = f.read()
    f.closed
    return re.findall(alphabetPattern, read_data)

def changeToNumberAndSortArray(stringArray):
    alphabetDict = dict(A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8, I=9, J=10,
                       K=11, L=12, M=13, N=14, O=15, P=16, Q=17, R=18, S=19, T=20,
                       U=21, V=22, W=23, X=24, Y=25, Z=26)
    stringArray = [map(lambda y:alphabetDict.get(y), list(x)) for x in stringArray]
    return sorted(stringArray)

def getAmountOfString(stringArray):
    amountOfString = 0
    for index in range(len(stringArray)):
        amountOfString += reduce(lambda x, y: x+y, stringArray[index])*(index+1)
        stringArray[index] = reduce(lambda x, y: x+y, stringArray[index])
    print stringArray
    return amountOfString

if __name__ == '__main__':
    inputFileName = sys.argv[1]
    stringArray = fileChangeToStringArray(inputFileName)
    print stringArray
    stringArray = changeToNumberAndSortArray(stringArray)
    print stringArray
    print getAmountOfString(stringArray)
