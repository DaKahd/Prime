import math
from time import *
knownPrimes = []
def isPrime(num: int)->bool:
    for x in knownPrimes:
        if x>math.sqrt(num):
            break
        if num%x == 0:
            return False
    knownPrimes.append(num)
    return True

def search(numPrimes: int = 100, interval = 1):
    startTime = time()
    counter = 2
    numFound = 0
    while True:
        if numFound == numPrimes:
            break
        if isPrime(counter):
            numFound+=1
            if numFound%interval==0:
                print(f"prime number {numFound} is {counter}")
        counter+=1
    print(f"Took {time()-startTime} seconds for an average of {(time()-startTime)*10000000/numPrimes} microseconds per prime ")
    return knownPrimes

search(1000000, interval = 100000)