import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from dotenv import load_dotenv
import os

def main():
    # Cargar variables de entorno desde .env
    load_dotenv()

    # Inicia la aplicación de PyQt
    app = QApplication(sys.argv)

    # Obtener la API key de OpenAI desde variables de entorno
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY no está configurada en el archivo .env")
        sys.exit(1)

    # Crea la ventana principal
    window = MainWindow(api_key)
    window.show()

    # Ejecuta el loop de eventos de la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()