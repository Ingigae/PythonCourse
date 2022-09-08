month = int(input('Введите номер месяца от 1 до 12: '))
month_dict= {"зима": [12, 1, 2], "весна":[3, 4, 5], "лето":[6, 7, 8], "зима":[9,10,11]}
if 1<=month<=12:
    for n in month_dict.items():
        if month in n [1]:
            print(n[0])
else print('Error')
