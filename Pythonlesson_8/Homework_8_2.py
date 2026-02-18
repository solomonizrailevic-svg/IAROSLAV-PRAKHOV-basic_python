p = int(input("Введите число: "))
kc = []
kc = [i ** 2 for i in range(1, p + 1)]
print(kc)


lst = [i for i in range(-10, 11) if i % 2 == 0]
print(lst)

lst_words = ["Fork", "Plate", "Spoon", "Glass"]
lst_ = [len(lst_words[i]) for i in range(len(lst_words))]
print(lst_)

numbers = ["четное" if num % 2 == 0 else "нечетное" for num in range(0, 20)]
print(numbers)

lst = ["Grok", [29, 34], 23]
for item in lst:
    try:
        iter(item)
        print("True")
    except TypeError:
        print("False") # подсмотрел у грока