# тернарный оператор(позволяет делать код более компактным)
a = 18
b = 15
if a > b:
    res = a
elif b > a:
    res = b
else:
    print("Числа равны")
print(res)

# тернарный оператор:
a = 18
b = 15
if a > b:
    res = a
else:
    res = b
print(res)
# другой способ
res = a if a > b else b
print(res)
#  в тернарном операторе должен быть элс

res = a +10 if a > b else b
print(res)

res = print(a +10) if a > b else b
print("Запринтовали res второй раз", res)
