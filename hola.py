# nombre="diego"
# edad=64


# print("hola ", nombre, "su edad es", edad)
# print(f"hola (nombre) y su edad es (nombre)")


# #Solicitud de datos
# print("ingrese su nombre")
# nombre=input()
# print("ingrese su edad")
# edad=input()
# #ejemplo de concatenacion
# print("hola ", nombre, "su edad es", edad)

# #Caracter = String Entero = Integer,int Real = float Logico = boolean true false 

# print("Ingrese un numero")
# n1=int(input())
# print("Ingrese otro numero")
# n2=int(input())
# print("Ingrese otro numero")
# n3=int(input())
# prom=(n1+n2+n3)/3


# print("El promedio de los numeros es: ",prom )

# if prom>=4.0:
#     print("el alumno aprobo")
# else:
#     print("el alumno reprobo")

# #pedir edad al usuario y determinar si es mayor de edad

# print("Ingrese su edad")
# edad=int(input())

# if edad>=18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor de edad")


# #Mostrar segun criterio
# #menos de 12 años es niños
# #entre 12 y 17 es adolescente
# # entre 18 y 64 es adulto
# # 65 y mas es adulto mayor

# print("Ingrese su edad")
# edad=int(input())

# if edad<12:
#     print("Usted es un niño")
# elif edad>=12 and edad<18:
#     print("Usted es adolescente")
# elif edad>=18 and edad<65:
#     print("Usted es adulto")
# else:
#     print("Usted es un adulto mayor")


# #Ingresar 3 numeros y mostrar el mayor de los 3 

# n1=int(input("Ingrese el primer numero: "))
# n2=int(input("Ingrese el segundo numero: "))
# n3=int(input("Ingrese el tercer numero: "))

# if n1>n2 and n1>n3:
#     print("El numero mayor es: ", n1)
# elif n2>n1 and n2>n3:
#     print("El numero mayor es: ", n2)
# elif n3>n1 and n3>n2:
#     print("El numero mayor es: ", n3)
    
# pw=2233
# print("Ingrese su clave")
# clave=int(input())

# if clave==pw:
#     print("Pasa")
# else:
#     print("No pasa")

# #par impar

# num=int(input("INgrese un numero "))

# if num % 2==0:
#     print("el numero: ", num, " Es par")
# else:
#     print("el numero: ", num, " Es impar")

# cant=int(input("Ingrese la cantidad de numeros: "))
# cont=0
# cont2=0
# for i in range(cant):
#     num=int(input("Ingrese un numero: "))
#     if num % 2==0:
#         print("el numero es par")
#         cont=cont+1
#     else:
#         print("el numero es impar")
#         cont2=cont2+1


# print("La cantidad de numeros pares son: ", cont)
# print("La cantidad de numeros impares son: ", cont2)

## terminar
# num=int(input("Ingrese un numero"))
# for i in range(num):
#     if (i+1) % 2==0:
#         print("El numero ", i, " es par" )
#     else:
#         print("El numero ", i, " es impar" )

# deuda=100000

# while True:
#     print(''' 
#      1.- Pago de Tarjeta de Crédito
#      2.- Simulación de Compras
#      3.- Salir

#     ''')
#     while True:
#         try:
#             op=int(input())
#             break
#         except Exception:
#             print("Solo se permiten numeros enteros")
#     match op:
#         case 1:
#             while True:
#                 print(''' 
#                 1.- Ingresar un monto
#                 2.- Salir
#                 ''')
#                 while True:
#                     try:
#                         op=int(input())
#                         break
#                     except Exception:
#                         print("Solo se permiten numeros enteros")
#                 match op:
#                     case 1:
#                         monto=int(input("Ingrese un monto: "))
#                         while monto<0:
#                             print("El monto debe ser mayor o igual a cero")
#                             monto=int(input())
#                         while monto>deuda:
#                             print("El monto excede el saldo actual de la tarjeta")
#                             monto=int(input())
#                         deuda=deuda-monto
#                         print("La deuda actual es: ", deuda)
#                     case 2:
#                         break
#                     case _ :
#                         print("Opción invalida")

#         case 2:
#             while True:
#                 print(''' 
#                 1.- Ingresar monto
#                 2.- Salir

#                 ''')
#                 while True:
#                     try:
#                         op=int(input())
#                         break
#                     except Exception:
#                         print("Solo se permiten numeros enteros")
#                 match op:
#                     case 1:
#                         num=int(input("Ingrese el monto de la compra: "))
#                         while num<0:
#                             print("El monto debe ser mayor o igual a cero")
#                             num=int(input("ingrese el monto de la compra"))
#                         deuda=deuda+num
#                         print("Saldo de la tarjeta: ", deuda)
#                     case 2:
#                         break
#                     case _ :
#                         print("Opción invalida")
                        
#         case 3:
#             break
#         case _ :
#             print("Opción invalida")


def menu2():
    global num, correo
    while True:
                            op=int(input(''' 
                        1.- Realizar llamada
                        2.- Enviar correo electronico
                        3.- Cerrar sesion 
                        '''))
                            match op:
                                case 1:
                                    num=int(input("Ingrese el numero: "))
                                case 2:
                                    correo=str(input("Ingrese el correo: "))
                                case 3:
                                    break
                                case _:
                                    print("Invalido")                                 
                            
usuario1=None
usuario2=None
usuario3=None
contraseña1=None
contraseña2=None
contraseña3=None

while True:
    op=int(input(''' 
        1.- iniciar sesion
        2.- registrar usuario
        3.- salir
            '''))
    match op:
        case 1:
            if usuario1==None:
                print("No hay usuarios")
            elif usuario1!=None:
                usuario=str(input("Ingrese el usuario: "))
                if usuario==usuario1:
                    contraseña=str(input(f"Bienvenido, ingrese la contraseña: "))
                    if contraseña!=contraseña1:
                        print("Contraseña incorrecta")
                    else:
                        print("Bienvenido")
                        menu2()

        case 2:
            if usuario1==None:
                usuario1=str(input("Ingrese el nombre de usuario: "))
                contraseña1=str(input(f"Ingrese la contraseña de {usuario1}: "))
            elif usuario1!=None and usuario2==None:
                usuario2=str(input("Ingrese el nombre de usuario: "))
                contraseña2=str(input(f"Ingrese la contraseña de {usuario2}: "))
            elif usuario2!=None and usuario3==None:
                usuario3=str(input("Ingrese el nombre de usuario: "))
                contraseña3=str(input(f"Ingrese la contraseña de {usuario3}: "))
            else:
                print("No se pueden registrar mas usuarios")


        case 3:
            break
        case 4:
              print(num,correo)
            