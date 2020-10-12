def greet(name):
    print("Hello", name)
    print("Whats going on")
greet("Paul")
print("This is outside greet()")    


# function to check string is 
def isPalindrome(str):
  
    for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
s = "civic"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")
