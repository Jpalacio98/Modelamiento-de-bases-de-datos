import requests
import json


#response = requests.get("https://jpalacio2022.000webhostapp.com/API/configBD.php")

#response = requests.post(f"https://jpalacio2022.000webhostapp.com/API/{archivo}.php",data=data)
#print(response.text)


def llenarTablaDpto():
    with open("Tablas/departamentos.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for dpto in datos:
        data={
            'id':dpto["codigodepartamentoatencion"],
            'nombre':dpto["nombremunicipioatencion"] 
        }
        response = requests.post(f"https://jpalacio2022.000webhostapp.com/API/adicionarDpto.php",data=data)
        listResult.append({'status_code':response.status_code,'message':response.text})
    return  listResult


def llenarTablaMun(dirData,archivo):
    with open(dirData, 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for dpto in datos:
        data={
            'id':dpto["codigodepartamentoatencion"],
            'nombre':dpto["nombremunicipioatencion"] 
        }
        response = requests.post(f"https://jpalacio2022.000webhostapp.com/API/{archivo}.php",data=data)
        listResult.append({'status_code':response.status_code,'message':response.text})
    return  listResult
