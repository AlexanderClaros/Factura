from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import fitz
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
ancho,alto,=A4
print (alto,ancho)
c = canvas.Canvas('factura.pdf',pagesize=A4)
c.setFillColor(aColor='lightblue')
#nombre documento
c.roundRect(60,alto-114,170,20,3,stroke=1 ,fill=0)
# cuadro datos factura
c.roundRect(60,alto-159,262,44,0,stroke=1,fill=0)
c.roundRect(60,alto-159,262,14,0,stroke=1,fill=0)
c.roundRect(60,alto-129,262,14,0,stroke=1,fill=1)
c.roundRect(60,alto-159,45,14,0,stroke=1,fill=1)
c.roundRect(210,alto-159,85,14,0,stroke=1,fill=1)
c.rect(122,alto-145,0,30)
c.rect(147,alto-145,0,30)
c.rect(205,alto-145,0,30)
c.rect(242,alto-145,0,30)
c.rect(300,alto-145,0,30)
# cuadro envio
c.roundRect(60,alto-222,262,48,0,stroke=1,fill=0)
# cuadro datos de remitente
c.roundRect(350,alto-125,205,73,0,stroke=1,fill=0)
# cuadro datos de destinatario
c.roundRect(350,alto-222,205,80,0,stroke=1,fill=0)
# cuadro de la tabla
c.roundRect(60,alto-560,520,330,0,stroke=1,fill=0)
c.roundRect(60,alto-244,520,14,0,stroke=1,fill=1)   # cabecera de la tabla
c.roundRect(60,alto-560,520,14,0,stroke=1,fill=0)
c.rect(136,alto-560,0,330)
c.rect(328,alto-560,0,330)
c.rect(365,alto-560,0,330)
c.rect(402,alto-560,0,330)
c.rect(447,alto-560,0,330)
c.rect(478,alto-560,0,330)
c.rect(523,alto-560,0,330)
# cuadro de total factura
c.roundRect(60,alto-625,520,30,0,stroke=1,fill=0)
c.roundRect(60,alto-610,520,15,0,stroke=1,fill=1)
# cuadro de importes
c.roundRect(290,alto-663,100,30,0,stroke=1,fill=0)
c.roundRect(290,alto-648,100,15,0,stroke=1,fill=1)
# cuadro de total
c.roundRect(410,alto-663,170,30,0,stroke=1,fill=0)
c.roundRect(410,alto-648,170,15,0,stroke=1,fill=1)
# cuadro de datos bancarios
c.roundRect(290,alto-682,290,15,0,stroke=1,fill=1)
c.roundRect(290,alto-694,290,12,0,stroke=1,fill=0)
c.roundRect(290,alto-706,290,12,0,stroke=1,fill=0)
c.roundRect(290,alto-718,290,12,0,stroke=1,fill=0)
c.roundRect(290,alto-730,290,12,0,stroke=1,fill=0)
# cuadros de forma de pago
c.roundRect(60,alto-655,205,17,3,stroke=1,fill=1)
c.roundRect(60,alto-685,205,25,3,stroke=1,fill=1)
c.roundRect(60,alto-700,205,10,3,stroke=1,fill=0)

#############################
# c.setFillColor(aColor='black')
# c.setFont("Helvetica", 7.5)

# c.drawString(138,alto-255,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

# c.drawString(138,alto-265,"PROGRAMA TPV PELUQUERIAS Y ESTETICA OTRO")

# c.setFont("Helvetica-Bold", 5.8)
# c.drawString(138,alto-305,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
# c.drawString(138,alto-295,"CNB1R2JCVK CNB1R2JCVJ CNB1R2JCVH CNB1R2JCVF CNB1R2J")

##############################
# "pedido": "Pedido nº 23BVU1, Albaran nº 23BLOH de 09/05/2023 (XPO LOGISITICS)",
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





# c.drawString(138,alto-255,datos["pedido"])
# c.drawString(138,alto-265,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

##############################

c.showPage()
c.save()