num=int(input('輸入放大倍數:'))
firstar=num+3

print('*'*firstar + ' ' + '*' *firstar + ' ' + ' '*1 + '*'*(firstar-2) + ' '*1 + ' '+' '*1+'*'*(firstar-1))

for i in range(num):
    print('*'+' '*firstar + '*'+' '*(firstar-2) +'*' + ' '+'*'+' '*(firstar-2) + '*'+' '+'*')

print('*'*(firstar-1)+' '*2+'*'*firstar+' '+'*'*firstar+' '+'*')

index=1
nindex=num+1
for i2 in range(num):
    print('*'+' '*firstar +'*'+' '*index+'*'+' '*nindex+'*'+' '*(firstar-2)+'*'+' '+'*')
    index+=1
    nindex-=1

print('*'*firstar +' ' + '*' + ' '*(num+1) + '*' + ' ' + '*' + ' '*(firstar-2) + '*' + ' '*2 + '*'*(firstar-1))
