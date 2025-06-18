# #Funciones

# def suma():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("La suma es: ", n1+n2)

# def resta():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("la resta es: ", n1-n2)

# def mult():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("la multiplicación es: ", n1*n2)

# def div():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     try:
#         print("la division es: ", n1/n2)
#     except ZeroDivisionError as hola:
#         print("Error xddd")


# def calcu():
#     while True:
#         op=int(input('''seleccione una opcion: 
#                     1.- Suma
#                     2.- Resta
#                     3.- Multiplicación
#                     4.- División
#                     5.- Salir
                    
#                     '''))
#         match op:
#             case 1:
#                 print("Suma")
#                 suma()
#             case 2:
#                 print("Resta")
#                 resta()
#             case 3:
#                 print("Multiplicación")
#                 mult()
#             case 4:
#                 print("División")
#                 div()
#             case 5:
#                 print("saliendo")
#                 break
#             case _ :
#                 print("no valido")

# calcu()

# def suma_ret():
#     n1=int(input("Ingrese un numero"))
#     n2=int(input("Ingrese otro numero"))
#     return n1+n2

# nume=suma_ret()

# for i in range(nume):
#     print("hola")

# def suma():
#     n1=int(input())
#     n2=int(input())
#     print(n1+n2)

# def resta(n1,n2):
#     print(n1-n2)

# n1=int(input())
# n2=int(input())
# resta(n1,n2)

########################################

# def suma(n1,n2):
#     print(n1+n2)

# def resta(n1,n2):
#     print(n1-n2)

# def mult(n1,n2):
#     print(n1*n2)

# def div(n1,n2):
#     print(n1/n2)

# while True:
#     print('''
#         1.- Ingresar numero
#         2.- Suma
#         3.- Resta
#         4.- Mult
#         5.- Div
#         6.- Salir
#         ''')
#     op=int(input("ingrese la opción: "))
#     match op:
#         case 1:
#             n1=int(input("Ingrese el primer numero: "))
#             n2=int(input("Ingrese el segundo numero: "))
#         case 2:
#             suma(n1,n2)
#         case 3:
#             resta(n1,n2)
#         case 4:
#             mult(n1,n2)
#         case 5:
#             div(n1,n2)
#         case 6:
#             break
#         case _:
#             print("Invalido")


# def suma_print():
#     n1=int(input())
#     n2=int(input())
#     print(n1+n2)

# def suma_return():
#     n1=int(input())
#     n2=int(input())
#     return n1+n2

# suma_print()
# print(suma_return()*1.19)


# def promedio(x,y,z):
#     return (x+y+z)/3

# if promedio(40,70,22) >=40:
#     print("El alumno aprobo")
# else:
#     print("El alumno reprobo")

##Crear un programa para calcular un descuento
## pedir al usuario el precio, y el descuento a aplicar, mostrar los resultados
# total=0

# def descuento(n1,n2):
#     return n1*n2

# def iva(n1):
#     return n1*1.19

# precio=int(input("Ingrese el precio: "))
# descuent=float(input("Ingrese el descuento: "))

# print(descuento(precio,descuent))
# total=descuento(precio,descuent)
# print(iva(total))

# def calc_desc(precio,desc):
#     return precio*(desc/100)

# p=int(input("Ingrese el precio: "))
# d=int(input("Ingrese el descuento: "))

# print("El descuento es de: ", calc_desc(p,d))
# print("El precio es de : ", p-calc_desc(p,d))

# lista_prod=[
# {"nombre": "zapato", "precio":20000},
# {"nombre": "pelota", "precio":24000}

# ]

# # print(lista_prod[0]["nombre"])
# print(lista_prod)

# lista_prod.append({"nombre": "paleta", "precio":24000})



# while True:
#     print('''
#     1.- Agregar producto
#     2.- Mostrar productos
#     3.- Salir
#         ''')
#     op=int(input("Seleccione una opción"))
#     match op:
#         case 1:
#         case 2:
#         case 3:
#         case 4:

# total=0
# lista=[]
# def mostrar_lista(lista):
#             contador=0
#             for i in lista:
#                 print(contador+1,".- ",lista[contador]["nombre"], "$",lista[contador]["precio"])
#                 contador=contador+1

# while True:
#     print('''
#     1.- Agregar producto
#     2.- Mostrar productos
#     3.- Actualizar producto
#     4.- Borrar producto
#     5.- Comprar producto
#     6.- Salir
#         ''')
#     op=int(input("Seleccione una opción: "))
#     match op:
#         case 1:
#             producto=str(input("Ingrese el nombre del producto: "))
#             precio=int(input("Ingrese el valor del producto: "))
#             lista.append({"nombre": producto, "precio":precio},)
#         case 2:
#             mostrar_lista(lista)
#         case 3:
#             mostrar_lista(lista)
#             op=int(input("Seleccione el producto a modificar: "))
#             producto=str(input("Ingrese el nombre del producto: "))
#             precio=int(input("Ingrese el valor del producto: "))
#             lista[op-1]["nombre"]=producto
#             lista[op-1]["precio"]=precio
#         case 4:
#             mostrar_lista(lista)
#             op=int(input("Ingrese el producto a borrar"))
#             lista.pop(op-1)
#         case 5:
#               mostrar_lista(lista)
#               op=int(input("Ingrese el producto a comprar: "))
#               total=total+lista[op-1]["precio"]
#               print("total: ", total)
#         case 6:
#               break
            
#         case _:
#             print("invalido")

#Crear programa CRUD del siguiente diccionario
#  

personas={
    1:{"nombre": "Diego Rivera",
       "numero":[11111,11112],
       "estadocivil": "casado",
       "trabajando": True,
       "edad": 64},
    2:{"nombre": "Hola hola",
       "numero":[22222,22223],
       "estadocivil": "soltero",
       "trabajando": True,
       "edad": 64},
    3:{"nombre": "alo alo",
       "numero":[33333,33334],
       "estadocivil": "casado",
       "trabajando": False,
       "edad": 64},
}


while True:
    print('''
    1.- Ingresar personas
    2.- Mostrar personas
    3.- Actualizar persona
    4.- Borrar persona
    5.- Salir
''')
    op=int(input("Ingrese opcion: "))
    match op:
        case 1:
            nombre=str(input("Ingrese el nombre: "))
            numero=int(input("Ingrese el numero: "))
            estadocivil=str(input("Ingrese el estado civil: "))
            trabajando=bool(input("Ingrese si esta trabajando o no: "))
            edad=int(input("Ingrese la edad: "))
            nextkey=len(personas)
            personas[nextkey+1]={"nombre": nombre,
             "numero":[numero],
             "estadocivil": estadocivil,
             "trabajando": trabajando,
             "edad": edad},

        case 2:
            contador=1
            for i in personas:
                print(contador,".-", personas[contador])
                contador=contador+1

        case 3:
            op=int(input("Selecciona la persona a actualizar: "))
            

        case 4:
            op=int(input("Selecciona la persona a borrar: "))

        case 5:
            break