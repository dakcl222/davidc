dic={"nombre": "Diego",
     "numero": 79873432,
     "casado": True
     }
print(dic)
dic["ciudad"]="santiago"
print(dic)

for key, value in dic.items():
    print(key, value)

#print(value)

print(dic["numero"])

personas=[{"nombre": "Diego",
     "numero": 7777777,
     "casado": False
     },
     {"nombre": "hola",
     "numero": 888888,
     "casado": True
     },
     {"nombre": "adios",
     "numero": 99999,
     "casado": False
     }]

print(personas[2]["numero"])


text=input("Ingrese un texto: ")

pala=input(" ")