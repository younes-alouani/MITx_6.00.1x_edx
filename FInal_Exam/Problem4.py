"""
Date : 26/02/2018 
Program COntext : 6.00.1 EDX course
"""

def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    
    ####
    """
    Private function that returns :
        True if a number is Prime
        False if not
    """
    def isPrime(number) :
        import math    
        if number == 0 or number == 1 :
            return False
        elif number == 2 :
            return True
        else :
            maxDenom = int(math.sqrt(number))
            for denom in range(2,maxDenom+1):
                if number % denom == 0 :
                    return False
        return True
    #####
    
    primesList = []
    for n in range(N+1) :
        if isPrime(n) :
            primesList += [n]
    return primesList
        



"""
Tests 
"""

#Test 1 :
N = 0
print("Test 1 result is : ",primes_list(N))
if primes_list(N) == [] :
    test1 = "Test 1 passed"
else :
    test1 = "Test 1 failed"
    
#Test 2 :
N = 3
print("Test 2 result is : ", primes_list(N))
if primes_list(N) == [2,3] :
    test2 = "Test 2 passed"
else :
    test2 = "Test 2 failed"
    
#Test 3 :
N = 11
print("Test 3 result is : ", primes_list(N))
if primes_list(N) == [2,3,5,7,11] :
    test3 = "Test 3 passed"
else :
    test3 = "Test 3 failed"
    

    
print(test1)
print(test2)
print(test3)


#All tests done - 10/10 full MARK
