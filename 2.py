a = int(input('Введите длину массива А: '))
array1 = []
i = 0
print('Введите массив A:')
while i < a:
    array1.append(int(input()))
    i+=1

b = int(input('Введите длину массива B: '))
array2 = []
i = 0
print('Введите массив B:')
while i < b:
    array2.append(int(input()))
    i+=1

print('Массив A:', array1)
print('Массив B:', array2)

array3 = []
for i in array1:
    if i in array2 and i not in array3:
        array3.append(i)

for item in array3:
    if array1.count(item) > array3.count(item) and array2.count(item) > array3.count(item):
        m = min(array1.count(item), array2.count(item))
        for i in range(m-1):
            array3.append(item)

if len(array3) != 0:
    print('Общие элементы для А и В:', array3)
else:
    print('Общих элементов нет')