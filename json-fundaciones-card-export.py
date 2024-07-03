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

# Accede a la pestaña específica por su nombre
nombre_de_la_pestaña = "fundaciones-cards"
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
        "card": {
            'imgSrc': row[0],
            'imgAlt': row[1],
            'title': row[2],
            'location': row[3],
            'text': row[4],
            'btnText': row[5],
            'btnLink': row[6],
        }
    }
    output.append(card_data)

# Nombre del archivo de salida
nombre_archivo = "fundaciones-cards.json"

# Abrir el archivo en modo escritura
with open(nombre_archivo, 'w') as archivo_json:
    # Utilizar json.dump() para escribir el diccionario en el archivo
    json.dump(output, archivo_json)

print(f"Se ha exportado el diccionario al archivo {nombre_archivo}")