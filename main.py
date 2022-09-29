foot_dict = {
'Россия': 'A',
'Португалия': 'B',
'Франция': 'C',
'Дания': 'C',
'Египет': 'A'
}
foot_dict['Турция'] = 'B'
foot_group = input('Введите название группы \n')
for i in foot_dict:
    if foot_dict[i] == foot_group:
        print(i)
a = 0
b = 0
c = 0
for j in foot_dict:
    if foot_dict[j] == 'A':
        a += 1
    elif foot_dict[j] == 'B':
        b += 1
    elif foot_dict[j] == 'C':
        c += 1
print('В группе А', a, 'команд')
print('В группе B', b, 'команд')
print('В группе C', c, 'команд')