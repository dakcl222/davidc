# #Funciones

def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("La suma es: ", n1+n2)

def resta():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("la resta es: ", n1-n2)

def mult():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("la multiplicación es: ", n1*n2)

def div():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    try:
        print("la division es: ", n1/n2)
    except ZeroDivisionError as hola:
        print("Error xddd")


def calcu():
    while True:
        op=int(input('''seleccione una opcion: 
                    1.- Suma
                    2.- Resta
                    3.- Multiplicación
                    4.- División
                    5.- Salir
                    
                    '''))
        match op:
            case 1:
                print("Suma")
                suma()
            case 2:
                print("Resta")
                resta()
            case 3:
                print("Multiplicación")
                mult()
            case 4:
                print("División")
                div()
            case 5:
                print("saliendo")
                break
            case _ :
                print("no valido")

calcu()

# def suma_ret():
#     n1=int(input("Ingrese un numero"))
#     n2=int(input("Ingrese otro numero"))
#     return n1+n2

# nume=suma_ret()

# for i in range(nume):
# print("hola")


#Realizar un programa que incluya match y llame a otras funciones, estas funciones deben incluir if, if else
#for y/o while 
#el programa debe ser recursivo xd