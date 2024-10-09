import base64

# Función para encriptar texto
def encriptar_texto(texto):
    texto_bytes = texto.encode('utf-8')  # Convertir texto a bytes
    texto_encriptado = base64.b64encode(texto_bytes)  # Codificar en Base64
    return texto_encriptado.decode('utf-8')  # Convertir de bytes a string

# Función para desencriptar texto
def desencriptar_texto(texto_encriptado):
    texto_encriptado_bytes = texto_encriptado.encode('utf-8')  # Convertir texto encriptado a bytes
    texto_desencriptado = base64.b64decode(texto_encriptado_bytes)  # Decodificar de Base64
    return texto_desencriptado.decode('utf-8')  # Convertir de bytes a string

# Función principal
def main():
    while True:
        opcion = input("¿Deseas (e)ncriptar o (d)esencriptar un texto? (o para salir): ").strip().lower()
        
        if opcion == 'e':
            texto = input("Introduce el texto a encriptar: ")
            texto_encriptado = encriptar_texto(texto)
            print(f"Texto encriptado: {texto_encriptado}")
        
        elif opcion == 'd':
            texto_encriptado = input("Introduce el texto a desencriptar: ")
            try:
                texto_desencriptado = desencriptar_texto(texto_encriptado)
                print(f"Texto desencriptado: {texto_desencriptado}")
            except Exception as e:
                print("Error al desencriptar:", e)
        
        elif opcion == 'o':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    main()
