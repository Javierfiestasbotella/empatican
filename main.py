from ui.main_window import MainWindow
import os

# Define BASE_DIR como el directorio donde se encuentra el archivo main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def main():
    """
    Función principal que inicia la aplicación.
    """
    app = MainWindow(BASE_DIR)  # Asegúrate de pasar BASE_DIR aquí
    #app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
