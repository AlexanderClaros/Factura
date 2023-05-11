import json

with open('prueba.json', mode='r', encoding='UTF-8') as file:
    datos = json.load(file)

print(datos)