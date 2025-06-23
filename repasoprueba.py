# #Validaciones
# #Validar si un texto tiene 3 numeros

# texto="hola123"
# contador=0

# for i in texto:
#     print(i)
#     if i.isdigit():
#         print("Es digito")
#         contador=contador+1

# if contador>=3:
#     print("Es correcto")
# else:
#     print("El texto debe tener 3 o mas numeros")

'''
Crear gestion de vehiculos
Crear programa para un parking de autos
se debe ingresar
Marca, año, patente, Tipo

Marca: tipo string, se debe tipear la marca
año: tipo int , solo de 4 digitos enteros
patente: debe tener 4 letras minusculas y 2 digitos
tipo: S= sedan, C= Camioneta, M= moto

Se deve validar cada aspecto y tener un mantenedor para 
todos los vehiculos motorizados

1.- Ingresar Vehiculo
2.- Mostrar Vehiculos
3.- Actualizar Vehiculo
4.- Borrar Vehiculo
5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
6.- Salir

Usar dunciones con argumentos para poder validar
y para poder llamar las acciones dentro del menu
'''

# anio=1985

# print(len(str(anio)))

# if len(str(anio)) ==4:
#     print("Tiene largo de 4")
# else:
#     print("El largo no es de 4 numeros")



#Creacion de contraseña
#Debe tener, tres mayusculas, una minuscula
#un # y3 numeros


# def validarpwd(passwd):
#         contmayus=0
#         contminus=0
#         nums=0
#         gato=0

#         for i in passwd:
#             print(i)
#             if i.isupper():
#                 contmayus=contmayus+1
#             if i.islower():
#                 contminus=contminus+1
#             if i.isdigit():
#                 nums=nums+1
#             if "#" in i:
#                 gato=gato+1

#         if contmayus<3:
#             print("Debe tener 3 o mas mayusculas")
#         elif contminus<1:
#             print("Debe tener 1 o mas minusculas")
#         elif nums<3:
#             print("Debe tener 3 o mas numeros")
#         elif gato<1:
#             print("Debe tener un #")
#         else:
#             print("contraseña creada")
#             return True
def validarcode(passwd):
        contmayus=0
        contminus=0
        nums=0
        gato=0

        for i in passwd:
            print(i)
            if i.isupper():
                contmayus=contmayus+1
            if i.islower():
                contminus=contminus+1
            if i.isdigit():
                nums=nums+1

        if contmayus!=2:
            print("Debe tener 2 Mayusculas")
        elif contminus!=2:
            print("Debe tener 2 minusculas")
        elif nums!=4:
            print("Debe tener 4 numeros")
        else:
            print("Codigo Valido")
            return True



# passwd=str(input("Ingrese la clave"))
# validarpwd(passwd)


prods={
    1:{"nombre":"Zelda TOTK",
            "precio":2000,
            "code": "ZZkk1985"}
        
}


while True:
        print('''
              1.- Registrar un juego
              2.- Mostrar juegos
              3.- Actualizar juegos
              4.- Borrar juego
              5.- Salir
              ''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                    dict=prods
                    nombre=input("Ingrese un nombre: ")
                    precio=input("Ingrese el precio: ")
                    codigo=input("Ingrese su codigo: ")
                    if validarcode(codigo)==True:
                        print("hola")
                        largo=list(dict.keys())[-1]
                        dict[largo+1]={"nombre": nombre,
                                       "precio": precio,
                                       "codigo": codigo}
                    else:
                                    print("el paramatro de la clave no es correcto")
            case 2:
                print(prods)
                cont=1
                for i in prods:
                     print(prods[cont]["nombre"], prods[cont]["precio"], prods[cont]["code"])
                     cont=cont+1
            case 3:
                op=int(input("Ingresa el item a actualizar"))
                nombre=input("nombre")
                precio=input("precio")
                codigo=input("codigo")
                if validarcode(codigo)==True:
                    prods[op]={"nombre":nombre,
                "precio":precio,
                "code": codigo}

            case 4 :
                print("borrar")
            case 5:
                break
            case _:
                    print("Opcion invalida")