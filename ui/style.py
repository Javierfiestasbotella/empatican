import tkinter as tk

def apply_style(widget):
    """
    Aplica el estilo estándar a un widget de tkinter.
    """
    widget.configure(
        bg="#f0f0f0",  # Color de fondo
        fg="#333333",  # Color del texto
        font=("Arial", 12)  # Fuente y tamaño
    )

def style_button(button):
    """
    Aplica estilo a los botones.
    """
    button.configure(
        bg="#4CAF50",  # Color de fondo del botón
        fg="#ffffff",  # Color del texto del botón
        font=("Arial", 12, "bold"),  # Fuente del botón
        relief="raised",  # Estilo del botón
        bd=2  # Ancho del borde
    )

def style_label(label):
    """
    Aplica estilo a las etiquetas.
    """
    label.configure(
        bg="#f0f0f0",  # Color de fondo
        fg="#333333",  # Color del texto
        font=("Arial", 12, "bold")  # Fuente de las etiquetas
    )
