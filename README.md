# Social Media and PDF Search Script

Este script permite buscar la existencia de un nombre de usuario en diferentes plataformas sociales y realizar búsquedas de archivos PDF o consultas en Google. Ideal para comprobar si un nombre de usuario está registrado en redes sociales populares o encontrar información relacionada con ese nombre en la web.

## Características

- **Instagram**: Verifica si el nombre de usuario está registrado en Instagram.
- **GitHub**: Comprueba si existe una cuenta de GitHub con el nombre de usuario proporcionado.
- **LinkedIn**: Busca un perfil en LinkedIn asociado al nombre de usuario.
- **Twitter**: Comprueba si existe una cuenta de Twitter (X) con ese nombre de usuario.
- **Búsqueda de PDFs**: Realiza una búsqueda en Google para encontrar archivos PDF relacionados con el nombre.
- **Búsqueda en Google**: Busca el nombre directamente en Google para obtener información general.
- **Búsqueda Completa**: Ejecuta todas las funciones anteriores para obtener un resultado completo.

## Requisitos

- **Python 3.6 o superior**
- Librerías necesarias:
  - `requests`
  - `googlesearch-python` (puedes instalarlo usando `pip install googlesearch-python`)

## Uso

1. Clona el repositorio o descarga el script:
    ```bash
    git clone https://github.com/tu-repo/social-media-search.git
    cd social-media-search
    ```

2. Instala las dependencias requeridas:
    ```bash
    pip install requests googlesearch-python
    ```

3. Ejecuta el script:
    ```bash
    python social_media_search.py
    ```

4. Selecciona una de las opciones proporcionadas:

    - **1**: Buscar en Instagram
    - **2**: Buscar en GitHub
    - **3**: Buscar en LinkedIn
    - **4**: Buscar en Twitter (X)
    - **5**: Buscar PDFs relacionados en Google
    - **6**: Realizar una búsqueda normal en Google
    - **7**: Ejecutar todas las funciones anteriores de forma completa
