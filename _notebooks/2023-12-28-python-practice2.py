
## Palindrom ex: Level, Mom, Kayak. 
## feature: same forward and backward string
## as a code representation for the feature: str[:len(str)] == str[len(str):1]
## level, mom, adda. for level, level[0]=level[len(level)-1], level[1]=level[3], level[2]
## deified
## adda, adddda
## 

def Palindrome (num):
    if num == num[::-1]:
        return True
    else:
        return False
##print(Palindrome("level"))

def Palindrome (num):
    num = num.lower()
    for i in range(len(num)//2):
        if num[i] != num[len(num)-i-1]:
            return False
    return True
        
print(Palindrome("David"))
