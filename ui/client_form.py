import tkinter as tk
from tkinter import messagebox
from ui.style import style_button, style_label
from models import Cliente

class ClientForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("SGE(Sistema de Gestión de Empatican)")
        self.geometry("400x300")
        self.iconbitmap("Gestion-App/empatican/logemp.ico")  # Ruta a tu archivo .ico

        self.configure(bg="#f0f0f0")

        # Etiquetas y campos de entrada
        tk.Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self, text="Phone:").grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self, text="Email:").grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self, text="Address:").grid(row=3, column=0, padx=10, pady=10)
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=3, column=1)

        # Botón para guardar
        #save_button = tk.Button(self, text="Save Client", command=self.save_client)
        #save_button = tk.Button(self, text="Save Client", command=self.save_client, bg="#FF8C00", fg="#ffffff", font=("Arial", 12, "bold"))
        save_button = tk.Button(self, text="Save Client", command=self.save_client, 
                        bg="#FF8C00",  # Fondo normal
                        fg="#ffffff",  # Texto normal
                        activebackground="#FF4500",  # Fondo cuando está activo
                        activeforeground="#ffffff",  # Texto cuando está activo
                        font=("Arial", 12, "bold"))
        style_button(save_button)
        save_button.grid(row=4, column=0, columnspan=2, pady=20 )

    def save_client(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name:
            # Crear una instancia de Cliente y guardar en la base de datos (tabla clientes_empatican)
            cliente = Cliente(nombre=name, telefono=phone, email=email, direccion=address)
            cliente.save()

            messagebox.showinfo("Success", "Client saved successfully!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Name is required.")
