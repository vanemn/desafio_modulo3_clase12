#lista de recordatorios  
recordatorios = [  
    ['2021-01-01', '11:00', 'Levantarse y ejercitar'],  
    ['2021-01-02', '06:00', 'Empezar el año'],  
    ['2021-07-15', '13:00', 'No hacer nada es feriado'],  
    ['2021-09-18', '16:00', 'Ramadas'],  
    ['2021-12-24', '22:00', 'Cena de Navidad'],    
    ['2021-12-25', '00:00', 'Navidad'],  
    ['2021-12-31', '22:00', 'Cena de Año Nuevo'],   
]  
# uso de función for para que cambie el feriado
for evento in recordatorios:  
    if evento[0] == '2021-07-15':  
        evento[0] = '2021-07-16'   
        break   
fechas_a_eliminar = ['2021-05-01']  
recordatorios = [evento for evento in recordatorios if evento[0] not in fechas_a_eliminar]  

# ordenar la lista por fecha y hora  
recordatorios.sort(key=lambda x: (x[0], x[1]))  
  
for evento in recordatorios:  
    print(evento)  