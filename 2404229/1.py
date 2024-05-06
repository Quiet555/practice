def factorial(n):
    for x in range(1,n+1):
        result=1
        for i in range(1,x+1):
            result=result*i
        print(f'{x:2}! = {result}')
print(factorial(25))