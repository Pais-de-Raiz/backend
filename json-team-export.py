import gspread
import json

#---------Permisos archivo drive
# Ruta al archivo JSON de credenciales descargado
credenciales = 'credentials/paisderaiz-0c89982b0273.json'


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


# Abre el archivo de Google Sheets (reemplaza 'Nombre de tu archivo' con el nombre de tu archivo)
spreadsheet = gc.open("paisderaiz-info")

# Selecciona la hoja específica por nombre (reemplaza 'Nombre de tu hoja' con el nombre de tu hoja)
worksheet = spreadsheet.worksheet("equipo")


# # Obtener datos
data = worksheet.get_all_values()

# Lista para almacenar objetos de servicios
# objetos_servicios = []

# Define la estructura de salida
output = {"equipo": []}

# Itera sobre las filas de datos (omitimos la primera fila si contiene encabezados)
for row in data[1:]:
    equipo = {
        'nombres': row[0],
        'apellidos': row[1],
        'cargo': row[2],
        'linkedin': row[3],
        'foto': row[4],
    }
    output["equipo"].append(equipo)

# Nombre del archivo de salida
nombre_archivo = "equipo.json"

# Abrir el archivo en modo escritura
with open(nombre_archivo, 'w') as archivo_json:
    # Utilizar json.dump() para escribir el diccionario en el archivo
    json.dump(output, archivo_json)

print(f"Se ha exportado el diccionario al archivo {nombre_archivo}")