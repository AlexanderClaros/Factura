from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def dividir_texto_por_ancho(texto, ancho_maximo):
    # Inicializar variables
    resultado = []
    oracion_actual = ''
    ancho_actual = 0

    # Crear un objeto canvas para medir el ancho del texto
    c = canvas.Canvas('dummy.pdf', pagesize=letter)
    c.setFontSize(12)

    # Recorrer todas las palabras del texto
    for palabra in texto.split():
        ancho_palabra = c.stringWidth(palabra + ' ')

        # Si la palabra cabe en la oración actual, añadirla a la oración actual y actualizar el ancho actual
        if ancho_actual + ancho_palabra <= ancho_maximo:
            if oracion_actual:
                oracion_actual += ' '
            oracion_actual += palabra
            ancho_actual += ancho_palabra
        # Si la palabra no cabe en la oración actual, guardar la oración actual y comenzar una nueva oración
        else:
            resultado.append(oracion_actual)
            oracion_actual = palabra
            ancho_actual = ancho_palabra

    # Añadir la última oración al listado de oraciones
    resultado.append(oracion_actual)

    return resultado
texto = 'Este es un texto de ejemplo que se va a dividir en oraciones de acuerdo al ancho máximo por oración. Espero que esta función te sea útil.'
ancho_maximo = 2 * inch  # 2 pulgadas
oraciones = dividir_texto_por_ancho(texto, ancho_maximo)
print(oraciones)
