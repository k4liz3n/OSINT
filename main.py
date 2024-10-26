import requests
from googlesearch import search

opcion = int(input("Qué acción quieres hacer\n[1]Instagram\n[2]Github\n[3]Linkedin\n[4]Twitter(X)\n[5]Buscar PDF's\n[6]Buscar en Google\n[7]Busqueda completa\nTu elección: "))
nombre = input("Introduce el nombre de usuario a comprobar: ")

def instagram(nombre):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    url_usuario = requests.get(f"https://www.instagram.com/{nombre}/", headers=headers)

    if url_usuario.status_code == 200:
        if "This page isn't available" in url_usuario.text or "Esta página no está disponible." in url_usuario.text:
            print("Usuario no encontrado.")
        else:
            print(f"Usuario encontrado: https://www.instagram.com/{nombre}/")
    else:
        print("Error en la solicitud:", url_usuario.status_code)

def github(nombre):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    url_usuario = requests.get(f"https://www.github.com/{nombre}/", headers=headers)

    if url_usuario.status_code == 200:
        print(f"Usuario encontrado: https://www.github.com/{nombre}/")
    else:
        print("Usuario no encontrado.")

def linkedin(nombre):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    url_usuario = requests.get(f"https://es.linkedin.com/in/{nombre}/", headers=headers)
    
    if url_usuario.status_code == 200:
        print(f"Usuario encontrado: https://es.linkedin.com/in/{nombre}/")
    else:
        print("Usuario no encontrado.")

def twitter(nombre):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        url_usuario = requests.get(f"https://twitter.com/{nombre}/", headers=headers)
        
        if url_usuario.status_code == 200:
            if ("Esta cuenta no existe" in url_usuario.text or 
                "No hemos encontrado esta página" in url_usuario.text or 
                "Página no encontrada" in url_usuario.text or 
                "User not found" in url_usuario.text):
                print("Usuario no encontrado. Intenta hacer otra búsqueda.")
            else:
                print(f"Usuario encontrado: https://twitter.com/{nombre}/")
        else:
            print("Usuario no encontrado.")
    
    except requests.exceptions.RequestException as e:
        print("Ocurrió un error en la solicitud:", str(e))

def buscar_pdf(nombre):
    try:
        resultados = search(f"{nombre} filetype:pdf", num_results=10)
        print("\nResultados de la búsqueda de PDF:")
        for i, resultado in enumerate(resultados, start=1):
            print(f"{i}. {resultado}")
    except Exception as e:
        print(f"Error: {e}")

def buscar_en_google(nombre):
    try:
        resultados = search(nombre, num_results=10)
        print("\nResultados de la búsqueda normal:")
        for i, resultado in enumerate(resultados, start=1):
            print(f"{i}. {resultado}")
    except Exception as e:
        print(f"Error: {e}")

if opcion == 1:
    instagram(nombre)
elif opcion == 2:
    github(nombre)
elif opcion == 3:
    linkedin(nombre)
elif opcion == 4:
    twitter(nombre)
elif opcion == 5:
    buscar_pdf(nombre)
elif opcion == 6:
    buscar_en_google(nombre)
elif opcion == 7:
    instagram(nombre)
    github(nombre)
    linkedin(nombre)
    twitter(nombre)
    buscar_pdf(nombre)
    buscar_en_google(nombre)
else:
    print("Opción no válida. Salida.")
