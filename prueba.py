import json
from medidas_letras import medidas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas('prueba.pdf',pagesize=A4)
UNIDADES_MAXIMAS_POR_LINEA = 112
UNIDADES_MAXIMAS_POR_LINEA_NEGRITA = 160
ancho,alto,=A4 

with open('AA23060876.json', mode='r') as file:
    datos = json.load(file)
    
numero_linea = 1
contador_lineas_cada_tabla = 1
unidades_en_linea = 0
texto_liena = ''
posicion = 0
for linea in datos['lineas']:
    # print(linea)
    # print(linea[0])
    for texto in linea[1]:
        contador = 0
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
                    print(texto_liena,'<<<<<<<')
                    numero_linea += 1
                    contador_lineas_cada_tabla += 1
                    texto_liena = ''
                    unidades_en_linea = 0
            else:
                c.drawString(138, alto - (255 + (numero_linea * 12.8 - 10)), texto_liena)
                posicion= numero_linea
                print(texto_liena)
                contador+=1
                numero_linea += 1
                
                contador_lineas_cada_tabla += 1
                unidades_en_linea = unidades_palabra
                texto_liena = palabra + ' '
        c.drawString(70, alto - (255 + (posicion * 12.8 - 10)), linea[0])
    #             if contador_lineas_cada_tabla  > 23:
    #                 break
    #     if contador_lineas_cada_tabla > 23:
    #         break
    # if contador_lineas_cada_tabla > 23:
    #     contador_lineas_cada_tabla = 1
    #     break
c.showPage()
c.save()