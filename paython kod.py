from random import *

n = 24
a = [0] * n  # 0'larla dolu bir liste oluşturuldu
s = 1

for i in range(n):
    a[i] = randint(-12, 24)  # Listenin belirli indekslerine rastgele sayılar atanır
    print('A:', a[i])
for i in range(n):
    if i % 2 == 0:
        s = s * a[i]
        print(s)
