def contar_letras_y_espacios(contenido):
    letras = 0
    espacios = 0
    for c in contenido:
        if c.isalpha():
            letras += 1
        elif c.isspace():
            espacios += 1
    return letras, espacios

def main():
   
    with open("ejemplo.txt", "r") as archivo:
        contenido = archivo.read()

  
    print(contenido)

    letras, espacios = contar_letras_y_espacios(contenido)

   
    resumen = f"Cantidad de letras: {letras}\nCantidad de espacios: {espacios}"

    with open("resumen.txt", "w") as archivo_resumen:
        archivo_resumen.write(resumen)

   
    print(resumen)

if __name__ == "__main__":
    main()
