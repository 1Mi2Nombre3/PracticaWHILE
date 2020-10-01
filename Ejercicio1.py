#X = Viaje sin tarjeta 
#Y = Viaje con tarjeta 
#A = Valor de la tarjeta 
#B = Carga Inicial 

N = 0
X = float (input('Viaje sin tarjeta  : '))
while X < 0:
    print('Ingrese un Numero Mayor a 0 porfabor')
    X = float (input('Viaje sin tarjeta  : '))
    
Y = float (input('Viaje con tarjeta  : '))
while Y < 0 or Y > X:
    print('Ingrese un Numero Mayor a 0 o Menor al viaje con tarjeta')
    Y = float (input('Viaje con tarjeta  : '))
    
A = float (input('Valor de la tarjeta: '))
while A < 0 or A < X:
    print('Numero Mayor a 0 o mayor al precio de las tarjetas')
    A = float (input('Viaje con tarjeta  : '))
    
B = float (input('Carga Inicial      : '))
while B < 0 or B > A:
    print('Numero Mayor a 0 o menor al valor de la tarjeta ')
    B = float (input('Viaje con tarjeta  : '))

#2 viajes al dia
#5 dias a la semana

X_1 = X*2     #Precio de viaje por 1 dia (Sin tarjeta) :  
X_2 = X*5     #Precio de viaje por 5 dias (Sin tarjeta): 
Y_1 = Y*2     #Precio de viaje por 1 dia (Con tarjeta) :  
Y_2 = Y_1*5     #Precio de viaje por 5 dias (Con tarjeta): 

R = Y_2 / Y   #Precio 1
R_1 = Y_1 / R #Precio ahorrado por cada viaje
print('Precio ahorrado por cada viaje', R_1)

R_2 = R_1 * 2 #Precio ahorrado por dia:
print('Precio ahorrado por dia', R_2)

R_3 = R_2 * 5 #Precio ahorrado por 5 dias:
print('Precio ahorrado por semana', R_3)

#Considerando que 5 dias es 1 semana

Semana = A // R_3
Dias = A // R_2 - 5
if Dias > 5:
    print(Semana, 'Semanas 0 Dias')
elif Dias <= 5:
    print(Semana, 'Semanas', Dias, 'Dias')





