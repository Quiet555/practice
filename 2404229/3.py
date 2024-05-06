def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def show_fib(n):
    result=[]
    for i in range(n):
        result.append(fib(i))
    return result

while 1:
    num=int(input('請輸入要顯示幾項的 Fibonacci 數列:'))
    if num<=0:
        print('請重新輸入！')
        continue
    else:
        print(show_fib(num))
        break