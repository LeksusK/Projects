print("Введите числа, после чего нажмите Enter:")
numbers = input() #принимаем числа в строку numbers
result = [] #сюда записываем чётные числа

for symbol in numbers:
    if symbol != ' ' or symbol != '0': #отбрасываем ненужные числа
        if (int(symbol) % 2 == 0): #проверка на чётность
            result.append(int(symbol)) #добавляем чет. числа в result

result.sort() #сортируем по возрастанию
result.reverse() #отразил result (сотрировка по убыванию)
print(result) #вывод чисед
