#for

# print("Ingrese un numero")
# rep=int(input())
# for i in range(rep):
#     print("repetición", i+1)

#Pide un numero y muestra la tabla de ese numero hasta el 10

# num=int(input("Ingrese un numero: "))
# for i in range(10):
#     print( num, "x", i+1, "=", (i+1)*num)


# #auto tabla 1-10

# for j in range(10):
#     for i in range(10):
#         print(j+1, "x", i+1, "=", (i+1)*(j+1))

# #pide cantidad de notas y muestra el promedio

# print("Cuantas notas son?")
# numnotas=int(input())

# suma=0
# for i in range(numnotas):
#     print("Ingrese nota: ", i+1)
#     nota=int(input())
#     suma=suma+nota

# prom=suma/numnotas
# print("el promedio es: ", prom)
    

# #pide la cantidad de alummnos y luego la cantidad de notas por alumnos 
# #muestra el promedio de cada uno

# cantalumn=int(input("Ingrese la cantidad de alumnos: "))

# for i in range(cantalumn):
#     print("Ingrese la cantidad de notas del alumno: ", i+1)
#     cantnotas=int(input())
#     suma=0
#     for j in range(cantnotas):
#         print("ingrese nota: ", i+1)
#         nota=float(input())
#         suma+=nota
#         prom=suma/cantnotas
#         print("El promedio es: ", prom)

# #pide un nmero y suma todos los digitos desd el 1 hasta ese numero mostrando la suma

# num=int(input("Ingrese un numero: "))
# suma=0
# for i in range(num):
#     suma+=i+1
# print("La suma de los numeros es: ", suma)

# #pedir la cantidad de nuemeros y verifique cada uno si es par o impar

# #par impar
# cantnum=int(input("Ingrese la cantidad de numeros "))

# for i in range(cantnum):
#     print("Ingrese un numero: ")
#     num=int(input())
#     if num % 2==0:
#         print("el numero: ", num, " Es par")
#     else:
#         print("el numero: ", num, " Es impar")

# #2 candidatos, pedir cantidad de votantes y mostrar el resultado

# nvotantes=int(input("Ingrese el numero de votantes: "))

# v1=0
# v2=0

# for i in range(nvotantes):
#     voto=int(input("Ingrese su voto 1 o 2: "))
#     if voto==1:
#         v1=v1+1
#     elif voto==2:
#         v2=v2+1
#     else:
#         print("Ingrese un voto valido")

# print("Los votos de v1 Son: ", v1)
# print("Los votos de v2 son: ", v2)

# if v1>v2:
#     print("gano v1")
# elif v1==v2:
#     print("Empate")
# else:
#     print("gano v2")

# pa=str(input())
# cont=0
# c=0
# cons=0
# for i in pa:
#     print(i)
#     c=c+1
#     if i.lower() in "aeiou":
#         cont=cont+1
#     elif i.lower() in " ":
#         cons=cons-1
#         c=c-1
#     else:
#         cons=cons+1

# print("La cantidad de vocales es: ", cont)
# print("La cantidad de caracteres es: ", c)
# print("La cantidad de consonantes es: ", cons)

# #supermercado
# cant=int(input("Ingrese la cantidad de productos: "))
# total=0

# for i in range(cant):
#     print("Que productos llevara?")
#     print("1.- Diazepam $9000")
#     print("2.- Metametozona $18500")
#     print("3.- Oblea china $1000")
#     op=int(input())
#     if op==1:
#         print("Usted lleva Diazepam")
#         total=total+9000
#     elif op==2:
#         print("Usted lleva Metametozona")
#         total=total
#     elif op==3:
#         print("Usted lleva Oblea china")
#         total=total+1000
#     else:
#         print("hola")

# print("El total neto es:", total)
# print("El total mas IVA es: ", total*1.19)

# #Perros de caza
# #Pide al usuario la cantidad de perros
# #Muestre cual es la cuota minima de conejos
# #Luego consulte cuantos conejos trajo?
# #Si el perro trajo la cantidad minima
# # Cumplio la cuota, si no, se queda sin filete
# #Mostrar resumen de perros que cumplieron y los que no

# import random

# sic=0
# noc=0

# crandom=random.randint(1,5)
# while True:    
#     try:
#         cant=int(input("Ingrese el numero de perros:"))
#         break
#     except Exception:
#         print("Solo se aceptan numeros enteros")

# for i in range(cant):
#     print("La cuota minima de conejos es ",crandom,".")
#     print("Cuantos conejos trajo el perro numero",i+1,"?")
#     nconejos=int(input())
#     if nconejos<crandom:
#         print("El perro no cumplio con la cuota, se quedo sin filete")
#         noc=noc+1
#     else:
#         print("El perro cumplio con la cuota, se gana un filete")
#         sic=sic+1
        
# print("Cantidad de perros que cumplieron: ", sic)
# print("Cantidad de perros que no cumplieron: ", noc)

# #Quiere pasar el ramo?
# #Pregunte la cantidad de rojos en el curso
# #los talleres que hay en el semestre son 4
# #Por cada taller asistido obtiene 0.3 decimas
# # si el alumno tiene mas de 1 punto
# # tiene la bendicion del profesor
# #si no, no se le puede ayudar
# #ingrese la nota final y sume las decimas acumuladas.
# #Muestre si aprueba o reprueba.

# decimas=0
# rojos=int(input("Ingrese la cantidad de rojos: "))
# asiste=int(input("A cuantos talleres asistio?: "))
# decimas=decimas+0.3*asiste
# print("Usted tiene", decimas,"decimas")
# if decimas>1:
#     print("Tiene la bendicion del profesor")
# else:
#     print("No se le puede ayudar")

# nfinal=float(input("Ingrese la nota final: "))
# nfinal=nfinal+decimas

# if nfinal>4.0:
#     print("Aprueba")
# else:
#     print("Reprueba")


#Lavado de autos
#Crear un menu para lavar autos
#1.- Cursar pago del lavado
#2.- Ver ventas diarias.
#3.- Salir
#El lavado tiene 3 niveles
#1.- Full $15000 2.- standard $10000 3.- basico $7000
#Al mostrar las ventas diarias, debe mostrar la
#Cantidad de autos que han ingresado y el monto total
#Recaudado. tambien debe mostrar el monto mas alto pagado

total=0
cautos=0
full=0
standard=0
basico=0

while True:
    print(''' 
    1.- Cursar pago del lavado
    2.- Ver ventas diarias
    3.- Salir
        ''')
    op=int(input())
    match op:
        case 1:
            print(''' 
        1.- Full $15000
        2.- Standard $10000
        3.- Basico $7000 
        4.- Salir         

            ''')
            op=int(input())
            match op:
                case 1:
                    total=total+15000
                    cautos=cautos+1
                    full=10
                case 2:
                    total=total+10000
                    cautos=cautos+1
                    standard=5
                case 3:
                    total=total+7000
                    cautos=cautos+1
                    basico=1
                case 4:
                    break
                case _ :
                    print("invalido")
                    
        case 2:
            print("Cantidad de autos: ", cautos)
            print("Total recaudado: ", total)
            if full>=1:
                print("El monto mas alto pagado fue 15.000")
            elif standard>full:
                print("El monto mas alto pagado fue 10.000")
            elif basico>standard and basico>full:
                print("El monto mas alto pagado fue 7.000")
        case 3:
            break
        case _ :
            print("Invalido")





