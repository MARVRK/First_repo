#function to get fibonacci number via suing cache
def caching_fibonacci():
    cache={}
    #recurcive inner function, to calculate fibonacci number.
    def fibonacci(n):
        if n <=0:
            return 0
        elif n == 1:
            return 1
        elif n in cache :
            return cache[n]
        cache[n] = fibonacci(n-1)+fibonacci(n-2)
        return cache[n]
    
    return fibonacci

#Summone function fibonaci
cashed_fibonacci=caching_fibonacci()   
#get results from the fibonacci function.
print(cashed_fibonacci(10))#result 55
print(cashed_fibonacci(15))#result 610



