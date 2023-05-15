from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import json
from medidas_letras import medidas
from barcode import *
from barcode.writer import ImageWriter


##############################################
with open('AA23060876.json', mode='r') as file:
    datos = json.load(file)


def check0 (dato):
    if dato<1:
        return ''
    else:
        return str(dato)
UNIDADES_MAXIMAS_POR_LINEA = 112
UNIDADES_MAXIMAS_POR_LINEA_NEGRITA = 125

contador_tablas = 1
numero_linea = 1
contador_lineas_cada_tabla = 1
unidades_en_linea = 0
texto_liena = ''

info_tablas = {
    'codigos': [[]],
    'descripcion_articulos': [[]],
    'garantias': [[]],
    'unidades': [[]],
    'precios': [[]],
    'descuentos': [[]],
    'netos': [[]],
    'importes': [[]],
}

def medida_str(texto):
    unidades_palabra = 0
    for letra in texto:
        unidades_palabra += medidas[letra]
    return unidades_palabra

def obtener_codigo(linea, texto_liena):
    if linea[1].startswith(texto_liena[:-1]) and linea[0] != '' and linea[0] != ' ':
        info_tablas["codigos"][-1].append(linea[0])
    else:
        info_tablas["codigos"][-1].append('')

def obtener_garantia(linea, texto_liena):
    if linea[1].startswith(texto_liena[:-1]) and linea[2] != '' and linea[2] != ' ':
        info_tablas["garantias"][-1].append(linea[2])
    else:
        info_tablas["garantias"][-1].append('')

def obtener_unidades(linea, texto_liena):
    if linea[1].startswith(texto_liena[:-1]) and linea[3] != 0:
        numero_formateado = "{:.2f}".format(linea[3])
        info_tablas["unidades"][-1].append(numero_formateado)
    else:
        info_tablas["unidades"][-1].append('')

def obtener_precios(linea, texto_liena):
    if linea[1].startswith(texto_liena[:-1]) and linea[4] != 0:
        numero_formateado = "{:.3f}".format(linea[4])
        info_tablas["precios"][-1].append(numero_formateado)
    else:
        info_tablas["precios"][-1].append('')

def obtener_descuentos(linea, texto_liena):
    if linea[1].startswith(texto_liena[:-1]) and linea[5] != 0:
        numero_formateado = "{:.2f}".format(linea[5])
        info_tablas["descuentos"][-1].append(numero_formateado)
    else:
        info_tablas["descuentos"][-1].append('')

def obtener_netos(linea, texto_liena):
    if linea[1].startswith(texto_liena[:-1]) and linea[6] != 0:
        numero_formateado = "{:.3f}".format(linea[6])
        info_tablas["netos"][-1].append(numero_formateado)
    else:
        info_tablas["netos"][-1].append('')

def obtener_importes(linea, texto_liena):
    if linea[1].startswith(texto_liena[:-1]) and linea[7] != 0:
        numero_formateado = "{:.3f}".format(linea[7])
        info_tablas["importes"][-1].append(numero_formateado)
    else:
        info_tablas["importes"][-1].append('')


