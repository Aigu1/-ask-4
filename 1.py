n = int(input('Введите длину массива: '))
array = []
i = 0
print('Введите массив:')
while i < n:
    array.append(float(input()))
    i+=1
print('Входной массив:', array)
maximum = array[0]
for i in range(n):
    if array[i] >= maximum:
        maximum = array[i]
        element_number = i
print("Максимальный элемент:", maximum)
for a in range(element_number + 1, n):
    array[a] = 0
print('Результат:', array)