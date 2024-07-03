import json
import gspread
from google.oauth2.service_account import Credentials

# Lee las credenciales desde el archivo client_secrets.json
with open('client_secrets.json') as f:
    creds_dict = json.load(f)  # Asegúrate de que el archivo tiene un JSON válido

creds = Credentials.from_service_account_info(creds_dict)
gc = gspread.authorize(creds)

# Abre tu hoja de cálculo por su ID
id_documento = 'your-google-sheet-id'
sh = gc.open_by_key(id_documento)

# Tu lógica aquí...
