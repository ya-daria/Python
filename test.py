print("Задание №1")
fname = input('Файл: ')
f = open(fname, 'w')
while True:
    s = input()
    if s == '': break
    f.write(s+'\n')
f.close()

print("Задание №2")
with open("text.txt") as f_obj:
    lines = 0
    for line in f_obj:
        if line.strip():
            lines += 1
            print(f'Строка №{lines}', len(line.split()))
    print(f'Всего {lines} не пустые строки.')

print("Задание №3")
with open('staff.txt') as f_obj:
    sum = 0
    lines = 0
    for line in f_obj:
        my_list = line.split()
        lines += 1
        if int(my_list[1]) < 20000:
            print(my_list[0])
        sum += int(my_list[1])
        sredn_dohod = sum/lines

print("Средний доход: ", '%.2f' % (sredn_dohod))

# print("Задание №4")
# rus_dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
# new_list = []
# with open('numbers.txt', 'r') as f_obj:
#     for line in f_obj:
#         line = line.split(' ', 1)
#         new_list.append(rus_dict.keys())
#         print(new_list)
# with open('numbers2.txt', 'w') as f_obj2:
#     f_obj2.writelines(new_list)


print("Задание №5")
fname = input("Название файла: ")
f = open(fname, 'w')
s = input("Введите числа через пробел: ")
f.write(s)
f.close()
with open('task5.txt') as f_obj:
    summa = 0
    for el in s.split():
        summa += int(el)
print(summa)