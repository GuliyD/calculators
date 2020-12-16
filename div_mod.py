while 1:
    text = input('takes 1 argument like "-11 mod 3" or "-11 div 3">>>')

    num1, type1, num2 = text.split()
    num1 = float(num1)
    num2 = float(num2)

    div = num1 // num2
    mod = num1 % num2

    if div<0:
        print(f'{num1} = {num2}*({div}) + {mod}')
    else:
        print(f'{num1} = {num2}*{div} + {mod}')

    if type1 == 'mod':
        print(f'{num1} mod {num2} = {mod}')
    elif type1 == 'div':
        print(f'{num1} div {num2} = {div}')