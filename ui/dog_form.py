import tkinter as tk
from tkinter import messagebox, filedialog
from ui.style import style_button, style_label
from models import Perro
import os
from shutil import copyfile  # Para copiar la imagen seleccionada a la carpeta de imágenes

class DogForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("SGE (Sistema de Gestión de Empatican)")
        self.geometry("400x500")
        self.configure(bg="#f0f0f0")
        self.iconbitmap("empatican/logemp.ico")  # Ruta a tu archivo .ico

        # Etiquetas y campos de entrada
        tk.Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self, text="Breed:").grid(row=1, column=0, padx=10, pady=10)
        self.breed_entry = tk.Entry(self)
        self.breed_entry.grid(row=1, column=1)

        tk.Label(self, text="Age:").grid(row=2, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=2, column=1)

        tk.Label(self, text="Client ID:").grid(row=3, column=0, padx=10, pady=10)
        self.client_id_entry = tk.Entry(self)
        self.client_id_entry.grid(row=3, column=1)

        # Etiqueta y campo para notas
        tk.Label(self, text="Notas:").grid(row=4, column=0, padx=10, pady=10)

        # Cambiar Entry a Text para notas
        self.notes_text = tk.Text(self, height=5, width=30)  # Aquí definimos el tamaño
        self.notes_text.grid(row=4, column=1, padx=10, pady=10)

        # Campo para la imagen
        tk.Label(self, text="Foto del Perro:").grid(row=5, column=0, padx=10, pady=10)
        self.foto_ruta_label = tk.Label(self, text="No hay imagen seleccionada")
        self.foto_ruta_label.grid(row=5, column=1, padx=10, pady=10)

        self.seleccionar_foto_btn = tk.Button(self, text="Seleccionar Foto", command=self.seleccionar_foto)
        style_button(self.seleccionar_foto_btn)
        self.seleccionar_foto_btn.grid(row=6, column=0, columnspan=2, pady=10)

        # Botón para guardar
        save_button = tk.Button(self, text="Save Dog", command=self.save_dog)
        style_button(save_button)
        save_button.grid(row=7, column=0, columnspan=2, pady=20)

        self.foto_path = None  # Aquí almacenamos la ruta de la imagen seleccionada

    def seleccionar_foto(self):
        """
        Abrir un diálogo para seleccionar la imagen desde el ordenador.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            self.foto_path = file_path
            self.foto_ruta_label.config(text=os.path.basename(file_path))  # Mostrar el nombre de la imagen

    def save_dog(self):
        name = self.name_entry.get()
        breed = self.breed_entry.get()
        age = self.age_entry.get()
        client_id = self.client_id_entry.get()
        notes = self.notes_text.get("1.0", tk.END).strip()  # Obtener texto desde la primera línea hasta el final

        if name and client_id:
            try:
                # Verificar si se seleccionó una foto
                if self.foto_path:
                    # Crear la carpeta de imágenes si no existe
                    carpeta_imagenes = os.path.join(os.getcwd(), 'imagenes_perros')
                    if not os.path.exists(carpeta_imagenes):
                        os.makedirs(carpeta_imagenes)

                    # Copiar la imagen seleccionada a la carpeta imagenes_perros
                    nueva_ruta_foto = os.path.join(carpeta_imagenes, os.path.basename(self.foto_path))
                    copyfile(self.foto_path, nueva_ruta_foto)
                    ruta_foto_db = f"imagenes_perros/{os.path.basename(self.foto_path)}"
                else:
                    ruta_foto_db = ""  # Si no se seleccionó foto, el campo queda vacío

                # Crear una instancia de Perro y guardar en la base de datos
                perro = Perro(nombre=name, raza=breed, edad=age, cliente_id=client_id, notas=notes, foto=ruta_foto_db)
                perro.save()

                messagebox.showinfo("Success", "Dog saved successfully!")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save dog: {str(e)}")
        else:
            messagebox.showerror("Error", "Name and Client ID are required.")
