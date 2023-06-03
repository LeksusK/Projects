from math import gcd
k = 0
# получение данных из файла
with open('INPUT.TXT') as fr:
    s = fr.read()

# разделение на отдельные числа
sUpgrade = s.split(" ")
#print(sUpgrade)

x1 = int(sUpgrade[0])
y1 = int(sUpgrade[1])
x2 = int(sUpgrade[2])
y2 = int(sUpgrade[3])


# n = НОД(|x2 - x1|,|y2 - y1|)
n = gcd(abs(x2 - x1), abs(y2 - y1))
res = str(n + 1)

# запись ответа в файл OUTPUT
with open('OUTPUT.TXT', 'w') as fw:
    fw.write(res)
