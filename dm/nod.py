# получение данных из файла
with open('INPUT.TXT') as fr:
    s = fr.read()
nms = []
nms = s
a1 = []
b1 = []

# разделение исходной строки на два числа
for i in range(len(s) - 1):
    if nms[i + 1] != ' ':
        a1.extend(nms[i])
    else:
        a1.extend(nms[i])
        t = i + 2
        break
for i in nms[t::]:
    b1.extend(i)
# перевод двух чисел из списка в int
a = int(''.join(map(str, a1)))
b = int(''.join(map(str, b1)))

# просто проверка <3
#print(a1)
#print(b1)
#print(a)
#print(b)

# использование алгоритма Евклида
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
res = str(a + b)

# запись ответа в файл OUTPUT
with open('OUTPUT.TXT', 'w') as fw:
    fw.write(res)