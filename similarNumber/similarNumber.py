def similarNumbers(N):
    import math
    a = getNumber(N)
    zero_number = a['0'] if '0' in a else 0
    result = (sum(a.values())-zero_number)*math.factorial(sum(a.values())-1)
    for x in a.values():
        result /= math.factorial(x)
    return result

def getNumber(N):
    str_n = str(N)
    dict = {}
    for i in range(len(str_n)):
        if str_n[i] in dict:
            dict[str_n[i]]+=1
        else:
            dict[str_n[i]]=1
    return dict

if __name__=="__main__":
    import sys
    number = sys.argv[1]
    print similarNumbers(number)
