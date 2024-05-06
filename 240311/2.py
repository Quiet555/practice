def temp():
    cel = int(input('請輸入攝氏溫度:'))
    fah = round(((9/5)*cel)+32,2)
    print(f'約等於華氏 {fah} 度。')
def BMI():
    hig = int(input('請輸入身高(cm):')) / 100
    weg = int(input('請輸入體重(kg):'))
    bmi = round(weg / hig**2,1)
    print('BMI = ',bmi)

flag = input('1)攝氏到華氏的溫度轉換\n2)計算 BMI\n你的選擇是:')
match flag:
    case '1':
        temp()
    case '2':
        BMI()