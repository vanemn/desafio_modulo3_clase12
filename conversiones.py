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

    valor_sol, valor_peso_arg, valor_dolar = convertir_pesos(valor_pesos, tasa_sol, tasa_peso_arg, tasa_dolar)
    
    print(f"Los {valor_pesos} pesos equivalen a:")
    print(f"{valor_sol:.1f} Soles")
    print(f"{valor_peso_arg:.1f} Pesos Argentinos")
    print(f"{valor_dolar:.1f} Dólares")

if __name__ == "__main__":
    main()
