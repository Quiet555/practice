lst= input('輸入一串數字:')
a=lst.split(',')
for i in range(len(a)):
        if a[i].find('.')==-1:
            a[i]=int(a[i])
        else:
            a[i]=float(a[i])
a.sort()
print(a)