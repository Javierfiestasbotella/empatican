import tkinter as tk
from tkinter import PhotoImage, messagebox
from ui.client_form import ClientForm
from ui.dog_form import DogForm
from ui.session_form import SessionForm
from ui.seminar_form import SeminarForm
from ui.payment_form import PaymentForm
from ui.client_card_form import ClientCardForm
from ui.style import style_button

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SGE(Sistema de Gestión de Empatican)")
        self.geometry("800x600")
        self.iconbitmap("Gestion-App/empatican/logemp.ico")  # Ruta a tu archivo .ico

        # Cargar imagen de fondo
        self.background_image = PhotoImage(file="Gestion-App/empatican/fondo4.png")
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)  # Expandir la imagen a toda la ventana
        self.configure(bg="#f0f0f0")
        background_label.lower()

        # Título principal
        title_label = tk.Label(self, text="Sistema de Gestión de Empatican", bg="#f0f0f0", fg="#FF4500", font=("Helvetica", 24, "bold italic"))
        title_label.pack(pady=20)

        # Color del fondo de los botones
        button_color = "#FF4500"

        # Botones para acceder a las diferentes secciones
        client_button = tk.Button(self, text="Gestionar Clientes", command=self.open_client_form, bg=button_color, fg="#ffffff", font=("Arial", 12, "bold"), relief="raised", bd=5)
        client_button.pack(pady=8, padx=20, anchor="center")

        dog_button = tk.Button(self, text="Gestionar Perros", command=self.open_dog_form, bg=button_color, fg="#ffffff", font=("Arial", 12, "bold"), relief="raised", bd=5)
        dog_button.pack(pady=8, padx=20, anchor="center")

        session_button = tk.Button(self, text="Gestionar Sesiones", command=self.open_session_form, bg=button_color, fg="#ffffff", font=("Arial", 12, "bold"), relief="raised", bd=5)
        session_button.pack(pady=8, padx=20, anchor="center")

        seminar_button = tk.Button(self, text="Gestionar Seminarios", command=self.open_seminar_form, bg=button_color, fg="#ffffff", font=("Arial", 12, "bold"), relief="raised", bd=5)
        seminar_button.pack(pady=8, padx=20, anchor="center")

        payment_button = tk.Button(self, text="Gestionar Pagos", command=self.open_payment_form, bg=button_color, fg="#ffffff", font=("Arial", 12, "bold"), relief="raised", bd=5)
        payment_button.pack(pady=8, padx=20, anchor="center")

        client_card_button = tk.Button(self, text="Ver Ficha del Cliente", command=self.open_client_card_form, bg=button_color, fg="#ffffff", font=("Arial", 12, "bold"), relief="raised", bd=5)
        client_card_button.pack(pady=8, padx=20, anchor="center")

    def open_client_form(self):
        form = ClientForm(self)
        form.grab_set()

    def open_dog_form(self):
        form = DogForm(self)
        form.grab_set()

    def open_session_form(self):
        form = SessionForm(self)
        form.grab_set()

    def open_seminar_form(self):
        form = SeminarForm(self)
        form.grab_set()

    def open_payment_form(self):
        form = PaymentForm(self)
        form.grab_set()

    def open_client_card_form(self):
        form = ClientCardForm(self)
        form.grab_set()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()