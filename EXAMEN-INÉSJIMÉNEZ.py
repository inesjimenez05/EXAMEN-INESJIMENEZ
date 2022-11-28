'''
·4-Crea una función que NO reciba ningún parámetro y que imprima por pantalla 
las opciones: 1-Sumar 2-Salir

·5-Crea una función que reciba dos números y devuelva la suma de estos números.

·6-El programa principal tiene que mostrar el menú de la función y hasta que se pulse 
la opción 2-Salir el programa tiene que funcionar.

·7-Si se pulsa la opción 1, el programa pide al usuario dos números y con la ayuda 
de la función sumar mostrar por pantalla el resultado.

·8-Cuando el usuario introduce dos números se puede equivocar e introducir caracteres 
con lo que el programa se interrumpe. Realiza los cambios necesarios para controlar 
estos errores.
'''


def sumaNumeros (num1,num2): 
    suma=num1+num2
    return (suma)


def mostrarMenu ():
    print("1-Sumar")
    print("2-Salir")


numero=0


while (numero!=2):
    try:
        mostrarMenu()
        numero=int(input("Selecciona una opción: "))

        if numero==1:
            num1=int(input("Di un numero: "))
            num2=int(input("Di otro numero: "))
            print(f"La suma es {sumaNumeros(num1,num2)} \n")

    except:
        print("Error, introduce un número válido \n")