# -*- coding: utf-8 -*-
import sys

list_stair = [1, 1, 1]
def recursion(current_stair):
    if len(list_stair) <= current_stair:
        for x in range(current_stair-2):
            list_stair.append(0)
    if current_stair<0: return 0
    elif current_stair<3: return 1
    else:
        five_stair = list_stair[current_stair-5] if list_stair[current_stair-5]!=0 else recursion(current_stair-5)
        three_stair = list_stair[current_stair-3] if list_stair[current_stair-3]!=0 else recursion(current_stair-3)
        one_stair = list_stair[current_stair-1] if list_stair[current_stair-1]!=0 else recursion(current_stair-1)
        list_stair[current_stair]=five_stair+three_stair+one_stair
        return list_stair[current_stair]

if __name__ == '__main__':
    stairs = int(sys.argv[1])
    answer = recursion(stairs)
    print answer
