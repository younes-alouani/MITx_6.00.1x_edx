import math
def genPrimes():
    start = 4
    yield 2
    yield 3
    while True :
        next = start
        isPrime = True
        for denom in range(2, int(math.sqrt(next)+1)) :
            if next % denom == 0 :
                isPrime = isPrime and False
        if isPrime == True :
            yield next
        start = next + 1