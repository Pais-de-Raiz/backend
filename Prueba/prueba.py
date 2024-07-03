import gspread
import json
import os
from google.oauth2 import service_account
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


# Ruta al archivo JSON de credenciales descargado
credenciales = 'credentials/paisderaiz-0c89982b0273.json'


# ID del documento de Google Sheets
id_documento = '1LlilYZIDVp4al8WGNr1sdZg-OuQW6jSK5zii6zHAVwU'

# ID del folder
folder_id = "12xa6lSWNmFb-gSDTg85bYDKijnwv6jeN"

# Autenticación
gc = gspread.service_account(filename=credenciales)

# Solicitud de acceso a documento
sh = gc.open_by_key(id_documento)

# credenciales = service_account.Credentials.from_service_account_file(credenciales)
# cliente = gspread.authorize(credenciales)


hoja_de_calculo = gc.open_by_key(id_documento)
hoja = hoja_de_calculo.sheet1  # Puedes cambiar el nombre de la hoja si es necesario

# # Obtener datos
datos = hoja.get_all_values()

# Lista para almacenar objetos de servicios
# objetos_servicios = []

# Define la estructura de salida
output = {"servicios": []}

# Itera sobre las filas de datos (omitimos la primera fila si contiene encabezados)
for row in datos[1:]:
    servicio = {
        'servicio': row[0],
        'descripcion': row[1],
        'fundacion': row[2],
        'imagen': row[3]
    }
    output["servicios"].append(servicio)

# Nombre del archivo de salida
nombre_archivo = "servicios-2.json"

# Abrir el archivo en modo escritura
with open(nombre_archivo, 'w') as archivo_json:
    # Utilizar json.dump() para escribir el diccionario en el archivo
    json.dump(output, archivo_json)

print(f"Se ha exportado el diccionario al archivo {nombre_archivo}")

# Configurar la autenticación con Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

# Inicializar el objeto GoogleDrive con la autenticación
drive = GoogleDrive(gauth)


# Crear un archivo en memoria y cargar el contenido JSON
archivo = drive.CreateFile({'title': nombre_archivo, 'parents': [{'id': folder_id}]})
archivo.UploadContent(contenido_json, mimetype='application/json')

print(f"Archivo JSON creado y guardado en Google Drive con ID: {archivo['id']}")
