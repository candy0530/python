# encoding: utf-8
import string
import sys

def checkXMLFormate(inputString):
    inputString = string.replace(inputString, '<a>', 'S')
    inputString = string.replace(inputString, '</a>', 'E')
    amountOfStart = 0
    for x in range(len(inputString)):
        popOutString = inputString[x]
        if popOutString == 'S':
            amountOfStart+=1
        elif popOutString == 'E':
            if amountOfStart>0:
                amountOfStart-=1
            else:
                return False
        else:
            return False
    if amountOfStart==0:
        return True
    else:
        return False

if __name__ == '__main__':
    inputString = sys.argv[1]
    print checkXMLFormate(inputString)
