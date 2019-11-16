# rand5-to-rand7
from rand5() to rand7()

## Problem

You have a method rand5() that generates a random integer from 1 to 5. 
Use it to write a method rand7() that generates a random integer from 1 to 7.

## Solution

### Best Solution (code1.py)

1. Create a rand25() via rand5().

Roll1 of rand5() to determine 5 base range. Result of roll1 and base range is:

1: 0*5 + roll2, 1-5
2: 1*5 + roll2, 6-10
3: 2*5 + roll2, 11-15
4: 3*5 + roll2, 16-20
5: 4*5 + roll2, 21-25

roll2 of rand5() to determin the function result. use formula above.

2. Create rand7() via rand25()

make a roll of rand25(). if result > 21 (because 21 is 7*3), roll again until result<=21.

use roll%7 to determin the final result. ( Actually it's rand21() to rand7() )

In Summary

rand5() -> rand25() -> rand21() -> rand7()

-----

Using the similar idea, there are other approaches.

### Solution 2 (my1.py)

1. rand5() -> rand2()
2. rand2() and rand5() -> rand10()
3. rand10() -> rand7()

### Solution 3 (my2.py)

1. rand5() -> rand4()
2. rand4() -> rand8()
3. rand8() -> rand7()

