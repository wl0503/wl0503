## two lists
    ## ans 2n, the twice length of nums
    ## num n, 
    ## ans[i] == num[i]
    ## ans[i+n] == nums[i]
## 0 <= i < n (0-indexed).
## ans is the concatenation of two nums arrays.
## return the array ans

def ansnums (ans, nums):
    n = len(nums)
    while n + n == len(ans):
        for i in range(n):
            if nums[i] == ans[i] == ans[i+n] and ans == nums + nums:
                return ans
    return False

ans = [1,2,3,1,1,2,3,1]
nums = [1,2,3,1]

print(ansnums(ans, nums))