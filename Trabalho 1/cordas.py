import math

# definir um x0 e x1 [x0, x1] e a parada [p]
x0 = 0
x1 = 0.5
p = 3

# função definida
def f(x):
    return x**2 - 2 * x + 1 

# função metodo das cordas
def fc(x0_old, x1_old, x0, x1):
    return (x1_old - ((x1 / (x1 - x0)) * (x1_old - x0_old)))

count = 0

while (count != p): #criterio de parada
    x0_old = x0
    x1_old = x1
    
    x0 = f(x0)
    x1 = f(x1)

    #print("x0: ", x0)
    #print("x1: ", x1)
    x2 = fc(x0_old, x1_old, x0, x1)

    x0 = x1_old
    x1 = x2

    print("fc(x): ", x2)
    count += 1

x = x2

print("---------------------")
print("x", count, ": ", x)
