import math

# definir um X0 [x] e a parada [p]
x = 0
p = 3

# função definida
def f(x):
    return x**2 - 2 * x + 1 

# derivada da função
def fl(x):
    return 2 * x - 2

# formula newton
def fn(x, x1, x2):
    return x - (x1 / x2)

count = 0

while (count != p): #criterio de parada
    x1 = f(x)
    x2 = fl(x)
    print("f(x): ",x1)
    print("fl(x): ",x2)
    print("x: ",x)

    x = fn(x, x1, x2)
    count += 1

print("---------------------")
print("x", count, ": ", x)
