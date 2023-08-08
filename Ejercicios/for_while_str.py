'''
ciclo for
'''

for x in range(6):
    print(x)

for x in "banana":
    print(x)

for x in range(2, 6): #inicia desde el 2 hasta el 6
    print(x)

for x in range(2, 30, 3): #incrementa de a 3
    print(x)

for x in range(6):
    if x == 3:
        print(x)
    else:
        print("finally finished")


'''
ciclo while
'''

i=1
while i < 6:
    print(i)
    i += 1

i=1
while i < 6:
    print(i)
    if i==3:
        break
    i += 1

i=0
while i < 6:
    i += 1
    if i ==3:
        continue
    print(i)

i=1
while i < 6:
    print(i)
    i += 1
else:
    print("i no es menor que 6")



'''
Strings and arrays
'''

a = "hola, mundo"
print(a[i])

for x in "banana":
    print(x)

a = "hello, world"
print(len(a))

txt = "the best things in life are free"
print("free" in txt)

txt = "the best things in life are free"
if "free" in txt:
    print("yes,  'free' is present")

txt  = "the best things in life are free"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")

txt = "the best things in life are free"
print("expensive" not in txt)

b = " Hello, World! "
print(b[2:5])

print(b[:5])

print(b[2:])

print(b[-5:-2])

print(b.upper())

print(b.lower())

print(b.strip()) #returns "Hello, World!" , quiere decir que borra los espacios que tienen las cadenas de textos

print(b.replace("H", "j"))

print(b.split(",")) #returns ['Hello', 'World']

age = 20
txt = "my name is cesar, i am " + str(age)
print(txt)

txt = "my name is cesar, and i am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "i want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

myorder = "i want to pay  {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))