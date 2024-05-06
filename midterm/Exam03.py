def inputa():
    a=input('輸入一串正整數，且每個正整數用!做分割:')
    lsta=a.split('!')
    for i in range(len(lsta)):
        lsta[i]=float(lsta[i])

    return lsta    

x=inputa()
for i in range(len(x)):
    result=101.325*(1-2.25577*10**-5*x[i])**5.2559
    print(result)
