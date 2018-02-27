"""
Date : 26/02/2018 
Program COntext : 6.00.1 EDX course
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # trans is a Python dictionary that captures the numbers between 0 and 10
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    n = int(us_num)
    
    if n >= 0 and n < 11:
        return trans[us_num]
    elif n > 10 and n < 20 :
        return "shi " + trans[us_num[1]]
    elif n > 19 and n < 100 :
        if us_num[1] == "0" :
            return trans[us_num[0]] + " shi"
        else :
            return trans[us_num[0]] + " shi " + trans[us_num[1]]



"""
Tests 
"""

#Test 1 :
us_num = "0"
if convert_to_mandarin(us_num) == "ling" :
    test1 = "Test 1 passed"
else :
    test1 = "Test 1 failed"
    
#Test 2 :
us_num = "11"
if convert_to_mandarin(us_num) == "shi yi" :
    test2 = "Test 2 passed"
else :
    test2 = "Test 2 failed"
    
#Test 3 :
us_num = "10"
if convert_to_mandarin(us_num) == "shi" :
    test3 = "Test 3 passed"
else :
    test3 = "Test 3 failed"
    
#Test 4 :
us_num = "19"
if convert_to_mandarin(us_num) == "shi jiu" :
    test4 = "Test 4 passed"
else :
    test4 = "Test 4 failed"
    
#Test 5 :
us_num = "20"
if convert_to_mandarin(us_num) == "er shi" :
    test5 = "Test 5 passed"
else :
    test5 = "Test 5 failed"

#Test 6 :
us_num = "99"
if convert_to_mandarin(us_num) == "jiu shi jiu" :
    test6 = "Test 6 passed"
else :
    test6 = "Test 6 failed"
    
print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print(test6)

#All tests done - 10/10 full MARK
