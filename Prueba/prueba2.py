import gspread
import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

#-------------Drive
# Define the Google Drive API scopes and service account file path
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = "paisderaiz-0c89982b0273.json"

# Create credentials using the service account file
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Google Drive service
drive_service = build('drive', 'v3', credentials=credentials)

def create_folder(folder_name, parent_folder_id=None):
    """Create a folder in Google Drive and return its ID."""
    folder_metadata = {
        'name': folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        'parents': [parent_folder_id] if parent_folder_id else []
    }

    created_folder = drive_service.files().create(
        body=folder_metadata,
        fields='id'
    ).execute()

#---------Permisos archivo drive
# Ruta al archivo JSON de credenciales descargado
credenciales = 'paisderaiz-0c89982b0273.json'


# ID del documento de Google Sheets
id_documento = '1LlilYZIDVp4al8WGNr1sdZg-OuQW6jSK5zii6zHAVwU'


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
        'imagen': row[3],
        'categoria': row[4],
        'linea': row[5],
    }
    output["servicios"].append(servicio)

# Nombre del archivo de salida
nombre_archivo = "servicios2.json"

# Abrir el archivo en modo escritura
with open(nombre_archivo, 'w') as archivo_json:
    # Utilizar json.dump() para escribir el diccionario en el archivo
    json.dump(output, archivo_json)

print(f"Se ha exportado el diccionario al archivo {nombre_archivo}")

create_folder("MyNewFolder")