import json
from medidas_letras import medidas

with open('AA23060876.json', mode='r') as file:
    datos = json.load(file)

c.setFillColor(aColor='black')
# c.setFont("Helvetica", 7)


UNIDADES_MAXIMAS_POR_LINEA = 112
UNIDADES_MAXIMAS_POR_LINEA_NEGRITA = 160

numero_linea = 1
unidades_en_linea = 0
texto_liena = ''


for linea in datos['lineas']:
    for texto in linea[1]:
        for indice, palabra in enumerate(texto.split(' ')):
            unidades_palabra = 0
            if "&.7/rf" in texto:
                palabra = palabra.replace("&.7/rf>", "")
                c.setFont("Helvetica-Bold", 5.4)
                unidades_por_linea = UNIDADES_MAXIMAS_POR_LINEA_NEGRITA
            else:
                c.setFont("Helvetica", 7)
                unidades_por_linea = UNIDADES_MAXIMAS_POR_LINEA

            for letra in palabra:
                unidades_palabra += medidas[letra]

            if unidades_en_linea + unidades_palabra < unidades_por_linea:
                unidades_en_linea += unidades_palabra
                texto_liena += palabra + ' '

                if palabra == texto.split(' ')[-1]:
                    c.drawString(138, alto - (255 + (numero_linea * 12.8 - 10)), texto_liena)
                    numero_linea += 1
                    texto_liena = ''
                    unidades_en_linea = 0
            else:
                c.drawString(138, alto - (255 + (numero_linea * 12.8 - 10)), texto_liena)
                numero_linea += 1
                unidades_en_linea = unidades_palabra
                texto_liena = palabra + ' '

# numero_tablas = numero_linea // 23
# if numero_linea % 23 != 0:
#     numero_tablas += 1

# print(numero_tablas)