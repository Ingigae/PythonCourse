test_list = [11, 10, 8, 6, 3, 1]
users_n = ""
while users_n != "s":
    users_n = input('Введите Ваше натуральное число, для окончания цикла введите s ')
    if users_n !="s" and float(users_n)%1 == 0 and int(users_n)>0 :
        i=0
        for n in test_list:
            if int(users_n)<=int(n):
                i=i+1
            else:
                break
        test_list.insert(i, int(users_n))
        print(test_list)
    else:
        print('Ошибка, введите натуральное число')
else:
    print('Программа остановлена')


