import tkinter as tk
from tkinter import messagebox
from ui.style import style_button, style_label
from models import Seminario

class SeminarForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("SGE(Sistema de Gestión de Empatican)")
        self.geometry("400x400")
        self.configure(bg="#f0f0f0")
        self.iconbitmap("empatican/logemp.ico")  # Ruta a tu archivo .ico

        # Etiquetas y campos de entrada
        tk.Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self, text="Client ID:").grid(row=1, column=0, padx=10, pady=10)
        self.client_id_entry = tk.Entry(self)
        self.client_id_entry.grid(row=1, column=1)

        tk.Label(self, text="Description:").grid(row=2, column=0, padx=10, pady=10)

        # Cambiar Entry a Text para descrption
        self.description_entry = tk.Text(self, height=5, width=30)  # Aquí definimos el tamaño
        self.description_entry.grid(row=2, column=1, padx=10, pady=10)

        # Al guardar
        notas = self.description_entry.get("1.0", tk.END)  # Obtener texto desde la primera línea hasta el final


        tk.Label(self, text="Date:").grid(row=4, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=4, column=1)

        tk.Label(self, text="Cost:").grid(row=5, column=0, padx=10, pady=10)
        self.cost_entry = tk.Entry(self)
        self.cost_entry.grid(row=5, column=1)

        # Botón para guardar
        save_button = tk.Button(self, text="Save Seminar", command=self.save_seminar)
        style_button(save_button)
        save_button.grid(row=6, column=0, columnspan=2, pady=20)

    def save_seminar(self):
        name = self.name_entry.get()
        #description = self.description_entry.get()
        description = self.description_entry.get("1.0", tk.END).strip()  # Obtener texto desde la primera línea hasta el final
        client_id = self.client_id_entry.get()
        date = self.date_entry.get()
        cost = self.cost_entry.get()

        if name and date:
            # Crear una instancia de Seminario y guardar en la base de datos
            seminario = Seminario(nombre=name, descripcion=description,cliente_id=client_id, fecha=date, costo=cost)
            seminario.save()

            messagebox.showinfo("Success", "Seminar saved successfully!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Name and Date are required.")
