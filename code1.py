import random

rand5_count = 0

def rand5():
    global rand5_count
    rand5_count += 1
    return random.randint(1,5)

def rand7():
    while True:

        # do our die rolls
        roll1 = rand5()
        roll2 = rand5()

        outcome_number = (roll1-1) * 5 + (roll2-1) + 1

        # if we hit an extraneous
        # outcome we just re-roll
        if outcome_number > 21:
            continue

        # our outcome was fine. return it!
        return outcome_number % 7 + 1

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