def word_count(archivo):
    #Metodo para evaluar errores
    try:
        #Metodo para abrir archivos
        with open(archivo , "r") as file:
            #Uso de metodo de listas
            texto = file.read()
            palabras = texto.split(" ")
            distinct_palabras = set(palabras)
            num_palabras = len(distinct_palabras)
            caracter_distinto = set(texto)
            num_caracter = len(caracter_distinto)
            return num_palabras, num_caracter
    #Metodo para evaluar si el archivo fue encontrado
    except FileNotFoundError:
        return(f'El archivo no fue encontrado')
    #Lanzar error visualmente
    except Exception as e:
        return(f'ocurrio un error: {e}')

#Cargar ruta de archivo
archivo = "lorem_ipsum.txt"
#Mostrar resultado pasando variable a la funcion
resultado = word_count(archivo)

#Mostrar resultados separando tupla
print(f'La cantidad de palabras distintas es: {resultado[0]}')
print(f'La cantidad de caracteres distintos es: {resultado[1]}')