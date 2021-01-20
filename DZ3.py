def my_func(var_1, var_2, var_3):
    a = [var_1, var_2, var_3]
    a.sort(reverse=True)
    print(a[0] + a[1])

my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: ')))
