import json
import gspread
from google.oauth2.service_account import Credentials

# Define los ámbitos necesarios para acceder a Google Sheets y Google Drive
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.readonly"
]

# Lee las credenciales desde el archivo client_secrets.json
with open('client_secrets.json') as f:
    creds_dict = json.load(f)  # Asegúrate de que el archivo tiene un JSON válido

creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
gc = gspread.authorize(creds)

# Abre tu hoja de cálculo por su ID
id_documento = '1LlilYZIDVp4al8WGNr1sdZg-OuQW6jSK5zii6zHAVwU'
sh = gc.open_by_key(id_documento)

# Tu lógica aquí...
hoja_de_calculo = gc.open_by_key(id_documento)
hoja = hoja_de_calculo.sheet1  # Puedes cambiar el nombre de la hoja si es necesario

# Accede a la pestaña específica por su nombre
nombre_de_la_pestaña = "equipo"
pestaña = hoja_de_calculo.worksheet(nombre_de_la_pestaña)


# # Obtener datos
datos = pestaña.get_all_values()

# Lista para almacenar objetos de servicios
# objetos_servicios = []

# Define la estructura de salida
output = []

# Itera sobre las filas de datos (omitimos la primera fila si contiene encabezados)
for row in datos[1:]:
    card_data = {
        "person": {
            'nombre': row[0],
            'cargo': row[1],
            'linkedin': row[2],
            'foto': row[3],
        }
    }
    output.append(card_data)

# Nombre del archivo de salida
nombre_archivo = "equipo.json"

# Abrir el archivo en modo escritura
with open(nombre_archivo, 'w') as archivo_json:
    # Utilizar json.dump() para escribir el diccionario en el archivo
    json.dump(output, archivo_json)

print(f"Se ha exportado el diccionario al archivo {nombre_archivo}")