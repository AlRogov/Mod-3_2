def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 'Строчечка', 3)
print_params(b=25)                       # Результат: 1 25 True
print_params(c=[1, 2, 3])                # Результат: 1 строка [1, 2, 3]


values_list = ["Москва", "Питер", "Владивосток"]
print_params(*values_list)

values_dict_ = {1: "a", 2: "b", 3: "c"}
print_params(*values_dict_)

values_list_2 = [1, '2']
print_params(*values_list_2, 42)      # Результат: 1 2 42
