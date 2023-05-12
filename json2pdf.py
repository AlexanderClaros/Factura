from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import json
from medidas_letras import medidas

##############################################
with open('AA23060876.json', mode='r') as file:
    datos = json.load(file)

# c.setFillColor(aColor='black')
# c.setFont("Helvetica", 7)


UNIDADES_MAXIMAS_POR_LINEA = 112
UNIDADES_MAXIMAS_POR_LINEA_NEGRITA = 160

contador_tablas = 1
numero_linea = 1
contador_lineas_cada_tabla = 1
unidades_en_linea = 0
texto_liena = ''

# info_por_tabla = [[]]
# inicializar una lista de listas, donde cada lista tenga 23 elementos

info_tablas = {
    'codigos': 0,
    'descripcion_articulos': [[]],
}

def medida_str(texto):
    unidades_palabra = 0
    for letra in texto:
        unidades_palabra += medidas[letra]
    return unidades_palabra

for linea in datos['lineas']:
    for texto in linea[1]:
        for indice, palabra in enumerate(texto.split(' ')):
            unidades_palabra = 0
            if "&.7/rf" in texto:
                unidades_por_linea = UNIDADES_MAXIMAS_POR_LINEA_NEGRITA
            else:
                unidades_por_linea = UNIDADES_MAXIMAS_POR_LINEA

            if "&.7/rf" in palabra:
                unidades_palabra -= medida_str("&.7/rf>")
            
            unidades_palabra += medida_str(palabra)

            if unidades_en_linea + unidades_palabra < unidades_por_linea:
                unidades_en_linea += unidades_palabra
                texto_liena += palabra + ' '

                if palabra == texto.split(' ')[-1]:
                    info_tablas["descripcion_articulos"][-1].append(texto_liena)
                    numero_linea += 1
                    contador_lineas_cada_tabla += 1
                    texto_liena = ''
                    unidades_en_linea = 0
                    if contador_lineas_cada_tabla == 23:
                        info_tablas["descripcion_articulos"].append([])
                        contador_lineas_cada_tabla = 1
                        contador_tablas += 1

            else:
                info_tablas["descripcion_articulos"][-1].append(texto_liena)
                numero_linea += 1
                contador_lineas_cada_tabla += 1
                unidades_en_linea = unidades_palabra
                texto_liena = palabra + ' '
                if contador_lineas_cada_tabla == 23:
                    info_tablas["descripcion_articulos"].append([])
                    contador_lineas_cada_tabla = 1
                    contador_tablas += 1

codigos = [['' for _ in range(23)] for _ in range(contador_tablas)]

info_tablas["codigos"] = codigos

for linea in datos['lineas']:
    codigo = linea[0]
    if codigo != "" and codigo != " ":
        indice_lista = 0
        indice_elemento = 0
        for indice, lista in enumerate(info_tablas["descripcion_articulos"]):
            for elemento in lista:
                if linea[1][0].startswith(elemento):
                    indice_lista = indice
                    indice_elemento = lista.index(elemento)
                    print(indice_lista,'---',indice_elemento,'----',codigo)
                    break
            print(codigo)
            info_tablas["codigos"][indice_lista][indice_elemento] = codigo


print(info_tablas["codigos"])

# print(codigos)

# print(info_tablas["descripcion_articulos"])
# print(contador_tablas)

##############################################

def writeString(c,x,alto,y,text,size,font='Helvetica-Bold'):
    c.setFont(font,size)
    c.setFillColor(aColor='black')
    c.drawString(x,alto-y,text)
    c.setFillColor(aColor='lightblue')


with open('cabecera_frances.json','r') as archivo:
    contenido = archivo.read()
    cabecera = json.loads(contenido)
     
