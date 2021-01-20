'''Задача 6 '''
ord_a = ord('a')
ord_z = ord('z')
ord_sp = ord(' ')
def int_func(var_1):
    for el in var_1:
        org_el = ord(el)
        if org_el > ord_z or org_el < ord_a:
            return ''
    return var_1.title()
var_1 = input('Введите слово маленькими латинскими буквами\n')
print(int_func(var_1))



'''Задача 7 '''
def str_func(var_1):
    list_var = var_1.split(' ')
    result = []
    for el in list_var:
        el_t = int_func(el)
        if len(el_t) == 0:
            return  False
        result.append(el_t)
    print(' '.join(result))

    return True

while True:
    var_1 = input('Введите слова маленькими латинскими буквами разделенные пробелом\n')
    if not str_func(var_1):
        break

print(str_func(var_1))
