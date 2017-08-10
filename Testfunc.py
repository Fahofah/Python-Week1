import math
from datetime import datetime


is_prime = list()
limit = 300000000
is_prime = [False] * (limit + 1)
primeList=[2,3]

startTime = datetime.now()
for x in range(1,int(math.sqrt(limit))+1):
    for y in range(1,int(math.sqrt(limit))+1):
        n = 4*x**2 + y**2

        if n<=limit and (n%12==1 or n%12==5):
            # print "1st if"
            is_prime[n] = not is_prime[n]
        n = 3*x**2+y**2
        if n<= limit and n%12==7:
            # print "Second if"
            is_prime[n] = not is_prime[n]
        n = 3*x**2 - y**2
        if x>y and n<=limit and n%12==11:
            # print "third if"
            is_prime[n] = not is_prime[n]

for n in range(5,int(math.sqrt(limit))):
    if is_prime[n]:
        for k in range(n**2,limit+1,n**2):
            is_prime[k] = False

for n in range(5,limit):
    if is_prime[n]: primeList.append(n)

calTime =datetime.now() - startTime  

for i in range(20):
    print(primeList[i])

print(calTime)
