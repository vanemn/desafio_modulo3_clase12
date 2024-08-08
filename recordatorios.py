#lista de recordatorios  
recordatorios = [  
    ['2021-01-01', '11:00', 'Levantarse y ejercitar'],  
    ['2021-07-15', '13:00', 'No hacer nada es feriado'],  
    ['2021-09-18', '16:00', 'Ramadas'],  
    ['2021-12-24', '22:00', 'Cena de Navidad'],    
    ['2021-12-25', '00:00', 'Navidad'],  
    ['2021-12-31', '22:00', 'Cena de Año Nuevo'],   
]  
print("-------------Recordatorios iniciales:")  
for evento in recordatorios:  
    print(evento) 

nuevo_evento = ['2021-01-02', '06:00', 'Empezar el Año']  #en la guia dice febrero pero despues muestra enero
recordatorios.append(nuevo_evento)  

print("-------------Recordatorios agregados:")  
for evento in recordatorios:  
    print(evento) 

# uso de función for para que cambie el feriado
for i in range(len(recordatorios)):  
    if recordatorios[i][0] == "2021-07-15":  
        recordatorios[i][0] = "2021-07-16"  
        recordatorios[i][1] = "13:00"  # Manteniendo la hora original  
        recordatorios[i][2] = "Día del trabajo (corregido)"

# ordenar la lista por fecha y hora  
recordatorios.sort(key=lambda x: (x[0], x[1]))  
  
print("-------------Lista final de recordatorios:")  
for evento in recordatorios:  
    print(evento)   