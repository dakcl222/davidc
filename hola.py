# nombre="diego"
# edad=64


# print("hola ", nombre, "su edad es", edad)

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


#Ingresar 3 numeros y mostrar el mayor de los 3 

n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el tercer numero: "))

if n1>n2 and n1>n3:
    print("El numero mayor es: ", n1)
elif n2>n1 and n2>n3:
    print("El numero mayor es: ", n2)
elif n3>n1 and n3>n2:
    print("El numero mayor es: ", n3)
    
