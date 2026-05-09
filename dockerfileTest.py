import os

# Nombre del archivo a buscar
archivo = "Dockerfile"

# Verificar la existencia del archivo
if os.path.exists(archivo):
    print("Dockerfile encontrado")
else:
    print("Dockerfile no encontrado")