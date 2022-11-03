import math

# definir um intervalo de [a,b] e a parada [p]
a = 0
b = 2
p = 0.01

# função definida
def f(x):
    return x**3 - 2 

if f(a) * f(b) < 0:
    while (math.fabs(b-a)/2 > p): #criterio de parada
        x = (a+b)/2
        print("x: ",x)
        print("f: ",f(x))
        if f(x) != 0:
            if f(a) * f(x) < 0:
                b = x
            else:
                a = x
        else:
            print("A raiz é: ", x)
            break
    print("---------------------")
    print("a: ", a)
    print("b: ", b)
    print("(b-a)/2: ",math.fabs(b-a)/2)
    print("Valor da raiz é: ", x)
else:
    print("Não podemos afirmar que há raiz neste intervalo!")
