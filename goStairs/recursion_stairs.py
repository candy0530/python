# -*- coding: utf-8 -*-
import sys

def recursion(current_stair):
    if current_stair<0: return 0
    elif current_stair<3: return 1
    else:
        return recursion(current_stair-5)+recursion(current_stair-3)+recursion(current_stair-1)

if __name__ == '__main__':
    stairs = int(sys.argv[1])
    answer = recursion(stairs)
    print answer
