import requests
import dicttoxml
import xml.etree.ElementTree as ET

# URL a la que deseas hacer la solicitud GET
url = 'https://www.datos.gov.co/resource/xfif-myr2.json'

# Realiza la solicitud GET
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de estado 200)
# if response.status_code == 200:
#     # Imprime el contenido de la respuesta
#     print(response.content)
# else:
#     # Imprime un mensaje de error si la solicitud no fue exitosa
#     print(f'Error en la solicitud. Código de estado: {response.status_code}')


root = ET.Element("root")

# Convertir los datos JSON a XML
print(len(response.json()))
# for index in response.json():
#     for key, value in index.items():
#         element = ET.SubElement(root, key)
#         element.text = str(value)

# # Crear un objeto ElementTree
# tree = ET.ElementTree(root)

# # Guardar el archivo XML
# xml_filename = "datos.xml"
# tree.write(xml_filename)

# print(f"Archivo XML '{xml_filename}' guardado correctamente.")