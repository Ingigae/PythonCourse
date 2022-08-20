my_string = str(input('Введите в строку несколько слов, разделенных пробелом: ')).split()
for n, t in enumerate (my_string,1):
    print(f'{n}: {t[:10]}')

