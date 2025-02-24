#lambda funtion: utile per definire funzioni brevi
"""def somma(a,b):
    return a+b
x, y = 10, 4
print(somma(x,y))

somma1 = lambda a,b: a+b

print(somma1(x,y))"""
somma1 = lambda a,b: a+b
lista=[10,4]
print(somma1(*lista))