while 1:
    text = input('takes 1 argument like "111 201">>>')

    num1, num2 = [float(i) for i in text.split()]
    print(num1, num2)
    num1_master = num1
    num2_master = num2


    if num1 == num2:
        print(f'{num1}, {num2} = {num1}')
        continue
    elif num1 < num2:
        num1, num2 = num2, num1

    div = num1 // num2
    mod = num1 % num2
    print(f'{num1} = {num2}*{div} + {mod}')


    num1 = num2
    num2 = mod

    while mod != 0:
        div = num1 // num2
        mod = num1 % num2
        print(f'{num1} = {num2}*{div} + {mod}')
        num1 = num2
        num2 = mod

    print(f'NWD({num1_master, num2_master}) = {num1}')