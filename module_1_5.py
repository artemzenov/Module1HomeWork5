immutable_var = 'abc', 1, ['a', 2], True
print('Кортеж:', immutable_var)
#immutable_var[1] = 10 #кортеж не поддерживает обращение по элементам
print()
mutable_list = ['abc', 1, ['a', 2], True]
print('Первоначальный список:', mutable_list)
mutable_list.insert(0, 'text')
mutable_list.append(15)
mutable_list.pop(1)
print('Измененный список', mutable_list)
