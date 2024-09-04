from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QScrollArea
from .pokedex_style import apply_pokedex_styles
from services.pokeapi_service import PokeAPIService
from services.openai_service import OpenAIService
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import requests

class MainWindow(QMainWindow):
    def __init__(self, openai_api_key):
        super().__init__()
        self.setWindowTitle("Pokédex Interactiva")
        self.resize(400, 600)
        self.pokeapi_service = PokeAPIService()
        self.openai_service = OpenAIService(openai_api_key)

        # Variables para almacenar la información de los Pokémon
        self.pokemon_data_1 = None
        self.pokemon_data_2 = None

        self.init_ui()

    def init_ui(self):
        # Configurar layout y widgets
        self.layout = QVBoxLayout()

        # Widgets de búsqueda para el primer Pokémon
        self.search_label_1 = QLabel("Buscar Pokémon 1")
        self.search_input_1 = QLineEdit()
        self.search_button_1 = QPushButton("Buscar Pokémon 1")
        self.search_button_1.clicked.connect(lambda: self.search_pokemon(1))

        # Widgets de búsqueda para el segundo Pokémon
        self.search_label_2 = QLabel("Buscar Pokémon 2")
        self.search_input_2 = QLineEdit()
        self.search_button_2 = QPushButton("Buscar Pokémon 2")
        self.search_button_2.clicked.connect(lambda: self.search_pokemon(2))

        # Botón para comparar los Pokémon
        self.compare_button = QPushButton("Comparar Pokémon")
        self.compare_button.clicked.connect(self.compare_pokemons)

        # Área de resultados
        self.result_label = QLabel("Comparación de Pokémon")
        self.response_area_1 = QLabel()
        self.response_area_2 = QLabel()
        self.response_area_1.setWordWrap(True)
        self.response_area_2.setWordWrap(True)

        self.image_label_1 = QLabel()
        self.image_label_1.setAlignment(Qt.AlignCenter)
        self.image_label_2 = QLabel()
        self.image_label_2.setAlignment(Qt.AlignCenter)

        # Añadir widgets al layout
        self.layout.addWidget(self.search_label_1)
        self.layout.addWidget(self.search_input_1)
        self.layout.addWidget(self.search_button_1)
        self.layout.addWidget(self.search_label_2)
        self.layout.addWidget(self.search_input_2)
        self.layout.addWidget(self.search_button_2)
        self.layout.addWidget(self.compare_button)
        self.layout.addWidget(self.result_label)

        # Crear una zona de desplazamiento para los resultados
        self.scroll_area = QScrollArea()
        self.scroll_area_widget = QWidget()
        self.scroll_area_layout = QVBoxLayout()

        self.scroll_area_layout.addWidget(self.image_label_1)
        self.scroll_area_layout.addWidget(self.response_area_1)
        self.scroll_area_layout.addWidget(self.image_label_2)
        self.scroll_area_layout.addWidget(self.response_area_2)

        self.scroll_area_widget.setLayout(self.scroll_area_layout)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.scroll_area.setWidgetResizable(True)

        self.layout.addWidget(self.scroll_area)

        # Crear contenedor principal
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Aplicar estilos a los widgets y contenedores
        self.apply_styles()

    def apply_styles(self):
        # Aplicar estilos a los widgets
        widgets = [
            self.search_label_1, self.search_input_1, self.search_button_1,
            self.search_label_2, self.search_input_2, self.search_button_2,
            self.compare_button, self.result_label,
            self.response_area_1, self.response_area_2,
            self.scroll_area_widget, self.centralWidget()
        ]

        for widget in widgets:
            apply_pokedex_styles(widget)

    def search_pokemon(self, pokemon_number):
        if pokemon_number == 1:
            pokemon_name = self.search_input_1.text()
            response_area = self.response_area_1
            image_label = self.image_label_1
            self.pokemon_data_1 = self.pokeapi_service.get_pokemon_data(pokemon_name)
            data = self.pokemon_data_1
        else:
            pokemon_name = self.search_input_2.text()
            response_area = self.response_area_2
            image_label = self.image_label_2
            self.pokemon_data_2 = self.pokeapi_service.get_pokemon_data(pokemon_name)
            data = self.pokemon_data_2

        if data:
            # Extrayendo información adicional del Pokémon
            pokemon_id = data.get('id')
            height = data.get('height') / 10  # Altura en metros
            weight = data.get('weight') / 10  # Peso en kilogramos
            types = ", ".join([t['type']['name'].capitalize() for t in data['types']])
            abilities = ", ".join([a['ability']['name'].capitalize() for a in data['abilities']])
            stats = "\n".join([f"{s['stat']['name'].capitalize()}: {s['base_stat']}" for s in data['stats']])
            moves = ", ".join([m['move']['name'].capitalize() for m in data['moves'][:5]])  # Muestra solo los primeros 5 movimientos

            # Formateando el mensaje de detalles
            details = (
                f"ID: {pokemon_id}\n"
                f"Nombre: {data['name'].capitalize()}\n"
                f"Altura: {height} m\n"
                f"Peso: {weight} kg\n"
                f"Tipos: {types}\n"
                f"Habilidades: {abilities}\n"
                f"Estadísticas Base:\n{stats}\n"
                f"Movimientos Principales: {moves}"
            )

            response_area.setText(details)

            # Mostrar imagen del Pokémon
            image_url = data['sprites']['front_default']
            if image_url:
                pixmap = QPixmap()
                pixmap.loadFromData(requests.get(image_url).content)
                image_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            else:
                image_label.clear()
        else:
            response_area.setText("Pokémon no encontrado")
            image_label.clear()

    def compare_pokemons(self):
        if self.pokemon_data_1 and self.pokemon_data_2:
            prompt = f"Compara las habilidades y características de los Pokémon {self.pokemon_data_1['name']} y {self.pokemon_data_2['name']}."
            ai_response = self.openai_service.generate_response(prompt)
            comparison_result = f"Comparación:\n{ai_response}"
            self.result_label.setText(comparison_result)
        else:
            self.result_label.setText("Por favor, busca dos Pokémon antes de comparar.")
