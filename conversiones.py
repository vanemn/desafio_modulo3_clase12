import sys

def convertir_pesos(valor_pesos, tasa_sol, tasa_peso_arg, tasa_dolar):
    valor_sol = valor_pesos * tasa_sol
    valor_peso_arg = valor_pesos * tasa_peso_arg
    valor_dolar = valor_pesos * tasa_dolar
    return valor_sol, valor_peso_arg, valor_dolar

def main():
    if len(sys.argv) != 5:
        print("Para calcular ingresar de la siguiente forma: python conversiones.py <tasa_sol> <tasa_peso_arg> <tasa_dolar> <valor_pesos>")
        sys.exit(1)
    
    try:
        tasa_sol = float(sys.argv[1])
        tasa_peso_arg = float(sys.argv[2])
        tasa_dolar = float(sys.argv[3])
        valor_pesos = float(sys.argv[4])
    except ValueError:
        print("Error: Los valores deben ser números.")
        sys.exit(1)