from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

def apply_pokedex_styles(widget):
    # Definir una fuente estándar para el tema Pokémon
    font = QFont("Arial", 11)
    widget.setFont(font)

    # Aplicar estilos según el tipo de widget
    if isinstance(widget, QLabel):
        widget.setStyleSheet("""
            QLabel {
                background-color: #ffffff;
                color: #333333;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
        """)
    elif isinstance(widget, QLineEdit):
        widget.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                padding: 5px;
                border: 2px solid #333333;
                border-radius: 5px;
            }
        """)
    elif isinstance(widget, QPushButton):
        widget.setStyleSheet("""
            QPushButton {
                background-color: #ffcb05;  /* Color amarillo Pokémon */
                border: 2px solid #d3d3d3;
                color: #000000;
                padding: 10px 20px;
                text-align: center;
                font-size: 12px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #fdb927; /* Color amarillo oscuro para hover */
            }
            QPushButton:pressed {
                background-color: #f0a500; /* Color naranja para el estado presionado */
            }
        """)
    elif isinstance(widget, QWidget):
        widget.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;  /* Color de fondo más claro */
            }
        """)

