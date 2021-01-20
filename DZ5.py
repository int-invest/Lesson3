def fun_sum():
    sum = 0
    num = False
    while num == False:
        numbers = input('Введите числа через пробел или нажмите "Q" для выхода: \n').split()
        count_sum = 0
        for i in range(len(numbers)):
            if(numbers[i] == 'Q' or numbers[i] == 'q'):
                num = True
                break
            else:
                count_sum = count_sum + int(numbers[i])
        sum = sum + count_sum
        print(f'Сумма чисел: {sum}')
    print(f'Итоговая сумма чисел: {sum}')


fun_sum()