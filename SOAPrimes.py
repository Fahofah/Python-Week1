import math 
from datetime import datetime

limit =20000000

sieveSet=[1,7,11,13,17,19,23,29,31,37,41,43,47,49,53,59]
sSubSet1=[1,13,17,29,37,41,49,53]
sSubSet2=[7,19,31,43]
sSubSet3=[11,23,47,59]
is_prime=[False] * (limit+1)
primeList=[2,3]
startTime = datetime.now()
for x in range(1,int(math.sqrt(limit))+1):
    for y in range(1,int(math.sqrt(limit))+1):
        n=4*x**2+y**2
        if(n<= limit and (n%60 in sSubSet1)):
            is_prime[n]= not is_prime[n]
        n=3*x**2+y**2
        if(n<= limit and (n%60 in sSubSet2)):
            is_prime[n]=not is_prime[n]
        n=3*x**2-y**2
        if(n<= limit and (n%60 in sSubSet3)):
            is_prime[n]= not is_prime[n]

for n in range(5,int(math.sqrt(limit))):
    if is_prime[n]:
        for k in range(n**2,limit+1,n**2):
            is_prime[k]=False

for n in range(5,limit+1):
    if is_prime[n]:
        primeList.append(n)
calTime =datetime.now() - startTime  

# for i in primeList:
#     print(i)

print(calTime)



