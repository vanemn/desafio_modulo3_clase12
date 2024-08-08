def word_count(archivo):
    
    try:
        with open(archivo , "r") as file:
            texto = file.read()
            palabras = texto.split(" ")
            distinct_palabras = set(palabras)
            num_palabras = len(distinct_palabras)
            caracter_distinto = set(texto)
            num_caracter = len(caracter_distinto)
            return num_palabras, num_caracter
    except FileNotFoundError:
        return(f'El archivo no fue encontrado')
    except Exception as e:
        return(f'ocurrio un error: {e}')


archivo = "lorem_ipsum.txt"
resultado = word_count(archivo)

print(f'La cantidad de palabras disntitas es: {resultado[0]}')
print(f'La cantidad de caracteres distintos es: {resultado[1]}')