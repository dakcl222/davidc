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


# #Crear un cajero automatico
# #tener en cuenta cajas de billetes de 5000 10000 y 20000
# #cada caja tiene 30 billetes verificar el monto solicitado
# #Esta disponible en el cajero verificar si el monto solicitado es posible por el multiplo de los billetes
# #disponibles
# #Al terminar cada transaccion debe mostrar saldo disponible 
# #debe haber 3 usuarios cada uno con su saldo correspondiente
# #usar clave secreta para iniciar y segun la clave asociar el saldo disponible
# #3claves3saldos

# saldo1=7500
# saldo2=10000
# saldo3=20000
# b5=5000*30
# b10=10000*30
# b20=20000*30

# pw=str(input("Ingrese su contraseña: "))
# if pw==111:
#     print("Hola 1")
#     monto=str(input("Ingrese el monto"))
#     if monto>saldo1:
#         print("no hay saldo")
#     elif monto==5000:

# elif pw==222:
#     print("hola 2")
#     monto=str(input("Ingrese el monto"))
# elif pw==333:
#     print("hola 3")
#     monto=str(input("Ingrese el monto"))
# else:
#     print("clave incorrecta")

# #La florida 20% ,la pintana 30%, puente alto 25%, san joaquin 25%
# #Grupo familiar: 1-->2%, 2 a 4 -> 3%, 5 o mas -> 4%
# # preguntar al usuario en que comuna vive
# # pregunar al ausuario con cuantas personas vive
# # el arancel actual es de 200.000 por semestre
# # basados en las respuestas del usuario y en
# # la informaicon dada, calcular su descuento

# #terminar XDDDDDDDDDDDDDD


# descuento=1
# arancel=200000
# print("Comunas disponibles: La florida, La pintana, Puente alto, San joaquin")
# comuna=str(input("Ingrese su comuna: "))
# personas=int(input("Con cuantas personas vive?: "))
# if comuna.lower()=="la florida":
#     descuento=descuento-0.20
# elif comuna.lower()=="la pintana":
#     descuento=descuento-0.30
# elif comuna.lower()=="puente alto":
#     descuento=descuento-0.25
# elif comuna.lower()=="san joaquin":
#      descuento=descuento-0.25
# if personas==1:
#     descuento=descuento-0.02
# elif personas>=2 and personas<=4:
#     descuento=descuento-0.03
# elif personas>=5:
#     descuento=descuento-0.04

# print(f"El total a pagar es:", round(arancel*descuento,1))


# #Clasificar segun categoria y precio
# # Cat 1 +200, Cat 2 +400, Cat 3 +600
# #Precios : 1000 y menos 3%, entre 1001 y 5000 5%, 5001 y mas 6%
# #Poner listado de 3 productos por categoria, las cat son 1 2 y 3
# #Agregar los impuests al precio, segun la cat y luego
# #aplicar descuentos al total de la boleta segun el monto
# descuento=0
# total=0

# cat=int(input("Ingrese la categoria 1,2,3: "))
# if cat==1:
#     print("Categoria 1: ")
#     print("Producto 1: cat1, 1000 +200")
#     print("Producto 2: cat1, 2500 +200")
#     print("Producto 3: cat1, 3500 +200")
#     op=int(input("Ingrese la opcion"))
#     if op==1:
#         total=total+1000+200
#     elif op==2:
#         total=total+2500+200
#     elif op==3:
#         total=total+3500+200
# elif cat==2:
#     print("Categoria 2: ")
#     print("Producto 4: cat1, 1000 +400")
#     print("Producto 5: cat1, 2500 +400")
#     print("Producto 6: cat1, 3500 +400")
#     op=int(input("Ingrese la opcion"))
#     if op==1:
#         total=total+1000+400
#     elif op==2:
#         total=total+2500+400
#     elif op==3:
#         total=total+3500+400
# elif cat==3:
#     print("Categoria 3: ")
#     print("Producto 7: cat3, 1000 +600")
#     print("Producto 8: cat3, 2500 +600")
#     print("Producto 9: cat3, 3500 +600")
#     op=int(input("Ingrese la opcion"))
#     if op==1:
#         total=total+1000+600
#     elif op==2:
#         total=total+2500+600
#     elif op==3:
#         total=total+3500+600

