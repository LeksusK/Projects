# получение данных из файла
with open('INPUT.TXT') as fr:
    lines = fr.readlines()
# разделение на отдельные числа
s = ''
for line in lines:
    s += line.rstrip() + ' '
sSort = s.split(' ')
sSort.pop(-1)
#проверка
#print(sSort)

start = 1
tmp = 0
for i in range(int(sSort[0])):
    # res - это флаг, который != 0, если a=c и b=d
    res = 0
    a = int(sSort[start])
    b = int(sSort[start + 1])
    c = int(sSort[start + 2])
    d = int(sSort[start + 3])
    #проверка
    #print("a =", a)
    #print("b =", b)
    #print("c =", c)
    #print("d =", d)
    if (a == c) and (b == d):
        res += 1
    # использование алгоритма Евклида
    while b != 0:
        if res != 0:
            break
        if (a == c) and (b == d):
            res += 1
        if b > a:
            tmp = a
            a = b
            b = tmp
            if (a == c) and (b == d):
                res += 1
        a = a - b
        if (a == c) and (b == d):
            res += 1
        if res != 0:
            break
    # запись ответа в файл
    # если первая итерация, то перезазапишем информацию, а не добавим
    if i == 0:
        if res != 0:
            with open('OUTPUT.TXT', 'w') as fw:
                fw.write("YES")
        else:
            with open('OUTPUT.TXT', 'w') as fw:
                fw.write("NO")
    else:
        if res != 0:
            with open('OUTPUT.TXT', 'a') as fw:
                fw.write("\n")
                fw.write("YES")
        else:
            with open('OUTPUT.TXT', 'a') as fw:
                fw.write("\n")
                fw.write("NO")
    # на всякий
    if start == len(sSort) - 4:
        break
    # задаём новую точку старта, для новых a, b, c, d
    start += 4