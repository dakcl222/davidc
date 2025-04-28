#Explicacion y uso de while

# #Clave intentos infinitos
# clave=3344
# password=int(input("Ingrese su pass: "))

# while clave!=password:
#     print("error") 
#     password=int(input("Ingrese su pass"))

# print("Bienvenido al sistema")


# #Clave con 3 intentos
# #terminar

# clave=3344
# intentos=0
# password=int(input("Ingrese su pass: "))

# while clave!=password and intentos<3:
#     print("error")
#     intentos=intentos+1
#     password=int(input("Ingrese su pass"))

# if intentos>=3:
#     print("Ya no tiene mas intentos")
# else:
#     print("Bienvenido al sistema")


# while True:
#     print("hello")

# suma=0

# while True:
#     num=int(input("Ingrese un nunmero, cero para salir: "))
#     if num==0:
#         break
#     suma=suma+num
#     print(suma)
# print(f"la suma total es {suma}")

#Pida al usuario el limite inferior y superior de un rango despues genere un numero al azar dentro de ese rango el segundo numero no debe ser menor que el primero 
#pero debe darle la ooportunidad al usuario de ingresar otro

# import random


# num1=int(input("Ingrese el limite inferior: "))
# num2=int(input("Ingrese el limite superior: "))
# while num2<num1:
#     print("El limite superior debe ser mayor al limite inferior, ingrese otro numero: ")
#     num2=int(input("Ingrese el limite superior: "))
# numram=random.randint(num1,num2)
# print(numram)

# import random

# numram=random.randint(1,50)
# print("Adivine el numero: ")
# intentos=5
# n1=int(input())

# while n1!=numram:
#     intentos=intentos-1
#     if intentos==0:
#         break
#     if n1<numram:
#         print("El numero ingresado es menor al numero random")
#         print(f"Te quedan {intentos} intentos")
#         n1=int(input())
#     elif n1>numram:
#         print("El numero ingresado es mayor al numero random")
#         print(f"Te quedan {intentos} intentos")
#         n1=int(input())
# if n1==numram:
#     print("Adivinaste el numero")
# else:
#     print("No adivinaste el numero")

#Street Fighter

#Designe 2 peleadores solicitando sus nombres
#cada peleador tiene 50 hp tiene que mostrar la barra de energia
# las peleas son por turnos
# cada turno el peleador ataca entre 3 y 15
# existe posibilidad de ataque critico del 20%
# gana el que le quita todo  el hp al rival

# import random
# import time

# turno=0
# j1n=str(input("Ingrese el nombre del primer peleador: "))
# j2n=str(input("Ingrese el nombre del segundo peleador: "))
# j1=50
# j2=50

# while j1>0 and j2>0:
#     if turno % 2==0:
#         print(f"turno {j1n}")
#         atk1=random.randint(3,15)
#         crit1=random.randint(1,5)
#         if crit1==1:
#             j2=j2-atk1*2
#             print(f"{j1n} Le dio un golpe critico {atk1*2} a {j2n} ")
#         else:
#             j2=j2-atk1
#             print(f"{j1n} Le quita {atk1} a {j2n}")
#         print(f"Vida de {j2n}")
#         print("/"*j2)
#         turno=turno+1
#         time.sleep(1)
#     else:
#         print(f"Turno {j2n}")
#         atk2=random.randint(3,15)
#         crit2=random.randint(1,5)
#         if crit2==1:
#             j1=j1-atk2*2
#             print(f"{j2n} Le dio un golpe critico {atk1*2} a {j1n}")
#         else:
#             j1=j1-atk2
#             print(f"{j2n} Le quita {atk2} a {j1n}")
#         print(f"Vida de {j1n}")
#         print("/"*j1)
#         turno=turno+1
#         time.sleep(1)
# if j1>0:
#     print(f"Gano {j1n}")
# else:
#     print(f"Gano {j2n}")


#Crear un cajero automatico
#tener en cuenta cajas de billetes de 5000 10000 y 20000
#cada caja tiene 30 billetes verificar el monto solicitado
#Esta disponible en el cajero verificar si el monto solicitado es posible por el multiplo de los billetes
#disponibles
#Al terminar cada transaccion debe mostrar saldo disponible 
#debe haber 3 usuarios cada uno con su saldo correspondiente
#usar clave secreta para iniciar y segun la clave asociar el saldo disponible
#3claves3saldos

pw=str(input("Ingrese su contraseña: "))
if pw==123:
    print("Hola 1")