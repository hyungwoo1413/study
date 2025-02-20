
'''
# 연습문제 2번
def addNumber(num):
    if num <= 10:
        return 0
    return num + addNumber(num-1)

print(addNumber(100))
'''

'''
# 연습문제 3번
def factorial(num):
    if num < 1:
        return 1
    retVal = factorial(num-1)
    return retVal * num

print(factorial(4))
'''

'''
# 연습문제 4번
def printStar(n):
    if n > 0:
        print('*'*n)
        printStar(n-1)

printStar(5)
'''


# 연습문제 5번
import random

def arySum(arr,n):
    if n <= 0:
        return arr[0]
    return #

ary = [random.randint(1,1000) for _ in range(random.randint(10,20))]
print(ary)
print('배열합게 -->', arySum(ary, len(ary)-1))