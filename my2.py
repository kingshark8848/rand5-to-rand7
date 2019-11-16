import random

rand5_count = 0

# that is the known function
def rand5():
    global rand5_count
    rand5_count += 1
    return random.randint(1,5)


def rand4():
    result = None
    while (not result) or result>4:
        result = rand5()
    
    return result


def rand8():
    base = 0 if rand4()%2==0 else 4 # determin 1-4 or 5-8
    return base + rand4()


def rand7():
    result = None
    while (not result) or result>7:
        result = rand8()
    
    return result


def simulate(rollTimes):
    global rand5_count

    resultDic = {}
    for i in range(rollTimes):
        r = rand7()
        resultDic[r] =  resultDic[r]+1 if r in resultDic else 1
    
    for r in resultDic:
        print(r, resultDic[r], str(round(resultDic[r]/rollTimes*100,4))+"%")
    
    print("avg calls of rand5: ", rand5_count/rollTimes)

if __name__ == '__main__':
    simulate(100000)
