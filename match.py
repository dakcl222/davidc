# #La florida 20% ,la pintana 30%, puente alto 25%, san joaquin 25%
# #Grupo familiar: 1-->2%, 2 a 4 -> 3%, 5 o mas -> 4%
# # preguntar al usuario en que comuna vive
# # pregunar al ausuario con cuantas personas vive
# # el arancel actual es de 200.000 por semestre
# # basados en las respuestas del usuario y en
# # la informaicon dada, calcular su descuento
# import random

# def arancel():

        

#     descuento=1
#     arancel=200000
#     print("Comunas disponibles: La florida, La pintana, Puente alto, San joaquin")
#     comuna=str(input("Ingrese su comuna: "))
#     personas=int(input("Con cuantas personas vive?: "))
#     if comuna.lower()=="la florida":
#         descuento=descuento-0.20
#     elif comuna.lower()=="la pintana":
#         descuento=descuento-0.30
#     elif comuna.lower()=="puente alto":
#         descuento=descuento-0.25
#     elif comuna.lower()=="san joaquin":
#         descuento=descuento-0.25
#     if personas==1:
#         descuento=descuento-0.02
#     elif personas>=2 and personas<=4:
#         descuento=descuento-0.03
#     elif personas>=5:
#         descuento=descuento-0.04

#     print(f"El total a pagar es:", round(arancel*descuento,1))
# def azarN():
#     num=random.randint(1,10)
#     print("Numero al azar: ", num)
#     return num
# def menu_tarea():
#     while True:
#         print(''' 
#         Seleccione una opcion:
#         1.- Numero al azar
#         2.- Calcular arancel
#         3.- Salir 

#         ''')
            
#         op=int(input())
#         match op:
#             case 1:
#                 azarN()
#             case 2:
#                 arancel()
#             case 3:
#                 break
#             case _ :
#                 print("opción invalida")


# #Crear un menu de carrito con las siguientes opciones
# #1.- Ingresar nombre del usuario
# #Sera mostrado en la boleta, con un saludo
# #2.- Comprar, poner productos para poder comprar
# # con su precio correspondiente
# #3.- Sacar boleta, calcular el precio neto
# #y el precio mas IVA, mostrar totales 
# #4.- Salir

# #Consideraciones:
# #Por lo menos 3 productos
# #No hay limite de compra
# #Se puede salir en cualquier momento
# #Los montos de los productos son fijos

total=0
while True:
    print(''' 
    1.- Ingresar nombre del usuario
    2.- Comprar
    3.- Sacar boleta
    4.- Salir
    ''')
    op=int(input())
    match op:
        case 1:
            print("ingrese su nombre")
            nombre=str(input())
        case 2:
            while True:
                print(''' 
            1.- hola1 500$
            2.- hola2 1000$
            3.- hola3 1500$
            4.- Salir
            ''')
                op2=int(input())
                match op2:
                    case 1:
                        total=total+500
                        print("total neto: ", total)
                    case 2:
                        total=total+1000
                        print("total neto: ", total)
                    case 3:
                        total=total+1500
                        print("total neto: ", total)
                    case 4:
                        break
                    case _ :
                        print("invalido")

        case 3:
            print(f"Hola {nombre}")
            print("El total es: ", total)
            print("El total+iva es: ", total*1.19)
        case 4:
            break
        case _:
            print("invalido")
