import time

def palindrome_create():
    nums=('9','8','7','6','5','4','3','2','1','0') # we create a list of the strings we will use
    iterations = 0 # we bring along our trusty iterator
    
    for dig1 in range(10):
        for dig2 in range(10):
            for dig3 in range(10):
                #we create the palindrome string by slicing using the iterators
                pal_str = nums[dig1] + nums[dig2] + nums[dig3] + nums[dig3] + nums[dig2] +nums[dig1]  
                palindrome = int(pal_str) # typecast string into an integer
                # print(pal_str, palindrome) #debug to check palindromes tested
                
                #lowest number to check against that can generate a higher 
                low_val = int(palindrome/999) # or //999 floor div gives int as answer 
                # highest possible factor to check, one factor must be lower than this
                high_val = int(palindrome**0.5) + 1 # **0.5 is "the square root" of palindrome 
                
                # check if palindrome divisible by any of the numbers between min and max
                for digit in range(low_val,high_val):
                    iterations += 1
                    if palindrome % digit == 0: #check for divisibility, since we are stepping through palindromes in order, as soon as we find one: we are Done! 
                       
                        return 'palindrome:', palindrome, 'digit:',digit, 'palindrome/digit:', palindrome/digit ,'iterations:',iterations #gives nicer close out of loops

def palindrome_create2():
    
    iterations = 0 # our trusty iterator
    
    for dig1 in range(9,0,-1):
        for dig2 in range(9,-1,-1):
            for dig3 in range(9,-1,-1):
                # we create the -palindromes by adding the 'placevalues', 
                # example step 999999 -> 998899 -> 997799 etc but only to 100001 
                palindrome = dig1*100000 + dig2*10000 + dig3*1000 + dig3*100 + dig2*10 + dig1
                #print(palindrome) #debug
                
                low_val = int(palindrome/999) # or low_val = palindrome//999 
                high_val = int(palindrome**0.5)+1
                for digit in range(low_val,high_val):
                    iterations += 1
                    if palindrome % digit == 0:
                        
                        return 'palindrome:',palindrome, 'digit:',digit, 'palindrome/digit:', palindrome/digit ,'iterations:',iterations

#palindrome()
#palindrome_back()
for func in ['palindrome_create','palindrome_create2']:
    runs = 10 
    start = time.time()
    for run in range(runs):
        #print(locals()[func])
        return_value = locals()[func]()
        end =time.time()
    print(return_value, 'Average run-time:', (end-start)/runs)
    