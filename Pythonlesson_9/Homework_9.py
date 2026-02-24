dict_fruits = {"name_1": "Манго", "price for 1 kilo": 50, "name_2": "apple", "price for 1 kilo": 70}
dict_fruits.setdefault ("name_3", "orange")
print(dict_fruits)

grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
for name in grades:
    if grades[name] >= 4:
        print(name)

countries = {"Germany": "Berlin", "United States": "Washington", "Saudi Arabia": "Riyadh", "Canada": "Ottawa"}
choice = input("Введите название страны: ")
for country in countries:
    if choice == country:
        print(countries[country])
    if not choice in countries:
        print("Страна не найдена")
        break

students = [
    ("Анна", "Python"),
    ("Борис", "Java"),
    ("Виктор", "Python"),
    ("Галина", "C++"),
    ("Дмитрий", "Python")
]
dict_student = {"Python": ["Анна", "Виктор", "Дмитрий"],"C++": ["Галина"], "Java": ["Борис"]}
print(dict_student)

dict_ex = {"Jason": "5", "Stacy": "4", "Enthony": "3", "Adam": "2"}
dict_ex.pop("Adam")
print(dict_ex)

students = ["Анна", "Борис", "Виктор", "Галина"]
students_dict = {}
for student in students:
    students_dict[student] = None
students_dict["Анна"]   = 19
students_dict["Борис"]  = 21
students_dict["Виктор"] = 20
students_dict["Галина"] = 18
print(students_dict)

exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
money = input("Введите валюту (USD, EUR, GBP): ").strip().upper()
if money in exchange_rates:
    print(f"{money}: {exchange_rates[money]}.")
else:
    print("Неизвестная валюта")
    exchange_rates[money] = None
    print(f"Добавлена новая валюта: {money} → {exchange_rates[money]}")

dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
dict1.update(dict2)
print(dict1)

t = (1423, 2223, 343242, "fd", [23123,213])
print(t[1], t[-1])

nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
print(nums.count(4))
print(nums.index(7))

lst = ["Python", "Java", "C++", "JavaScript"]
t = tuple(lst)
print("C++ присутствует" if "C++" in t else "отсутствует")

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t[0:3])
print(t[:-4:-1])
print(t[0::2])

t = (1423, 2223, 343242, "fd", [23123,213], {22, 346})
t[4].append("Nem element")
print(t)