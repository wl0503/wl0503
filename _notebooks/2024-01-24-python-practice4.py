def Fizzbuzz (arr):
    for i in range(len(arr)):
        if arr[i] % 3 == 0:
            arr[i] = "Fizz"
        elif arr[i] % 5 == 0:
            arr[i] = "Buzz"
        elif arr[i] % 5 == 0 and arr[i] % 3 == 0:
            arr[i] = "Fizzbuzz"
    return arr
arr = [1,2,3,5,15,3,15]
print(Fizzbuzz(arr))
            
    ## n = length of arr, can be anything
    ## arr[i] divisible by 3 and 5, fizzbuzz
    ## arr[i] divisible by 3, fizz
    ## arr[i] divisibel by 5, buzz
    ## for i in n 
    ## input = 3
        