for linea in datos['lineas']:
    linea[1]=''.join(linea[1])
    if "&.7/rf" in linea[1]:
        linea[1]="&.8/rf"+linea[1]
        linea[1]= linea[1].replace("&.7/rf>", ' ')
    for indice, palabra in enumerate(linea[1].split(' ')):
        unidades_palabra = 0
        if "&.8/rf" in linea[1]:
            unidades_por_linea = UNIDADES_MAXIMAS_POR_LINEA_NEGRITA
        else:
            unidades_por_linea = UNIDADES_MAXIMAS_POR_LINEA

        if "&.8/rf" in palabra:
            unidades_palabra -= medida_str("&.8/rf")
        
        unidades_palabra += medida_str(palabra)

        if unidades_en_linea + unidades_palabra < unidades_por_linea:
            unidades_en_linea += unidades_palabra
            if palabra == linea[1].split(' ')[0] and texto_liena in linea[1] :
                if linea[1].startswith("&.8/rf"):
                    texto_liena="&.8/rf"
                    texto_liena += palabra+' '
                   
                else:
                    texto_liena=""
                    texto_liena += palabra+' '
                
            else:
                texto_liena += palabra+' '
               
             
                    
                
            
            if palabra == linea[1].split(' ')[-1]:
                if linea[1].startswith("&.8/rf"):
                    texto_liena="&.8/rf"+texto_liena
                info_tablas["descripcion_articulos"][-1].append(texto_liena[:-1])
                ##############################
                obtener_codigo(linea, texto_liena)
                obtener_garantia(linea, texto_liena)
                obtener_unidades(linea, texto_liena)
                obtener_precios(linea, texto_liena)
                obtener_descuentos(linea, texto_liena)
                obtener_netos(linea, texto_liena)
                obtener_importes(linea, texto_liena)
                ###############################
                
                numero_linea += 1
                contador_lineas_cada_tabla += 1
                texto_liena = ''
                unidades_en_linea = 0
                if contador_lineas_cada_tabla == 24:
                    info_tablas["descripcion_articulos"].append([])
                    info_tablas["codigos"].append([])
                    info_tablas["garantias"].append([])
                    info_tablas["unidades"].append([])
                    info_tablas["precios"].append([])
                    info_tablas["descuentos"].append([])
                    info_tablas["netos"].append([])
                    info_tablas["importes"].append([])
                    contador_lineas_cada_tabla = 1
                    contador_tablas += 1
        
        else:
            if linea[1].startswith("&.8/rf"):
                texto_liena="&.8/rf"+texto_liena
            info_tablas["descripcion_articulos"][-1].append(texto_liena)
            ##############################
            obtener_codigo(linea, texto_liena)
            obtener_garantia(linea, texto_liena)
            obtener_unidades(linea, texto_liena)
            obtener_precios(linea, texto_liena)
            obtener_descuentos(linea, texto_liena)
            obtener_netos(linea, texto_liena)
            obtener_importes(linea, texto_liena)
            ###############################
            numero_linea += 1
            contador_lineas_cada_tabla += 1
            unidades_en_linea = unidades_palabra
            texto_liena = palabra + ' '
            if contador_lineas_cada_tabla == 24:
                info_tablas["descripcion_articulos"].append([])
                info_tablas["codigos"].append([])
                info_tablas["garantias"].append([])
                info_tablas["unidades"].append([])
                info_tablas["precios"].append([])
                info_tablas["descuentos"].append([])
                info_tablas["netos"].append([])
                info_tablas["importes"].append([])
                contador_lineas_cada_tabla = 1
                contador_tablas += 1
            
            if linea[1].split(' ')[-1] in texto_liena.split():
                info_tablas["descripcion_articulos"][-1].append(texto_liena)
                info_tablas["codigos"][-1].append('')
                info_tablas["garantias"][-1].append('')
                info_tablas["unidades"][-1].append('')
                info_tablas["precios"][-1].append('')
                info_tablas["descuentos"][-1].append('')
                info_tablas["netos"][-1].append('')
                info_tablas["importes"][-1].append('')
                numero_linea += 1
                contador_lineas_cada_tabla += 1
                unidades_en_linea = unidades_palabra
                texto_liena =' '
                if contador_lineas_cada_tabla == 24:
                    info_tablas["descripcion_articulos"].append([])
                    info_tablas["codigos"].append([])
                    info_tablas["garantias"].append([])
                    info_tablas["unidades"].append([])
                    info_tablas["precios"].append([])
                    info_tablas["descuentos"].append([])
                    info_tablas["netos"].append([])
                    info_tablas["importes"].append([])
                    contador_lineas_cada_tabla = 1
                    contador_tablas += 1

##############################################

def writeString(c,x,alto,y,text,size,font='Helvetica-Bold'):
    c.setFont(font,size)
    if font == 'Helvetica-Bold':
        c.setFillColor(aColor='black')
    else:
        c.setFillColor(aColor='#111111')
    # c.setFillColor(aColor='black')
    c.drawString(x,alto-y,text)
    c.setFillColor(aColor='lightblue')


with open('cabecera.json','r') as archivo:
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

c = canvas.Canvas('factura.pdf',pagesize=A4)

