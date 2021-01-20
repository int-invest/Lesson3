def arithmetic(var_1, var_2):
    print(var_1 / var_2)
try:
    arithmetic(int(input('Введите первое число: ')), int(input('Введите второе число: ')))

except ZeroDivisionError:
        print('Введен 0!')
except ValueError:
        print('Вы ввели не число!')
