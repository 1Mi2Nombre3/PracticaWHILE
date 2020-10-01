#N = NumeroFactorial
#N = Numeros del 1 al 5: 1*2*3*4*5 = 120

N = int (input('Ingrese un numero entero: '))
while N < 0:
    N = int (input('Ingrese un numero entero: '))
    
for i in range(0, N):
    i = i+1
    N= N+i
print(N)
    
for i in range(0, N):
    N = N+i
print(N)