numero=contador_tablas  
final=False
total_unidades = 0
for numero_tabla in range(numero):
    if numero_tabla<4:
        c.setFillColor(aColor='lightblue')
        c.setStrokeColor(aColor='gray')
        #nombre documento
        c.roundRect(60,alto-114,170,20,3,stroke=1 ,fill=0)
        c.roundRect(60,alto-114,171,20,3,stroke=1 ,fill=0)
        writeString(c,115,alto,110,datos['DOC_DENU'],15)
            #codigo barras
        with open('codigo.png', 'wb') as f:
            Code39(datos['FE_BARCODE'].replace('*',''), writer=ImageWriter(),add_checksum=False).write(f, text='', options= {'quiet_zone':0})
            c.drawImage('codigo.png',235,alto-112,110,15)
                        
      
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
        writeString(c,65,alto,140,'Prueba',titulo,'Helvetica')#datos['CDFRA']
        writeString(c,123,alto,125,serie,titulo)
        writeString(c,123,alto,140,datos['SFAC'],titulo,'Helvetica')
        writeString(c,148,alto,125,fecha_factura,titulo)
        writeString(c,148,alto,140,'Prueba',titulo,'Helvetica')#datos['FE_FEC']
        writeString(c,205,alto,125,cod_cl,titulo)
        writeString(c,205,alto,140,'prueba',titulo,'Helvetica')#datos['FE_CCL']
        writeString(c,245,alto,125,cif_dni,titulo)
        writeString(c,245,alto,140,'prueba',titulo,'Helvetica')#datos['CL_CIF']
        writeString(c,302,alto,125,alm,titulo)
        writeString(c,302,alto,140,'Prueba',titulo,'Helvetica')#datos['FE_ALM']
        writeString(c,63,alto,155,vendedor,titulo)
        writeString(c,106,alto,155,'Prueba',titulo,'Helvetica')#datos['FE_VD'] datos['VD_DENO'] 
        writeString(c,213,alto,155,ext_centralita,titulo)
        writeString(c,296,alto,155,'prueba',titulo,'Helvetica')#datos['VD_EXT']
        # cuadro envio
        c.roundRect(60,alto-222,262,48,0,stroke=1,fill=0)
        c.roundRect(60,alto-223,263,49,0,stroke=1,fill=0)
        writeString(c,60,alto,170,enviar_a,titulo)
        writeString(c,62,alto,185,datos['DL_DENO'],titulo,'Helvetica')
        writeString(c,62,alto,195,datos['DL_CON'],titulo,'Helvetica')
        writeString(c,62,alto,205,datos['DL_DOM'],titulo,'Helvetica')
        writeString(c,62,alto,215,datos['DL_CDP']+' '+datos['DL_POB']+' '+datos['DL_PROV']+' '+datos['DL_PAIS'] ,titulo,'Helvetica')

        # cuadro datos de remitente
        c.roundRect(350,alto-125,205,73,0,stroke=1,fill=0)
        c.roundRect(350,alto-126,206,74,0,stroke=1,fill=0)
        writeString(c,355,alto,60,datos["AMNOM"],titulo,'Helvetica')#datos['AM_NOM']
        writeString(c,550-len(datos["AMDOM"])*4.7,alto,75,datos["AMDOM"],titulo)#datos['AM_DOM']
        writeString(c,550-len(datos['AMCDP'])*4.7,alto,90,datos['AMCDP'],titulo)
        writeString(c,550-len(datos['AMFAX'])*4.2,alto,105,datos['AMFAX'],titulo)
        writeString(c,550-len(datos['AMFAX'])*4.2,alto,120,datos['AMFAX'],titulo)
        # cuadro datos de destinatario
        c.roundRect(350,alto-222,205,80,0,stroke=1,fill=0)
        c.roundRect(350,alto-223,206,81,0,stroke=1,fill=0)
        writeString(c,350,alto,138,factura_a,titulo)
        writeString(c,352,alto,152,datos['CL_DENO'],titulo)#datos['CL_DENO']
        writeString(c,352,alto,165,datos['CL_NOM'],titulo,'Helvetica')#datos['CL_NOM']
        writeString(c,352,alto,177,datos['CL_DOM'],titulo,'Helvetica')#datos['CL_DOM']
        writeString(c,352,alto,190,datos['CL_CDP']+' '+ datos['CL_POB'],titulo,'Helvetica')
        writeString(c,352,alto,202,datos['CL_PROV']+' '+ datos['CL_PAIS'],titulo,'Helvetica')
        writeString(c,352,alto,215,datos['CL_ATT'],titulo,'Helvetica')#datos['CL_ATT']
        writeString(c,520,alto,138,'Pag. '+str(numero_tabla+1),titulo,'Helvetica')
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
        codigos_tabla_1 = info_tablas["codigos"][numero_tabla]
        descripciones_tabla_1 = info_tablas["descripcion_articulos"][numero_tabla]
        garantias_tabla = info_tablas["garantias"][numero_tabla]
        unidades_tabla = info_tablas["unidades"][numero_tabla]
        precios_tabla = info_tablas["precios"][numero_tabla]
        descuentos_tabla = info_tablas["descuentos"][numero_tabla]
        netos_tabla = info_tablas["netos"][numero_tabla]
        importes_tabla = info_tablas["importes"][numero_tabla]

        lineas_tabla_1 = zip(codigos_tabla_1, descripciones_tabla_1, garantias_tabla, unidades_tabla, precios_tabla, descuentos_tabla, netos_tabla, importes_tabla)
        for index,linea in enumerate(lineas_tabla_1):
            if linea[3] != '':
                total_unidades += float(linea[3])
            if '&.8/rf' in linea[1]:
                texto=linea[1].replace('&.8/rf', '')
                # writeString(c,138,alto,255+(index*12.8),texto,5.45)
                writeString(c,138,alto,255+(index*12.8),texto,6.7)
            else:
                writeString(c,138,alto,255+(index*12.8),linea[1],7.5,'Helvetica')
            text_code=linea[0].replace('&.7>', '')    
            writeString(c,65,alto,255+(index*12.8),text_code,7.5,'Helvetica')
            writeString(c,330,alto,255+(index*12.8),linea[2],7.5,'Helvetica')
            writeString(c,368,alto,255+(index*12.8),linea[3],7.5,'Helvetica')
            writeString(c,405,alto,255+(index*12.8),linea[4],7.5,'Helvetica')
            writeString(c,450,alto,255+(index*12.8),linea[5],7.5,'Helvetica')
            writeString(c,480,alto,255+(index*12.8),linea[6],7.5,'Helvetica')
            writeString(c,526,alto,255+(index*12.8),linea[7],7.5,'Helvetica')
        writeString(c,368,alto,556,str("{:.2f}".format(total_unidades)),7.5,'Helvetica-Bold')
            
        if numero_tabla!=numero - 1:
            c.showPage()
    final=True
