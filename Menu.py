import os

def Numeros(): #pedir cantidad de numeros, Solicitar numeros, positivos y negativos
    positivos=0
    negativos=0
    ceros=0
    cantidad=int(input("Cuantos numeros va a ingresar?: "))
    for i in range(cantidad):
        num=int(input(str(i+1)+ "Ingrese un numero: "))
        if (num>0):
            positivos+=1
        elif (num<0):
            negativos+=1
        else:
            ceros+=1

    print("Cantidad de positivos: "+str(positivos))
    print("Cantidad de negativos: "+str(negativos))
    print("Cantidad de ceros: "+str(ceros))
    tecla = input("Presiona cualquier tecla para continuar")


def Personas(): #Ingresar para n personas: Nombre y edad. Mostrar promedios de todas las edades ingresadas
    contadoredad=0
    sumita=0
    cantiPersonas=int(input("Ingrese cantidad de personas que va a registrar: "))
    for i in range(cantiPersonas):
        nom=input(str(i+1)+"Ingrese su nombre: ")
        edad=int(input("Ingrese su edad: "))
        contadoredad=+1
        sumita=+edad

    print("El promedio de todas las edades es de: "+str(sumita/contadoredad));
    tecla = input("Presiona cualquier tecla para continuar")


verde=True
while(verde):
    os.system('cls')
    print("1. Numeros")
    print("2. Datos Personales")
    print("3. Finalizar")
    print("-------------------")
    opcion=int(input("Ingrese una de las opciones: "))
    if (opcion==1):
        Numeros()
    if (opcion==2):
        Personas()
    if (opcion==3):
        print("Cerrando Menu...")
        break
    