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
    

#pide la cantidad de alummnos y luego la cantidad de notas por alumnos 
#muestra el promedio de cada uno

cantalumn=int(input("Ingrese la cantidad de alumnos: "))

for i in range(cantalumn):
    print("Ingrese la cantidad de notas del alumno: ", i+1)
    cantnotas=int(input())
    suma=0
    for j in range(cantnotas):
        print("ingrese nota: ", i+1)
        nota=float(input())
        suma+=nota
        prom=suma/cantnotas
        print("El promedio es: ", prom)