tipo = cabecera["tipo"]
n_factura = cabecera["n_factura"]
serie = cabecera["serie"]
fecha_factura = cabecera["fecha_factura"]
cod_cl = cabecera["cod_cl"]
cif_dni = cabecera["cif_dni"]
alm = cabecera["alm"]
vendedor = cabecera["vendedor"]
ext_centralita = cabecera["ext_centralita"]
enviar_a = cabecera["enviar_a"]
factura_a = cabecera["factura_a"]
codigo = cabecera["codigo"]
desc_art = cabecera["desc_art"]
garantia = cabecera["garantia"]
ud = cabecera["ud"]
precio = cabecera["precio"]
dto = cabecera["dto"]
neto = cabecera["neto"]
importes = cabecera["importes"]
importe = cabecera["importe"]
irpf = cabecera["irpf"]
retencion = cabecera["retencion"]
transporte = cabecera["transporte"]
imponible = cabecera["imponible"]
por_iva = cabecera["por_iva"]
iva = cabecera["iva"]
por_eqv = cabecera["por_eqv"]
equivalencia = cabecera["equivalencia"]
t_factura = cabecera["t_factura"]
pago = cabecera["pago"]
c_c = cabecera["c_c"]
p_realizados = cabecera["p_realizados"]
f_ven = cabecera["f_ven"]
importes2 = cabecera["importes2"]
r_financiero = cabecera["r_financiero"]
total = cabecera["total"]
dat_banco = cabecera["dat_banco"]
swift = cabecera["swift"]
iban = cabecera["iban"]
c_c2 = cabecera["c_c2"]
text_aten1 = cabecera["text1_atencion"]
text_aten2= cabecera["text2_atencion"]
fecha =cabecera['fecha']
recopilacion =cabecera['recopilacion']
admisible =cabecera['admisible']
p_formulario =cabecera['p_formulario']
ancho,alto,=A4
titulo=8
negrita=5.8
normal=7
print (alto,ancho)
c = canvas.Canvas('factura.pdf',pagesize=A4)
numero=3  
final=False
for numero_tabla in range(numero):
    if numero_tabla<4:
        c.setFillColor(aColor='lightblue')
        c.setStrokeColor(aColor='gray')
        #nombre documento
        c.roundRect(60,alto-114,170,20,3,stroke=1 ,fill=0)
        c.roundRect(60,alto-114,171,20,3,stroke=1 ,fill=0)
        writeString(c,115,alto,110,tipo,15)
        # cuadro datos factura
        c.roundRect(60,alto-159,262,44,0,stroke=1,fill=0)
        c.roundRect(60,alto-160,263,45,0,stroke=1,fill=0)
        c.roundRect(60,alto-159,262,14,0,stroke=1,fill=0)
        c.roundRect(60,alto-129,262,14,0,stroke=1,fill=1)
        c.roundRect(60,alto-159,45,14,0,stroke=1,fill=1)
        c.roundRect(210,alto-159,85,14,0,stroke=1,fill=1)
        c.rect(122,alto-145,0,30)
        c.rect(147,alto-145,0,30)
        c.rect(205,alto-145,0,30)
        c.rect(242,alto-145,0,30)
        c.rect(300,alto-145,0,30)
        writeString(c,65,alto,125,n_factura,titulo)
        writeString(c,123,alto,125,serie,titulo)
        writeString(c,148,alto,125,fecha_factura,titulo)
        writeString(c,205,alto,125,cod_cl,titulo)
        writeString(c,245,alto,125,cif_dni,titulo)
        writeString(c,302,alto,125,alm,titulo)
        writeString(c,63,alto,155,vendedor,titulo)
        writeString(c,213,alto,155,ext_centralita,titulo)
        # cuadro envio
        c.roundRect(60,alto-222,262,48,0,stroke=1,fill=0)
        c.roundRect(60,alto-223,263,49,0,stroke=1,fill=0)
        writeString(c,60,alto,170,enviar_a,titulo)

        # cuadro datos de remitente
        c.roundRect(350,alto-125,205,73,0,stroke=1,fill=0)
        c.roundRect(350,alto-126,206,74,0,stroke=1,fill=0)
        # cuadro datos de destinatario
        c.roundRect(350,alto-222,205,80,0,stroke=1,fill=0)
        c.roundRect(350,alto-223,206,81,0,stroke=1,fill=0)
        writeString(c,350,alto,138,factura_a,titulo)
        writeString(c,520,alto,138,'Pag. ',titulo,'Helvetica')
        # cuadro de la tabla
        c.roundRect(60,alto-560,520,330,0,stroke=1,fill=0)
        c.roundRect(60,alto-244,520,14,0,stroke=1,fill=1)
        c.roundRect(60,alto-560,520,14,0,stroke=1,fill=0)
        c.roundRect(365,alto-560,37,14,0,stroke=1,fill=1)
        c.rect(136,alto-560,0,330)
        c.rect(328,alto-560,0,330)
        c.rect(365,alto-560,0,330)
        c.rect(402,alto-560,0,330)
        c.rect(447,alto-560,0,330)
        c.rect(478,alto-560,0,330)
        c.rect(523,alto-560,0,330)
        writeString(c,65,alto,240,codigo,titulo)
        writeString(c,190,alto,240,desc_art,titulo)
        writeString(c,330,alto,240,garantia,titulo)
        writeString(c,370,alto,240,ud,titulo)
        writeString(c,410,alto,240,precio,titulo)
        writeString(c,448,alto,240,dto,titulo)
        writeString(c,490,alto,240,neto,titulo)
        writeString(c,535,alto,240,importes,titulo)
        ##############################################
        # with open('AA23060876.json', mode='r') as file:
        #     datos = json.load(file)

        # c.setFillColor(aColor='black')
        # # c.setFont("Helvetica", 7)


        # UNIDADES_MAXIMAS_POR_LINEA = 112
        # UNIDADES_MAXIMAS_POR_LINEA_NEGRITA = 160

        # numero_linea = 1
        # contador_lineas_cada_tabla = 1
        # unidades_en_linea = 0
        # texto_liena = ''


        # for linea in datos['lineas']:
        #     for codigo in linea[0]:
        #         pass
        #     for texto in linea[1]:
        #         for indice, palabra in enumerate(texto.split(' ')):
        #             unidades_palabra = 0
        #             if "&.7/rf" in texto:
        #                 palabra = palabra.replace("&.7/rf>", "")
        #                 c.setFont("Helvetica-Bold", 5.4)
        #                 unidades_por_linea = UNIDADES_MAXIMAS_POR_LINEA_NEGRITA
        #             else:
        #                 c.setFont("Helvetica", 7)
        #                 unidades_por_linea = UNIDADES_MAXIMAS_POR_LINEA

        #             for letra in palabra:
        #                 unidades_palabra += medidas[letra]

        #             if unidades_en_linea + unidades_palabra < unidades_por_linea:
        #                 unidades_en_linea += unidades_palabra
        #                 texto_liena += palabra + ' '

        #                 if palabra == texto.split(' ')[-1]:
        #                     c.drawString(138, alto - (255 + (numero_linea * 12.8 - 10)), texto_liena)
        #                     numero_linea += 1
        #                     contador_lineas_cada_tabla += 1
        #                     texto_liena = ''
        #                     unidades_en_linea = 0
        #             else:
        #                 c.drawString(138, alto - (255 + (numero_linea * 12.8 - 10)), texto_liena)
        #                 numero_linea += 1
        #                 contador_lineas_cada_tabla += 1
        #                 unidades_en_linea = unidades_palabra
        #                 texto_liena = palabra + ' '
        #                 if contador_lineas_cada_tabla  > 23:
        #                     break
        #         if contador_lineas_cada_tabla > 23:
        #             break
        #     if contador_lineas_cada_tabla > 23:
        #         contador_lineas_cada_tabla = 1
        #         break
        ################################################
        if numero_tabla!=numero - 1:
            c.showPage()
    final=True
