#N = NumeroFactorial
#N = Numeros del 1 al 5: 1*2*3*4*5 = 120

N = int (input('Ingrese un numero entero: '))
while N < 0:
  N = int (input('Ingrese un numero entero: '))
M = 1
while(N != 0):
    M = M * N
    N = N - 1
print('El factorial de su numero es: ', M)
    

