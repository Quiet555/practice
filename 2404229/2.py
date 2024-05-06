def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
num=int(input('輸入一個值:'))
for i in range(num):
    if i == num-1:
        print(fib(i),end='')
    else:
        print(fib(i),end=',')
