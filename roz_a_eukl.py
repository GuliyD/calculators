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
    temp = []
    print(f'{num1} = {num2}*{div} + {mod}')
    temp.append([str(num1), f'{num2}*{div}', str(mod)])


    num1 = num2
    num2 = mod

    while mod != 0:
        div = num1 // num2
        mod = num1 % num2
        print(f'{num1} = {num2}*{div} + {mod}')
        temp.append([str(num1), f'{num2}*{div}', str(mod)])
        num1 = num2
        num2 = mod

    temp.reverse()
    print(f'NWD({num1_master, num2_master}) = {num1}')
    print(temp)
    del temp[0]
    temp2 = []
    for i in range(len(temp)):
        '''An implementation of extended Euclidean algorithm.
        Returns integer x, y and gcd(a, b) for Bezout equation:
            ax + by = gcd(a, b).
        '''
        print(f'{temp[i][2]} = {temp[i][0]} - {temp[i][1]}')
    print('дальше сам')