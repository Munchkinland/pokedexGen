# Pokédex Interactiva

## Descripción

La **Pokédex Interactiva** es una aplicación de escritorio desarrollada en Python utilizando PyQt5, que permite a los usuarios buscar y comparar diferentes Pokémon. La aplicación integra la API de OpenAI y la API de PokeAPI para proporcionar información detallada sobre los Pokémon seleccionados y generar comparaciones entre ellos.

### Características principales:

- **Búsqueda de Pokémon:** Permite buscar información detallada sobre cualquier Pokémon utilizando su nombre. Los datos incluyen estadísticas base, habilidades, tipos, movimientos principales, entre otros.

- **Comparación de Pokémon:** Compara dos Pokémon seleccionados y genera una respuesta automatizada que predice cuál de ellos ganaría en una batalla, proporcionando una breve explicación.

- **Interfaz Gráfica de Usuario (GUI):** La aplicación cuenta con una interfaz amigable y estilizada que facilita la interacción del usuario. Incluye áreas de texto para mostrar la información, botones de búsqueda y comparación, y etiquetas para visualizar las imágenes de los Pokémon.

- **Estilo personalizado:** Se han aplicado estilos personalizados inspirados en el tema Pokémon, proporcionando una experiencia visual atractiva y coherente con la temática.

## Tecnologías y Librerías Utilizadas

- **Python 3.9+**
- **PyQt5:** Para la creación de la interfaz gráfica de usuario.
- **OpenAI API:** Para generar respuestas automáticas basadas en la comparación de Pokémon.
- **PokeAPI:** Para obtener datos detallados de cada Pokémon.
- **Requests:** Para realizar solicitudes HTTP a la PokeAPI y descargar imágenes de los Pokémon.
- **QTimer:** Para manejar eventos de tiempo y actualizar la interfaz en tiempo real.

## Estructura del Proyecto

- **`services/openai_service.py`**: Contiene la clase `OpenAIService` que se encarga de interactuar con la API de OpenAI.
- **`services/pokeapi_service.py`**: Contiene la clase `PokeAPIService` que maneja las solicitudes a la PokeAPI para obtener datos de Pokémon.
- **`ui/`**: Carpeta donde se almacenan los recursos visuales como íconos.
- **`pokedex_style.py`**: Define los estilos personalizados aplicados a los distintos componentes de la interfaz.

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/usuario/pokedex-interactiva.git
    cd pokedex-interactiva
    ```

2. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configurar la API Key de OpenAI:**
   - Abre el archivo `main.py`.
   - Reemplaza `"your_openai_api_key_here"` con tu clave de API de OpenAI.

4. **Ejecutar la aplicación:**

    ```bash
    python main.py
    ```

## Uso

- **Buscar Pokémon:** Ingresa el nombre de un Pokémon en los campos de búsqueda y presiona el botón correspondiente.
- **Comparar Pokémon:** Después de realizar las búsquedas de dos Pokémon, presiona el botón "Comparar Pokémon" para ver cuál de ellos ganaría en una batalla según la inteligencia artificial.
- **Visualizar resultados:** La información detallada de cada Pokémon y la comparación se mostrarán en la interfaz gráfica, incluyendo las imágenes correspondientes.

## Contribución

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes ideas para mejorar el proyecto, por favor abre un issue o un pull request en GitHub.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

¡Disfruta explorando el mundo de los Pokémon con la Pokédex Interactiva!

## Requisitos

Este archivo `requirements.txt` incluye las versiones recomendadas de las librerías necesarias para ejecutar la Pokédex Interactiva:

- `PyQt5==5.15.7`: Para la creación de la interfaz gráfica de usuario.
- `requests==2.31.0`: Para manejar las solicitudes HTTP a la PokeAPI.
- `openai==0.27.8`: Para interactuar con la API de OpenAI y generar respuestas automáticas.

### Contenido del archivo `requirements.txt`

```plaintext
PyQt5==5.15.7
requests==2.31.0
openai==0.27.8
