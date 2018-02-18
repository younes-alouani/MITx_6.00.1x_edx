def general_poly(L):
    
    """L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    def g(x) :
        total = 0    
        if L == [] :
            return 0
        else :
            for index in range(0,len(L)):
                total += L[index]*(x**(len(L)-1-index))
            return total
    
    return g
    
    
    
    
