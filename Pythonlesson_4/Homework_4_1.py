from pydoc import stripid

s = "Python для автоматизации"
print(s.upper())
print(s.lower())

msg = "абракадабра"
print(msg.count("ра"))
print(msg.count("а", 3))

print(msg.index("ка", 0,10))
print(msg.rfind("а"))
print(msg.find("xyz"))

text = "Я изучаю Java"
print(text.replace("Java", "Python"))
print(text.replace(" ", ""))

stroka ="python"
print(stroka.isalpha())
stroka2 = "12345"
print(stroka2.isdigit())
stroka3 = "123abc"
print(stroka3.isdigit())

code = "42"
print(code.ljust(5, "0"))
st = "text"
print(st.rjust(10, "*"))

fruits = "яблоко, груша, банан"
print(fruits.split(", "))
yaziki = "Python;Java;C++"
print(yaziki.split(";"))

spisok = ["Привет", "мир", "!"]
print(" ".join(spisok))
spisok2 = ["apple", "banana", "cherry"]
print(",".join(spisok2))

troka1 = " Python"
print(troka1.lstrip(" "))
troka2 = "Python "
print(troka2.rstrip(" "))
troka3 = " Python "
print(troka3.strip(" "))

text = "программирование"
print(text.title())
print(text.count("р"))
print(text.index("и"))
print(text[::-1])

