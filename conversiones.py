import sys

def convertir_pesos(valor_pesos, tasa_sol, tasa_peso_arg, tasa_dolar):
    valor_sol = valor_pesos * tasa_sol
    valor_peso_arg = valor_pesos * tasa_peso_arg
    valor_dolar = valor_pesos * tasa_dolar
    return valor_sol, valor_peso_arg, valor_dolar