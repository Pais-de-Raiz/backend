from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def autenticar_con_credenciales_json(json_file_path):
    gauth = GoogleAuth()
    gauth.credentials = None

    # Cargar las credenciales desde el archivo JSON
    gauth.LoadCredentialsFile(json_file_path)

    if gauth.credentials is None:
        # Si no hay credenciales, solicitar autenticación
        gauth.LocalWebserverAuth()

    elif gauth.access_token_expired:
        # Si las credenciales han expirado, refrescarlas
        gauth.Refresh()

    else:
        # Las credenciales son válidas
        gauth.Authorize()

    # Guardar las credenciales para la próxima ejecución
    gauth.SaveCredentialsFile(json_file_path)

    drive = GoogleDrive(gauth)
    return drive

def crear_carpeta_en_drive(nombre_carpeta, drive):
    folder = drive.CreateFile({'title': nombre_carpeta, 'mimeType': 'application/vnd.google-apps.folder'})
    folder.Upload()
    print(f'Se creó la carpeta "{nombre_carpeta}" en Google Drive con el ID: {folder["id"]}')

if __name__ == "__main__":
    nombre_carpeta = "MiNuevaCarpeta"
    json_file_path = "paisderaiz-0c89982b0273.json"  # Reemplaza con la ruta real de tu archivo JSON
    
    # Autenticar con las credenciales del archivo JSON y obtener el objeto GoogleDrive
    drive = autenticar_con_credenciales_json(json_file_path)

    # Crear la carpeta en Google Drive
    crear_carpeta_en_drive(nombre_carpeta, drive)
