import json
datos={
    "tipo": "Factura",
    "n_factura": "Nºfactura",
    "serie": "Serie",
    "fecha_factura": "Fecha Factura",
    "cod_cl": "Cod Cl",
    "cif_dni": "Cif/Dni",
    "alm": "Alm",
    "vendedor": "Vendedor",
    "ext_centralita": "Extensión Centralita",
    "enviar_a":"Enviar A:",
    "factura_a":"FACTURA A:",
    "codigo":"Código",
    "desc_art":"Descripción Articulo",
    "garantia":"Garantia",
    "ud":"Udes",
    "precio":"Precio",
    "dto":"%Dto",
    "neto":"Neto",
    "importes":"Importes",
    "importe":"Importe",
    "irpf":"%R.IRPF",
    "retencion":"Retencion",
    "transporte":"Transporte",
    "imponible":"B.imponible",
    "por_iva":"%Iva",
    "iva":"Iva",
    "por_eqv":"%Eqv",
    "equivalencia":"Equivalencia",
    "t_factura":"Total Factura",
    "pago":"Forma Pago:",
    "c_c":"C/C:",
    "p_realizados":"Pagos Realizados o abonos aplicados:",
    "f_ven":"Fecha Vto",
    "importes2":"Importes",
    "r_financiero":"Rec.Financiero",
    "total":"Total €",
    "dat_banco":"Datos Bancarios Transfer",
    "swift":"Swift",
    "iban":"Iban",
    "c_c2":"C/C",
    "text1_atencion":'¡¡¡ATENCIÓN!!! Todo artículo que tenga las etiquetas  de Nº de serie o de Garantía manipuladas, quitadas o deterioradas perderá la garantía',
    "text2_atencion":'Para hacer efectiva la garantía  es imprescindible enviar junto con el articulo copia de la factura de compra, manuales y discos originales del mismo.'
}
with open("cabecera.json", "w") as archivo:
    # Convierte los datos en formato JSON y escribe en el archivo
    json.dump(datos, archivo)