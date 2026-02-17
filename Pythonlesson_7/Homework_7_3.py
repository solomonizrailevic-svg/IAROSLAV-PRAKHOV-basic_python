s=("Çok güzel oldu")
строка = list(s)
строка.reverse()
for letter in строка:
    print(letter)

g = [2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(g)):
    if g[i] % 2 == 0:
        g[i] = 0
    print(g[i])

k = int(input("Введите число: "))
степени = []
for k in range(k + 1):
    степени.append(2 ** k)
print(степени)

a = int(input("Введите число: "))
b = int(input("Введите число: "))
k = int(input("Введите число: "))
ch = 0
for ch in range(a, b, k):
    print(ch)