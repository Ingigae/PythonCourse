test_list = input('Введите значения через пробел:').split()
for n in range(1, len(test_list), 2):
    test_list.insert(n-1,test_list.pop(n))
print (test_list)