from datetime import datetime
import math



class PrimeNumber():

    def __init__(self):
        self.primeList=[]
        self.calTime=-1

    def prime3mil(self):
        startTime = datetime.now()
        for x in range(1,3000001,2):
            if ( x >1 ):
                isnotprime=0
                for p in range(3,math.ceil(math.sqrt(x))+1,2):
                    if( x % p == 0):
                        isnotprime += 1
                if(isnotprime==0):
                    self.primeList.append(x)
                if(x%1000001==1 or x%1000001==0):
                    print('million checkpoint, ', x)
        self.primeList=[2]+self.primeList
        self.calTime =datetime.now() - startTime            
    
    def printPrimes(self):
        for i in range(100):
            print(self.primeList[i])

primer = PrimeNumber()

primer.prime3mil()
primer.printPrimes()
print('\n', primer.calTime)