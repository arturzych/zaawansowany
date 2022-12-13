import re

with open('C:\\Users\\Artur\\PycharmProjects\\zaawansowany\\my_regex.txt', 'r') as file:
    data = file.read()

x = re.findall(".*py", data)
print(x)

y = re.finditer(".*py", data)

for i in y:
    print(i)

print('========================')
z = re.search(".+\.py", data)
print(z)

'''import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)'''
