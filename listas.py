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

# productos=[]
# precios=[]
# total=0
# ##terminar
# while True:
#     print('''
#         Selecciona una opción
#     1. Agregar productos (Nombre producto y precio)
#     2. Comprar (submenu mostrando productos y precios)
#     3. Crear boleta
#     4. Salir 
#         ''')
#     op=int(input())
#     match op:
#         case 1:
#             producto=str(input("Ingrese el nombre del producto: "))
#             productos.append(producto)
#             precio=int(input("Ingrese el precio del producto: "))
#             precios.append(precio)

#         case 2:
#             while True:
#                 contador=0
#                 print("Seleccione el producto: ")
#                 for i in productos:
#                     print(contador,".- ", productos[contador], precios[contador])
#                     contador=contador+1
#                 while True:
#                     try:
#                         op=int(input("Seleccione el producto: "))
#                         print("Usted seleccionó el producto", productos[op])
#                         total=total+precios[op]
#                         print(total)
#                         break
#                     except IndexError:
#                         print("No hay producto en ese espacio") 

#         case 3:
#             print("hola3")
#         case 4:
#             break
#         case _:
#             print("Opción invalida")

notas=[]
suma=0
promedio=0
while True:
    print('''
    1.- Ingresar Nota
    2.- Borrar nota
    3.- Mostrar notas
    4.- Sacar promedio, nota mayor y nota menor
    5.- Limpiar todas las notas
    6.- Salir
        ''')
    op=int(input())
    match op:
        case 1:
            nota=float(input("Ingrese una nota: "))
            notas.append(nota)
            print(f"Se ingreso la nota: {nota}")
        case 2:
            while True:
                try:
                    op=int(input("Seleccione una nota a borrar: "))
                    notas.remove(notas[op-1])
                    break
                except IndexError:
                    print("No hay notas en ese espacio")
        case 3:
            contador=0
            for i in notas:
                print(contador+1, ".-",notas[contador])
                contador=contador+1
        case 4:
            contador=0
            for i in notas:
                suma=suma+notas[contador]
                contador=contador+1
            promedio=promedio+suma/contador
            print("El promedio es: ", promedio)
            print("La nota maxima fue: ", max(notas))
            print("La nota minima fue: ", min(notas))
        case 5:
            notas.clear()
        case 6:
            break

###### append() Pone un elemento al final de la lista
###### sum() suma todos los elementos de la lista
###### max() muestra el elemento mayor
###### min() muestra el elemento menor
###### len() muestra el largo del objeto
###### pop() elimina un elemento por el indice
###### remove() elimina un elemento por el valor
###### clear() limpia la lista completa
###### insert() inserta un elemento en el indice indicado
###### enumerate() enumera la lista con otro argumento
###### extend() agrega varios elementos a la lista
###### sort() ordena la lista de mayor a menor
###### reverse() voltea la lista