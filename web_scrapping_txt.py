import re

# Ruta al archivo de texto (txt) con el fragmento HTML
ruta_archivo = 'Inbox.txt'

# Leer el contenido del archivo
with open(ruta_archivo, 'r', encoding='utf-8') as file:
    contenido_txt = file.read()

# Definir un patrón de expresión regular para buscar la palabra "matrícula"
patron_matricula = re.compile(r'\bMatricula\b', re.IGNORECASE)

# Buscar la palabra "matrícula" en el contenido
coincidencias_matricula = patron_matricula.search(contenido_txt)

# Extraer el párrafo completo si se encuentra la palabra "matrícula"
if coincidencias_matricula:
    inicio_parrafo = contenido_txt.rfind('\n', 0, coincidencias_matricula.start()) + 1
    fin_parrafo = contenido_txt.find('\n', coincidencias_matricula.end())

    # Asegurarse de que fin_parrafo no sea -1 (indicando que no se encontró otro salto de línea)
    if fin_parrafo == -1:
        fin_parrafo = len(contenido_txt)

    # Extraer el párrafo completo
    parrafo_completo = contenido_txt[inicio_parrafo:fin_parrafo].strip()

    # Imprimir el resultado
    print("Párrafo que contiene la palabra 'matrícula':")
    print(parrafo_completo)
else:
    print("La palabra 'matrícula' no se encontró en el archivo.")





# Definir un patrón de expresión regular para buscar la palabra "modelo"
patron_modelo = re.compile(r'\bModelo\b', re.IGNORECASE)

# Buscar la palabra "modelo" en el contenido
coincidencias_modelo = patron_modelo.search(contenido_txt)

# Extraer el párrafo completo si se encuentra la palabra "modelo"
if coincidencias_modelo:
    inicio_parrafo = contenido_txt.rfind('\n', 0, coincidencias_modelo.start()) + 1
    fin_parrafo = contenido_txt.find('\n', coincidencias_modelo.end())

    # Asegurarse de que fin_parrafo no sea -1 (indicando que no se encontró otro salto de línea)
    if fin_parrafo == -1:
        fin_parrafo = len(contenido_txt)

    # Extraer el párrafo completo
    parrafo_completo = contenido_txt[inicio_parrafo:fin_parrafo].strip()

    # Imprimir el resultado
    print("Párrafo que contiene la palabra 'modelo':")
    print(parrafo_completo)
else:
    print("La palabra 'modelo' no se encontró en el archivo.")
    

# Definir un patrón de expresión regular para buscar la palabra "marca"
patron_marca = re.compile(r'\bMarca\b', re.IGNORECASE)

# Buscar la palabra "marca" en el contenido
coincidencias_marca = patron_marca.search(contenido_txt)

# Extraer el párrafo completo si se encuentra la palabra "marca"
if coincidencias_marca:
    inicio_parrafo = contenido_txt.rfind('\n', 0, coincidencias_marca.start()) + 1
    fin_parrafo = contenido_txt.find('\n', coincidencias_marca.end())

    # Asegurarse de que fin_parrafo no sea -1 (indicando que no se encontró otro salto de línea)
    if fin_parrafo == -1:
        fin_parrafo = len(contenido_txt)

    # Extraer el párrafo completo
    parrafo_completo = contenido_txt[inicio_parrafo:fin_parrafo].strip()

    # Imprimir el resultado
    print("Párrafo que contiene la palabra 'marca':")
    print(parrafo_completo)
else:
    print("La palabra 'marca' no se encontró en el archivo.")