def my_func(x, y):
    '''Первый способ через степень'''
    c = x ** y
    print('Результат:', c)

    '''Второй способ через функцию (pow)'''
    z = pow(x, y)
    print('Результат: ', z)

    '''Третий способ через цикл'''
    r = 1
    while (y < 0):
        r *= 1 / x
        y += 1
    print('Результат:', r)

my_func(int(input('Введите положительное число: ')), int(input('Введите отрицательное число: ')))


