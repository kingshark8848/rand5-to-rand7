import random

rand5_count = 0

def rand5():
    global rand5_count
    rand5_count += 1
    return random.randint(1,5)

def rand2():
    result = None
    while (not result) or result>4:
        result = rand5()
    
    if result%2 == 0:
        return 2
    else:
        return 1

def rand10():
    base = 0 if rand2()==1 else 5
    return base + rand5()

def rand7():
    result = None
    while (not result) or result>7:
        result = rand10()
    
    return result


def simulate(count):
    global rand5_count

    resultDic = {}
    for i in range(count):
        r = rand7()
        resultDic[r] =  resultDic[r]+1 if r in resultDic else 1
    
    for r in resultDic:
        print(r, resultDic[r], str(round(resultDic[r]/count*100,4))+"%")
    
    print("avg calls of rand5: ", rand5_count/count)

if __name__ == '__main__':
    simulate(100000)
