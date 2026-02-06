text = "Hello\nPython"
print(text)
# "Python" перешел на новую строку по причине перевода строка через \n символ

t = "Python\tAutomation"
print(t)
# Потому что символ \t создает отступ

path = "C:\new\test.txt"
print(path)
# пайтон считал некоторые данные в объекте как символы табуляции, такие как \n и \t
path2 = "C:\\new\\test.txt"
print(path2)
marka = "Марка вина \"Ягодка\""
print(marka)

path = r"C:\new\test.txt"
print(path)
#в сырой строке пайтон не обращает внимание на спецсимволы в ней и выводит все как написано

s = "Hello\b World"   # все дело в \b который возвращает курсор на одну позицию назад и перезаписывает символ
print(s)
s = "Hello\fPython"
print(s)
