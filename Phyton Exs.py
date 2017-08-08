#Task1
print('#Task1')
print('Hello World!')
#Task2
print('#Task2')
hi='Hello World'
print(hi)
#Task3
print('#Task3')
def printThis(text):
    print(text)
printThis('Hello Mama')
#Task4
print('#Task4')
def add(x,y):
    print(x+y)
add(4,5)
#Task5
print('#Task5')
def sumORmult(x,y,sumIt):
    if (sumIt):
        result=x+y
    else:
        result=x*y
    print(result)
sumORmult(2,3,False)
#Task6
print('#Task6')
def sumORmult2(x,y,sumIt):
    if (x==0):
        result=y
    elif (y==0):
        result=x
    else:
        if (sumIt):
            result=x+y
        else:
            result=x*y
    print(result)
sumORmult2(0,7,True)
#Task7
print('#Task7')
for x in range(0,10):
    sumORmult2(x,3,True)
#Task8
print('#Task8')
numList= [6,2,7,4,3,6,7,8,9,10]
for x in range(0,10):
    sumORmult2(numList[x],numList[-(x+1)],True) 
#Task9  
print('#Task9')
for x in numList:
    print(x)
#Task10
print('#Task10')
nums=[None]*10
for x in range(0,10):
    nums[x]=x
    print(x)
for x in nums:
    print(x*10)
#Task11
print('#Task11')
size=int(input('How many numbers you want to enter?'))
numSet=[None]*size
print('OK, now please enter the first number')
for x in range(0,size):
    numSet[x]=int(input())
    print('Now please enter number %d' %(x+2))
for x in numSet:
    print(x)
for x in numSet:
    print(x*10)
#Task12
print('#Task12')
from functools import partial
def mult(x,y):
    return x*y
num=int(input('Enter a number:'))
double = partial(mult,2)
triple = partial(mult,3)

print("Double is", str(double(num)) ,"and triple is " ,str(triple(num)))
#Task13
print('#Task13')
def blackjack(x,y):
    if(x<0 or y<0):
        print('Invalid cards')
    else:
        if(x>21 and y>21):
            return 0
        elif(x>21 and y<22):
            print('was here')
            return y
        elif(y>21 and x<22):
            return x
        else:
            if(x>y):
                return x
            elif(y>x):
                return y
            elif(x==y):
                print('Tie')
    
print(blackjack(23,23))
#Task14
print('#Task14')
def uniqSum(x,y,z):
    if(x==y==z):
        return 0
    elif(x==y):
        return y+z
    elif(y==z):
        return x+y
    elif(x==z):
        return x+y
    else:
        return x+y+z
print(uniqSum(2,2,1))
#Task15
print('#Task15')
def tooHot(temp,isSummer):
    upLim=90
    if(isSummer):
        upLim=100
    if(temp>=60 and temp<=upLim):
        return True
    else: 
        return False
print(tooHot(95,True))
#Task16
print('#Task16')
def isLeap(year):
    if(year%4==0):
        return True
    else:
        return False
print(isLeap(2001))






