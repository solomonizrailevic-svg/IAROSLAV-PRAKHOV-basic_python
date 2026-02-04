"Методы строк"
q = "Yaroslav Prakhov"
print(type("Yaroslav"))

# print(q.upper())
# print(q.lower())
# print(q)
# строка.метод()

# print(q.count("v"))
# print(q.count("a", 0, 20))

# print(q.find("a", 7))
# print(q.rfind("a"))
# print(q.rfind("c"))
# print(q.find("f"))
# print(q.index("Y"))
# print(q.index("f"))

# print(q.replace("a","o"))
# print(q.replace("a","o",2))
# print(q.replace(" ",""))
# print(q.isalpha())
# print(q.replace(" ","").isalpha())
# print("Yaroslav Prakhov".isalpha())
# print("YaroslavPrakhov".isalpha())
# a = "22332456"
# print(a.isdigit())
# print(a.replace(""," ").isdigit())

# h = "23"
# v = "26"
# g = "54"
# print(h.rjust(8))
# print(v.rjust(8))
# print(g.rjust(8))
# print(h.rjust(8))
# print(v.rjust(8, "*"))
# print(g.rjust(8, "-"))
# print(h.rjust(8, "%"))
# print(v.ljust(8, "*"))
# print(g.ljust(8, "-"))
# print(h.ljust(8, "%"))

# s = "Yaroslav Prakhov Vadimovich"
# name, surname, father_name = s.split("")
# print(name)
# print(surname)
# print(father_name)
# e = "Yaroslav-Prakhov-Vadimovich"
# name, surname, fathername = e.split("-")
# print(name)
# print(surname)
# print(fathername)

# nums = "1,  2,33, 43,    ,23"
# print(nums.replace(" ","").split(","))

# words = ["str", "float","bool"]
# print(", ".join(words))

j = "   ffff fff   "
print(j.strip())
print(j.rstrip())
print(j.lstrip())