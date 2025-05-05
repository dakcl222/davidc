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