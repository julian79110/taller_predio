import re
import json

with open('132-14150.json','r', encoding='utf-8') as f:
    data=json.load(f)

if data:
        for item in data['textoAnotaciones']:   
            cadena = item 
            for i in re.findall(r'ESPECIFICACION: [0-9]{3,5}', cadena):
                print(i)
else:
    print('No hay datos disponibles')