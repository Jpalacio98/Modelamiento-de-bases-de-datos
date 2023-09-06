import pandas as pd
import json
from sodapy import Socrata

client = Socrata("www.datos.gov.co",
                 "U1UbMtgUtzZzxdlanUWUWx4mz",
                 username="jdavidpalacio@unicesar.edu.co",
                 password="@Jpalacio0949")

results = client.get("xfif-myr2", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)



# construimos los datos para la tabla departamento
departamentos = results_df[['codigodepartamentoatencion','nombredepartamentoatencion']]
#depuramos la tabla solo para dejar un insidencia de cada registro
depurar_DPTO = departamentos.drop_duplicates(subset='codigodepartamentoatencion')
# Mostrar los resultados
#print(depurar_DPTO)
#convertimos el data frame en un json 
depurar_DPTO.to_json("Tablas/departamentos.json", orient='records')

# Verificación: cargar el archivo JSON de nuevo en un DataFrame
# df_desde_json = pd.read_json("Tablas/departamentos.json", orient='records')
# # Mostrar el DataFrame cargado desde el archivo JSON
# print(df_desde_json)


# construimos los datos para la tabla municipio
municipios = results_df[['codigomunicipioatencion','nombremunicipioatencion']]
#depuramos la tabla solo para dejar un insidencia de cada registro
depurar_MUN = municipios.drop_duplicates(subset='codigomunicipioatencion')
# Mostrar los resultados
#print(depurar_DPTO)
#convertimos el data frame en un json 
depurar_DPTO.to_json("Tablas/municipios.json", orient='records')