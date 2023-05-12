import json
from medidas_letras import medidas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas('prueba.pdf',pagesize=A4)
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
    'codigos': [[]],
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
            print(palabra,'--',texto) 
            if unidades_en_linea + unidades_palabra < unidades_por_linea:
                unidades_en_linea += unidades_palabra
                texto_liena += palabra + ' '
               
                if palabra == texto.split(' ')[-1]:
                    info_tablas["descripcion_articulos"][-1].append(texto[:-1])
                    
                    print(texto_liena,'>>>>>>>>>>>>>>>>>>')
                    numero_linea += 1
                    contador_lineas_cada_tabla += 1
                    texto_liena = ''
                    unidades_en_linea = 0
                    if contador_lineas_cada_tabla == 23:
                        info_tablas["descripcion_articulos"].append([])
                        contador_lineas_cada_tabla = 1
                        contador_tablas += 1
            
            else:
                info_tablas["descripcion_articulos"][-1].append(texto)
                print(texto_liena,'----------')
                
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
                    info_tablas["codigos"][indice_lista][indice_elemento] = codigo
                    break
            # print(codigo)
        
        # info_tablas["codigos"][indice_lista][indice_elemento] = codigo



c.showPage()
c.save()