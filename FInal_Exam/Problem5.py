def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    N = len(map_from)
    key_code = {}
    decoded = ""
    
    # Get dictionary key_code
    for index in range(N):
        key_code[map_from[index]] = map_to[index]
    #Decode code according to the key_code
    for letter in code :
        decoded += key_code[letter]
    
    return (key_code, decoded)
  


#Test 1 :
(map_from, map_to, code) = ("abcd", "dcba", "dab")
print("Test 1 result is : ",cipher(map_from, map_to, code))
if cipher(map_from, map_to, code) == ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc') :
    test1 = "Test 1 passed"
else :
    test1 = "Test 1 failed"
    
#Test 2 :
(map_from, map_to, code) = ("a", "d", "a")
print("Test 2 result is : ", cipher(map_from, map_to, code))
if cipher(map_from, map_to, code) == ({'a':'d'}, "d") :
    test2 = "Test 2 passed"
else :
    test2 = "Test 2 failed"
    

    

    
print(test1)
print(test2)
  
        

            
            
                