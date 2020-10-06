#Suma, Multiplicacion y Exponente de 2 numeros
numero1=int(input("Digite un numero: "))
numero2=int(input("Digite un segundo numero: "))
suma=numero1+numero2
multi=numero1*numero2
Exponente=numero1**numero2
print("La suma de "+str(numero1)+ " Y " +str(numero2)+ " Es: " +str(suma))
print("La multiplicacion de "+str(numero1)+ " Y " +str(numero2)+ " es: " +str(multi))
print("El resultado de "+str(numero1) + " elevado a " +str(numero2)+ " Es: " +str(Exponente))

if (numero1>numero2):
	print("De los digitos que ingreso: " +str(numero1)+ " Es mayor que "+str(numero2))
elif(numero2>numero1):
	print("De los digitos que ingreso: " +str(numero1)+ " Es mayor que "+str(numero2))
else:
	print("Ambos numeros son iguales")

