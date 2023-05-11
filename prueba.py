from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import json

def writeString(c,x,alto,y,text,size,font='Helvetica-Bold'):
    c.setFont(font,size)
    c.setFillColor(aColor='black')
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

ancho,alto,=A4
titulo=8
negrita=5.8
normal=7
print (alto,ancho)
c = canvas.Canvas('prueba.pdf',pagesize=A4)
numero=4  
final=False
for numero_linea in range(numero):
    if numero_linea<4:
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
        writeString(c,210,alto,125,cod_cl,titulo)
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
        writeString(c,375,alto,240,ud,titulo)
        writeString(c,410,alto,240,precio,titulo)
        writeString(c,450,alto,240,dto,titulo)
        writeString(c,490,alto,240,neto,titulo)
        writeString(c,535,alto,240,importes,titulo)
        if numero_linea!=3:
            c.showPage()
    final=True
if numero_linea<4 and final==True:
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
    writeString(c,330,alto,603,por_iva,titulo)
    writeString(c,385,alto,603,iva,titulo)
    writeString(c,405,alto,603,por_eqv,titulo)
    writeString(c,440,alto,603,equivalencia,titulo)
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

c.save()
