import platform

# Sistema operativo
sistema_operativo = platform.system()
print(f"Sistema operativo: {sistema_operativo}")

# Versión del sistema operativo
version_sistema = platform.version()
print(f"Versión del sistema operativo: {version_sistema}")

# Arquitectura de la máquina
arquitectura = platform.machine()
print(f"Arquitectura de la máquina: {arquitectura}")
