#Ciclo que permita mostrar 10 numeros. Que cunete cuantos son pares y cuantos impares

par=0
impar=0
for i in range (10):
    num=int(input("Ingrese un numero: "))
    if(num%2==0):
        par=par+1
    else:
        impar=impar+1

print("La cantidad de numeros pares es: "+str(par))
print("La cantidad de numeros impares es: "+str(impar))