if numero_tabla<4 and final==True:
    # texto de Atencion
    writeString(c,90,alto,570,text_aten1,6)
    writeString(c,90,alto,579,text_aten2,6)

    # cuadro de total factura
    c.roundRect(60,alto-624,520,30,0,stroke=1,fill=0)
    c.roundRect(60,alto-625,521,31,0,stroke=1,fill=0)
    c.roundRect(60,alto-608,520,14,0,stroke=1,fill=1)
    c.roundRect(496,alto-624,84,16,0,stroke=1,fill=1)
    c.rect(112,alto-624,0,30)
    c.rect(159,alto-624,0,30)
    c.rect(206,alto-624,0,30)
    c.rect(258,alto-624,0,30)
    c.rect(320,alto-624,0,30)
    c.rect(351,alto-624,0,30)
    c.rect(403,alto-624,0,30)
    c.rect(434,alto-624,0,30)
    c.rect(496,alto-624,0,30)
    writeString(c,65,alto,603,importe,titulo)
    writeString(c,120,alto,603,irpf,titulo)
    writeString(c,165,alto,603,retencion,titulo)
    writeString(c,210,alto,603,transporte,titulo)
    writeString(c,265,alto,603,imponible,titulo)
    writeString(c,322,alto,603,por_iva,titulo)
    writeString(c,380,alto,603,iva,titulo)
    writeString(c,405,alto,603,por_eqv,titulo)
    writeString(c,435,alto,603,equivalencia,titulo)
    writeString(c,525,alto,603,t_factura,titulo)
    # cuadro de importes
    c.roundRect(285,alto-663,100,30,0,stroke=1,fill=0)
    c.roundRect(285,alto-664,101,31,0,stroke=1,fill=0)
    c.roundRect(285,alto-647,100,14,0,stroke=1,fill=1)
    c.rect(328,alto-663,0,30)
    writeString(c,288,alto,644,f_ven,titulo)
    writeString(c,335,alto,644,importes2,titulo)
    # cuadro de total
    c.roundRect(395,alto-663,182,30,0,stroke=1,fill=0)
    c.roundRect(395,alto-664,183,31,0,stroke=1,fill=0)
    c.roundRect(523,alto-663,54,16,0,stroke=1,fill=1)
    c.roundRect(395,alto-647,182,14,0,stroke=1,fill=1)
    c.rect(446,alto-663,0,30)
    c.rect(523,alto-663,0,30)
    writeString(c,450,alto,644,r_financiero,titulo)
    writeString(c,530,alto,644,total,titulo)
    # cuadro de datos bancarios
    c.roundRect(290,alto-684,290,14,0,stroke=1,fill=1)
    c.roundRect(290,alto-696,290,12,0,stroke=1,fill=0)
    c.roundRect(290,alto-708,290,12,0,stroke=1,fill=0)
    c.roundRect(290,alto-720,290,12,0,stroke=1,fill=0)
    c.roundRect(290,alto-732,290,12,0,stroke=1,fill=0)
    c.roundRect(290,alto-733,291,63,0,stroke=1,fill=0)
    c.rect(392,alto-732,0,62)
    c.rect(446,alto-732,0,62)
    c.rect(471,alto-732,0,62)
    writeString(c,295,alto,680,dat_banco,titulo)
    writeString(c,398,alto,680,swift,titulo)
    writeString(c,450,alto,680,iban,titulo)
    writeString(c,476,alto,680,c_c,titulo)
    # cuadros de forma de pago
    c.roundRect(60,alto-653,205,17,3,stroke=1,fill=1)
    c.roundRect(60,alto-653.5,205.5,17.5,3,stroke=1,fill=0)
    writeString(c,65,alto,643,pago,6)
    writeString(c,65,alto,650,c_c2,6)
    c.roundRect(60,alto-684,205,25,3,stroke=1,fill=1)
    c.roundRect(60,alto-684.5,205.5,25.5,3,stroke=1,fill=0)
    c.roundRect(60,alto-700,205,10,3,stroke=1,fill=0)
    c.roundRect(60,alto-700.5,205.5,10.5,3,stroke=1,fill=0)
    writeString(c,110,alto,697,p_realizados,6)
    
    c.roundRect(60,alto-713,225,8,0,stroke=1,fill=1)
    c.roundRect(60,alto-732,225,27,0,stroke=1,fill=0)
    c.roundRect(60,alto-733,226,28,0,stroke=1,fill=0)
    c.rect(99,alto-732,0,27)
    c.rect(128,alto-732,0,27)
    c.rect(170,alto-732,0,27)
    c.rect(207,alto-732,0,27)
    writeString(c,62,alto,711,recopilacion,5)
    writeString(c,102,alto,711,fecha,5)
    writeString(c,130,alto,711,recopilacion,5)
    writeString(c,172,alto,711,admisible,5)
    writeString(c,210,alto,711,p_formulario,5)


c.save()
