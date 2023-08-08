import math

numeros = [1, 4, 9, 16, 25]

"""
raices = []
for n in numeros:
    raices.append(int(math.sqrt(n)))
"""

raices = [int(math.sqrt(x)) for x in numeros ]
print(raices)

v = [x if (x > 10) else '*' for x in numeros]
print(v)

l = [c.upper() for c in 'Maldonado']
print(l)

a = [l if l in 'aeiou' else '*' for l in 'murcielago']
print(a)