if numero_tabla<4 and final==True:
    # texto de Atencion
    writeString(c,90,alto,570,text_aten1,6)
    writeString(c,90,alto,579,text_aten2,6)

    # cuadro de total factura
    if len(datos['FE_TTTIMP'])==1:
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
        writeString(c,70,alto,620,check0(datos['FE_TTTIMP'][0][0]),titulo)
        writeString(c,112,alto,620,check0(datos['FE_TTTIMP'][0][1]),titulo)
        writeString(c,159,alto,620,check0(datos['FE_TTTIMP'][0][2]),titulo)
        writeString(c,206,alto,620,check0(datos['FE_TTTIMP'][0][3]),titulo)
        writeString(c,275,alto,620,check0(datos['FE_TTTIMP'][0][4]),titulo)
        writeString(c,325,alto,620,check0(datos['FE_TTTIMP'][0][5]),titulo)
        writeString(c,360,alto,620,check0(datos['FE_TTTIMP'][0][6]),titulo)
        writeString(c,408,alto,620,check0(datos['FE_TTTIMP'][0][7]),titulo)
        writeString(c,439,alto,620,check0(datos['FE_TTTIMP'][0][8]),titulo)
        writeString(c,518,alto,620,check0(datos['FE_TTTIMP'][0][9]),titulo)
        
    if len(datos['FE_TTTIMP'])== 2:
        c.roundRect(60,alto-624,520,40,0,stroke=1,fill=0)
        c.roundRect(60,alto-625,521,41,0,stroke=1,fill=0)
        c.roundRect(60,alto-598,520,14,0,stroke=1,fill=1)
        c.roundRect(496,alto-624,84,26,0,stroke=1,fill=1)
        c.rect(112,alto-624,0,40)
        c.rect(159,alto-624,0,40)
        c.rect(206,alto-624,0,40)
        c.rect(258,alto-624,0,40)
        c.rect(320,alto-624,0,40)
        c.rect(351,alto-624,0,40)
        c.rect(403,alto-624,0,40)
        c.rect(434,alto-624,0,40)
        c.rect(496,alto-624,0,40)
        writeString(c,65,alto,593,importe,titulo)
        writeString(c,120,alto,593,irpf,titulo)
        writeString(c,165,alto,593,retencion,titulo)
        writeString(c,210,alto,593,transporte,titulo)
        writeString(c,265,alto,593,imponible,titulo)
        writeString(c,322,alto,593,por_iva,titulo)
        writeString(c,380,alto,593,iva,titulo)
        writeString(c,405,alto,593,por_eqv,titulo)
        writeString(c,435,alto,593,equivalencia,titulo)
        writeString(c,525,alto,593,t_factura,titulo)
        writeString(c,70,alto,607,check0(datos['FE_TTTIMP'][0][0]),titulo,'Helvetica')
        writeString(c,112,alto,607,check0(datos['FE_TTTIMP'][0][1]),titulo,'Helvetica')
        writeString(c,159,alto,607,check0(datos['FE_TTTIMP'][0][2]),titulo,'Helvetica')
        writeString(c,206,alto,607,check0(datos['FE_TTTIMP'][0][3]),titulo,'Helvetica')
        writeString(c,275,alto,607,check0(datos['FE_TTTIMP'][0][4]),titulo,'Helvetica')
        writeString(c,325,alto,607,check0(datos['FE_TTTIMP'][0][5]),titulo,'Helvetica')
        writeString(c,360,alto,607,check0(datos['FE_TTTIMP'][0][6]),titulo,'Helvetica')
        writeString(c,408,alto,607,check0(datos['FE_TTTIMP'][0][7]),titulo,'Helvetica')
        writeString(c,439,alto,607,check0(datos['FE_TTTIMP'][0][8]),titulo,'Helvetica')
        writeString(c,518,alto,607,check0(datos['FE_TTTIMP'][0][9]),9)
        writeString(c,70,alto,618,check0(datos['FE_TTTIMP'][1][0]),titulo,'Helvetica')
        writeString(c,112,alto,618,check0(datos['FE_TTTIMP'][1][1]),titulo,'Helvetica')
        writeString(c,159,alto,618,check0(datos['FE_TTTIMP'][1][2]),titulo,'Helvetica')
        writeString(c,206,alto,618,check0(datos['FE_TTTIMP'][1][3]),titulo,'Helvetica')
        writeString(c,275,alto,618,check0(datos['FE_TTTIMP'][1][4]),titulo,'Helvetica')
        writeString(c,325,alto,618,check0(datos['FE_TTTIMP'][1][5]),titulo,'Helvetica')
        writeString(c,360,alto,618,check0(datos['FE_TTTIMP'][1][6]),titulo,'Helvetica')
        writeString(c,408,alto,618,check0(datos['FE_TTTIMP'][1][7]),titulo,'Helvetica')
        writeString(c,439,alto,618,check0(datos['FE_TTTIMP'][1][8]),titulo,'Helvetica')
        writeString(c,518,alto,618,check0(datos['FE_TTTIMP'][1][9]),9)
    if len(datos['FE_TTTIMP'])== 3:
        c.roundRect(60,alto-630,520,40,0,stroke=1,fill=0)
        c.roundRect(60,alto-631,521,41,0,stroke=1,fill=0)
        c.roundRect(60,alto-598,520,14,0,stroke=1,fill=1)
        c.roundRect(496,alto-630,84,32,0,stroke=1,fill=1)
        c.rect(112,alto-630,0,46)
        c.rect(159,alto-630,0,46)
        c.rect(206,alto-630,0,46)
        c.rect(258,alto-630,0,46)
        c.rect(320,alto-630,0,46)
        c.rect(351,alto-630,0,46)
        c.rect(403,alto-630,0,46)
        c.rect(434,alto-630,0,46)
        c.rect(496,alto-630,0,46)
        writeString(c,65,alto,593,importe,titulo)
        writeString(c,120,alto,593,irpf,titulo)
        writeString(c,165,alto,593,retencion,titulo)
        writeString(c,210,alto,593,transporte,titulo)
        writeString(c,265,alto,593,imponible,titulo)
        writeString(c,322,alto,593,por_iva,titulo)
        writeString(c,380,alto,593,iva,titulo)
        writeString(c,405,alto,593,por_eqv,titulo)
        writeString(c,435,alto,593,equivalencia,titulo)
        writeString(c,525,alto,593,t_factura,titulo)
        writeString(c,70,alto,607,check0(datos['FE_TTTIMP'][0][0]),titulo,'Helvetica')
        writeString(c,112,alto,607,check0(datos['FE_TTTIMP'][0][1]),titulo,'Helvetica')
        writeString(c,159,alto,607,check0(datos['FE_TTTIMP'][0][2]),titulo,'Helvetica')
        writeString(c,206,alto,607,check0(datos['FE_TTTIMP'][0][3]),titulo,'Helvetica')
        writeString(c,275,alto,607,check0(datos['FE_TTTIMP'][0][4]),titulo,'Helvetica')
        writeString(c,325,alto,607,check0(datos['FE_TTTIMP'][0][5]),titulo,'Helvetica')
        writeString(c,360,alto,607,check0(datos['FE_TTTIMP'][0][6]),titulo,'Helvetica')
        writeString(c,408,alto,607,check0(datos['FE_TTTIMP'][0][7]),titulo,'Helvetica')
        writeString(c,439,alto,607,check0(datos['FE_TTTIMP'][0][8]),titulo,'Helvetica')
        writeString(c,518,alto,607,check0(datos['FE_TTTIMP'][0][9]),9)
        writeString(c,70,alto,618,check0(datos['FE_TTTIMP'][1][0]),titulo,'Helvetica')
        writeString(c,112,alto,618,check0(datos['FE_TTTIMP'][1][1]),titulo,'Helvetica')
        writeString(c,159,alto,618,check0(datos['FE_TTTIMP'][1][2]),titulo,'Helvetica')
        writeString(c,206,alto,618,check0(datos['FE_TTTIMP'][1][3]),titulo,'Helvetica')
        writeString(c,275,alto,618,check0(datos['FE_TTTIMP'][1][4]),titulo,'Helvetica')
        writeString(c,325,alto,618,check0(datos['FE_TTTIMP'][1][5]),titulo,'Helvetica')
        writeString(c,360,alto,618,check0(datos['FE_TTTIMP'][1][6]),titulo,'Helvetica')
        writeString(c,408,alto,618,check0(datos['FE_TTTIMP'][1][7]),titulo,'Helvetica')
        writeString(c,439,alto,618,check0(datos['FE_TTTIMP'][1][8]),titulo,'Helvetica')
        writeString(c,518,alto,618,check0(datos['FE_TTTIMP'][1][9]),9)
        writeString(c,70,alto,628,check0(datos['FE_TTTIMP'][2][0]),titulo,'Helvetica')
        writeString(c,112,alto,628,check0(datos['FE_TTTIMP'][2][1]),titulo,'Helvetica')
        writeString(c,159,alto,628,check0(datos['FE_TTTIMP'][2][2]),titulo,'Helvetica')
        writeString(c,206,alto,628,check0(datos['FE_TTTIMP'][2][3]),titulo,'Helvetica')
        writeString(c,275,alto,628,check0(datos['FE_TTTIMP'][2][4]),titulo,'Helvetica')
        writeString(c,325,alto,628,check0(datos['FE_TTTIMP'][2][5]),titulo,'Helvetica')
        writeString(c,360,alto,628,check0(datos['FE_TTTIMP'][2][6]),titulo,'Helvetica')
        writeString(c,408,alto,628,check0(datos['FE_TTTIMP'][2][7]),titulo,'Helvetica')
        writeString(c,439,alto,628,check0(datos['FE_TTTIMP'][2][8]),titulo,'Helvetica')
        writeString(c,518,alto,628,check0(datos['FE_TTTIMP'][2][9]),9)
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
    for pos,d_banco in enumerate(datos['BCH']):
        writeString(c,295,alto,693+(12*pos),d_banco[0],6)
        writeString(c,396,alto,693+(12*pos),d_banco[1],6,'Helvetica')
        writeString(c,449,alto,693+(12*pos),d_banco[3],6,'Helvetica')
        writeString(c,475,alto,693+(12*pos),d_banco[2],6)
    # cuadros de forma de pago
    c.roundRect(60,alto-653,205,17,3,stroke=1,fill=1)
    c.roundRect(60,alto-653.5,205.5,17.5,3,stroke=1,fill=0)
    writeString(c,65,alto,643,pago,6)
    writeString(c,65,alto,650,c_c2,6)
    c.roundRect(60,alto-684,205,25,3,stroke=1,fill=1)
    c.roundRect(60,alto-684.5,205.5,25.5,3,stroke=1,fill=0)
    line=''
    listado=['','']
    unidadeslinea=1000
    unidades_en_linea=0
    text = medida_str(datos['TRANS'].replace('\n', ''))
    for palabra in datos['TRANS'].split():
        unidades_palabra += medida_str(palabra)
        if unidades_en_linea + unidades_palabra < unidadeslinea:
            unidades_en_linea += unidades_palabra
            line += palabra+' '
            listado[1] = line
            
        else:
            listado[0] = line
            line=''
            unidades_en_linea=0
        
    if len(listado)>1:
        writeString(c,65,alto,670,listado[0],6)
        writeString(c,65,alto,680,listado[1],6)
    else:
        writeString(c,65,alto,670,listado[0],6)
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
    # texto de reemboloso
    writeString(c,40,alto,745,datos['MSG_LPI'].replace('\n', ''),5.3)


c.save()
