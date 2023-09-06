from firebase import firebase
import pandas as pd
import json
 

firebase = firebase.FirebaseApplication("https://bd-avanzada-default-rtdb.firebaseio.com/",None)

def llenarTablaDpto():
    with open("Tablas/departamentos.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for dpto in datos:
        data={
            'idDpto':dpto["codigodepartamentoatencion"],
            'nombre':dpto["nombredepartamentoatencion"] 
        }
        response = firebase.post("/departamentos",data=data)
        if response != 'None':
            message="Registro Completo"
        else:
            message="Registro Inompleto"
        listResult.append(message)
    return  listResult

def llenarTablaMun():
    with open("Tablas/municipios.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for mun in datos:
        data={
            'idMun':mun["codigomunicipioatencion"],
            'nombre':mun["nombremunicipioatencion"],
            'idDpto':mun["codigodepartamentoatencion"], 
        }
        response = firebase.post("/municipios",data=data)
        if response != 'None':
            message="Registro Completo"
        else:
            message="Registro Inompleto"
        listResult.append(message)
    return  listResult

def llenarTablaBenficiario():
    with open("Tablas/beneficiario.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for index,benef in enumerate(datos):
        data={
            'idBeneficiario':index,
            'bancarizado':benef["bancarizado"],
            'discapacidad':benef["discapacidad"],
            'etnia':benef["etnia"], 
            'genero':benef["genero"], 
            'nivelescolaridad':benef["nivelescolaridad"], 
            'pais':benef["pais"], 
            'tipodocumento':benef["tipodocumento"], 
            'titular':benef["titular"], 
            'idMun':benef["codigomunicipioatencion"],
            'estadobeneficiario':benef["estadobeneficiario"], 
        }
        response = firebase.post("/beneficiarios",data=data)
        if response != 'None':
            message="Registro Completo"
        else:
            message="Registro Inompleto"
        listResult.append(message)
    return  listResult

def llenarTablaPrograma():
    with open("Tablas/programa.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for index,prog in enumerate(datos):
        data = {
        'idPrograma':index,
        'tipoasignacionbeneficio': prog["tipoasignacionbeneficio"],
        'tipobeneficio': prog["tipobeneficio"],
        'tipopoblacion': prog["tipopoblacion"],
        'rangobeneficioconsolidadoasignado': prog["rangobeneficioconsolidadoasignado"],
        'rangoultimobeneficioasignado': prog["rangoultimobeneficioasignado"],
        'fechaultimobeneficioasignado': prog["fechaultimobeneficioasignado"],
        'idBeneficiario':index,
        'rangoedad': prog["rangoedad"],
        'cantidaddebeneficiarios': prog["cantidaddebeneficiarios"],
        }
        response = firebase.post("/programa",data=data)
        if response != 'None':
            message="Registro Completo"
        else:
            message="Registro Inompleto"
        listResult.append(message)
    return  listResult

def Resultados(datos):
    clases = {}
    # Contar la frecuencia de cada clase en la lista
    for elemento in datos:
        if elemento in clases:
            clases[elemento] += 1
        else:
            clases[elemento] = 1
    # Imprimir las clases y sus cuentas
    for clase, count in clases.items():
        print(f"Clase {clase}: {count}")

def listarTablaDpto():
    datos = firebase.get("/departamentos","")
    return list(datos)
def BuscarTablaDpto(id):
    return firebase.get("/departamentos",id)


def listarTablaPrograma():
    datos = firebase.get("/programa","")
    return datos
def BuscarTablaPrograma(id):
    return firebase.get("/programa",id)
#-------llenado de tablas------#
# res = llenarTablaDpto()
# Resultados(res)
# res = llenarTablaMun()
# Resultados(res)
# res = llenarTablaBenficiario()
# Resultados(res)
# res = llenarTablaPrograma()
# Resultados(res)


#----------------DESARROLLO DE CONSULTAS---------------#
#1)¿Cuántos tipos de población hay y cuatos beneficiarios hay por cada tipo?

results =listarTablaPrograma()
#results = 
lista =[]
for clave, element in results.items():
    lista.append(element['tipopoblacion'])
Resultados(lista)


