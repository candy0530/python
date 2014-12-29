# -*- coding: utf-8 -*-
# 有一個樓梯，你每次只能爬 1 階、3 階，或 5 階。請寫一個 function，傳入樓梯總長為 N 階，回傳總共有多少種走法。
# 例如：樓梯總長為 5 階，走法有「1、1、1、1、1」、「5」、「1、3、1」、「1、1、3」、「3、1、1」，共 5 種

# 5*a + 3*b + 1*c = N

# N/5 ... o o/3 ... p 
# N/5-1 ... o+5 (o+5)/3 ... p

import sys

def get_five_stairs(stairs):
    five_stairs = stairs/5
    other_stairs = stairs - five_stairs*5
    return five_stairs, other_stairs

def get_three_stairs(stairs):
    three_stairs = stairs/3
    other_stairs = stairs - three_stairs*3
    return three_stairs, other_stairs

def get_matrix_of_possible(stairs):
    stairs_set = []
    count_stairs = stairs
    while(count_stairs>=0):
        five_stairs, other_stairs = get_five_stairs(count_stairs)
        other_stairs = other_stairs + stairs - count_stairs
        count_other_stairs = other_stairs
        while(count_other_stairs>=0):
            three_stairs, one_stair = get_three_stairs(count_other_stairs)
            one_stair = one_stair + other_stairs - count_other_stairs
            stairs_set.append((five_stairs, three_stairs, one_stair))
            count_other_stairs = count_other_stairs - 3
        count_stairs = count_stairs - 5
    return stairs_set

def get_combination(matrix):
    number = 0
    for x in range(len(matrix)):
        combination = matrix[x]
        all_element = combination[0] + combination[1] + combination[2]
        each_number = reduce(lambda x, y: x*y, range(1, all_element+1))
        if combination[0]>0:
            each_number = each_number/reduce(lambda x, y: x*y, range(1, combination[0]+1))
        if combination[1]>0:
            each_number = each_number/reduce(lambda x, y: x*y, range(1, combination[1]+1))
        if combination[2]>0:
            each_number = each_number/reduce(lambda x, y: x*y, range(1, combination[2]+1))
        number = number + each_number

    return number

if __name__ == '__main__':
    stairs = int(sys.argv[1])
    stairs_set = get_matrix_of_possible(stairs)
    print stairs_set
    answer = get_combination(stairs_set)
    print answer
