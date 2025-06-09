# #       -5 -4 -3 -2 -1
# numeros=[2,5,12,8,4]
# #        0 1  2 3 4


# # print(numeros[3])

# for numero in numeros:
#     print("Numero: ", numero)



# nombres=["Felipe", "Curly", "Larry", "Moe"]

# print(nombres)

# nombres.append("Luthien")

# print(nombres)

# n=["Hola1", "Hola2", "Hola3"]
# a=["Adios1", "Adios2", "Adios3"]
# contador=0
# for i in n:
#     print(n[contador], a[contador])
#     contador=contador+1

# nombres=[]
# apellidos=[]
# contador=0

# while True:

#     print('''
#        1. Ingresar Nombre
#        2. Mostrar nombres
#        3. Buscar 
#        4. Salir

#         ''')
#     op=int(input())

#     match op:
#         case 1:
#             ing=str(input("Ingrese un nombre: "))
#             nombres.append(ing)
#             ap=str(input("Ingrese su apellido: "))
#             apellidos.append(ap)

#         case 2:
#             for i in nombres:
#                 print(nombres[contador], apellidos[contador])
#                 contador=contador+1

#         case 3:
#             buscar=str(input("Indique que nombre buscar: "))
#             if buscar in nombres:
#                 print(f"El nombre {buscar} está en la lista")
#             else:
#                 print(f"El nombre {buscar} no está en la lista")


#         case 4:
#             break

productos=[]
precios=[]
total=0

while True:
    print('''
        Selecciona una opción
    1. Agregar productos (Nombre producto y precio)
    2. Comprar (submenu mostrando productos y precios)
    3. Crear boleta
    4. Salir 
        ''')
    op=int(input())
    match op:
        case 1:
            producto=str(input("Ingrese el nombre del producto: "))
            productos.append(producto)
            precio=int(input("Ingrese el precio del producto: "))
            precios.append(precio)

        case 2:
            while True:
                contador=0
                print("Seleccione el producto: ")
                for i in productos:
                    print(productos[contador], precios[contador])
                    contador=contador+1
                op=str(input("Seleccione el producto: "))
                if op in productos:
                    print(f"Usted selecciono el Producto {op}")

        case 3:
            print("hola3")
        case 4:
            break
        case _:
            print("Opción invalida")