# if total<=1000:
#     total=total*0.97
# elif total<=1001 and total>=500:
#     total=total*0.95
# elif total<=5001:
#     total=total*0.94

# print(f"el total es:{total} ")

# flag1=True
# flag2=False
# if flag1 and flag2:
#     flag1,flag2= False, True
# elif not flag2 and flag1:
#     flag2,flag1=False,False
#     if not flag1 and flag2:
#         flag1,flag2=True,False
#     elif not flag1 and not flag2:
#         flag1,flag2=True,True

# print(flag1, flag2)


# num1=1
# num2,num3=1, 1
# num3=num3+1
# if num1+num2==num3:
#     print("igual")
# else:
#     print("diferente")


# #calcular el puntaje de credito
# #____ calcular que tanto credito tiene una persona
# #en cierta entidad financiera, debera considerar
# #cantidad de ingresos, nivel educacional y nacionailidad
# #cantidad de ingresos
# #500.000 a 1.000.000 : 300.000
# #1.000.000 a 1.500.000 : 650.000
# #1.500.000 o mas: 1.000.000
# #Nivel educacional
# #Basico: x1, medio:x1,3 , superior: x1,5
# #Nacionalidad
# #Chilena: +300.000, Extranjero: +0

# credito=0
# cingresos=0
# niveledu="hola"
# nacionalidad="hola"
# cingresos=int(input("Ingrese la cantidad de ingresos: "))
# niveledu=str(input("Ingrese su nivel educacional Basico, Medio, Superior:")).lower()
# nacionalidad=str(input("Ingrese su nacionalidad: ")).lower()


# if cingresos>=500000 and cingresos<=1000000:
#     credito=credito+300000
# elif cingresos>=1000000 and cingresos<=1500000:
#     credito=credito+650000
# elif cingresos>=1500000:
#     credito=credito+1000000

# if niveledu=="Medio".lower():
#     credito=credito*1.3
# elif niveledu=="Superior".lower():
#     credito=credito*1.5

# if nacionalidad=="Chilena".lower():
#     credito=credito+300000

# print("Su credito es: ", credito)


# #pida al usuario 2 digitos verificando si el seguno sea mayor
# # genere un nuemro aleatorio entre esos digitos 
# # imprima la cantida de veecs el simbolo ▄ alt+220 

# import random

# num1=int(input("Ingrese el primer numero: "))
# num2=int(input("Ingrese el segundo numero: "))

# while num2<=num1:
#     print("El segundo numero debe ser mayor al primero")
#     num2=int(input("Ingrese el segundo numero: "))

# cant=random.randint(num1,num2)
# print("▄"*cant)

#Crear un programa que pida la cantidad de ramos
#Luego pida el promedio por cada materia 
#Basados en su promedio final, aplicar puntaje de beneficios 
#4.5 y 5: 300, 5.1 y 6.0: 500, 6.1 y 7: 800
#Agregar puntaje segun carrera
#Tecnico: +60, Ingenieria: +40, Diplomado: +20

beneficios=0
suma=0
ramos=int(input("Ingrese la cantidad de ramos: "))
for i in range(ramos):
    print("Ingrese el promedio del ramo: ", i+1," ")
    prom=int(input())
    suma=suma+prom

promfinal=suma/ramos

if promfinal>=4.5 and promfinal<=5:
    beneficios=beneficios+300
elif promfinal>=5.1 and promfinal<=6.0:
    beneficios=beneficios+500
elif promfinal>=6.1 and promfinal <=7:
    beneficios=beneficios+800

carrera=str(input("Ingrese Carrera: Tecnico, Ingenieria, Diplomado: ")).lower()

if carrera=="tecnico".lower():
    beneficios=beneficios+60
elif carrera=="ingenieria".lower():
    beneficios=beneficios+40
elif carrera=="diplomado".lower():
    beneficios=beneficios+20

print(f"Promedio: ", promfinal, "Beneficio: ", beneficios)


