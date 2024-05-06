nums=[0]*5
i=0
even,odd=0,0
evstr='偶數:'
odstr='奇數:'

while(i<5):
    nums[i]=int(input(f'整數{i+1}:'))
    numstr=str(nums[i])

    if nums[i]%2 == 0:
        even+=1
        evstr= evstr + numstr +' '    
    else :
        odd+=1
        odstr= odstr + numstr +' '
    i+=1

print(f'{even}個{evstr}')
print(f'{odd}個{odstr}')