# dic={"nombre": "Diego",
#      "numero": 79873432,
#      "casado": True
#      }
# print(dic)
# dic["ciudad"]="santiago"
# print(dic)

# for key, value in dic.items():
#     print(key, value)

# #print(value)

# print(dic["numero"])

# personas=[{"nombre": "Diego",
#      "numero": 7777777,
#      "casado": False
#      },
#      {"nombre": "hola",
#      "numero": 888888,
#      "casado": True
#      },
#      {"nombre": "adios",
#      "numero": 99999,
#      "casado": False
#      }]

# print(personas[2]["numero"])


# text=input("Ingrese un texto: ")

# pala=input(" ")




lista=[{"producto": "hola", "precio": 5000},
       {"producto": "hola2", "precio": 6000},
       {"producto": "hola3", "precio": 7000},
       ]
# print(lista[0]["producto"])

# for i in lista:
#     print(i)

# for p,c in enumerate(lista):
#     print(p,c[0]["producto"],c[0]["precio"])

contador=0
for  i in lista:
    print(contador+1,".-",lista[contador]["producto"],lista[contador]["precio"])
    contador=contador+1