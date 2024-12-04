import tkinter as tk
from tkinter import messagebox
from models import Sesion  # Importar el modelo de Sesion

class SessionForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Formulario de Sesión")
        self.geometry("400x400")

        # Etiquetas y campos de entrada para la sesión
        tk.Label(self, text="ID del Perro:").grid(row=0, column=0, padx=10, pady=10)
        self.perro_id_entry = tk.Entry(self)  # Aquí el usuario puede ingresar el perro_id manualmente
        self.perro_id_entry.grid(row=0, column=1)

        tk.Label(self, text="Fecha:").grid(row=1, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=1, column=1)

        tk.Label(self, text="Descripción:").grid(row=2, column=0, padx=10, pady=10)
        self.description_entry = tk.Text(self, height=5, width=30)  # Cambiado a campo Text
        self.description_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self, text="Duración (minutos):").grid(row=3, column=0, padx=10, pady=10)
        self.duration_entry = tk.Entry(self)
        self.duration_entry.grid(row=3, column=1)

        tk.Label(self, text="Costo:").grid(row=4, column=0, padx=10, pady=10)
        self.cost_entry = tk.Entry(self)
        self.cost_entry.grid(row=4, column=1)

        # Botón para guardar la sesión
        save_button = tk.Button(self, text="Guardar Sesión", command=self.save_session)
        save_button.grid(row=5, column=0, columnspan=2, pady=20)

    def save_session(self):
        """Guardar la sesión en la base de datos."""
        perro_id = self.perro_id_entry.get()  # ID del perro
        fecha = self.date_entry.get()
        duracion = self.duration_entry.get()
        descripcion = self.description_entry.get("1.0", tk.END).strip()  # Obtener texto del campo Text
        costo = self.cost_entry.get()  # Ahora estamos obteniendo el costo correctamente

        # Verificar que todos los campos requeridos estén completos
        if perro_id and fecha and descripcion and duracion and costo:
            try:
                # Crear una instancia de Sesion y guardarla en la base de datos usando perro_id y costo
                sesion = Sesion(perro_id=perro_id, fecha=fecha, duracion=duracion, descripcion=descripcion, costo=costo)
                sesion.save()

                messagebox.showinfo("Éxito", "Sesión guardada exitosamente.")
                self.destroy()  # Cerrar el formulario después de guardar
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar la sesión: {str(e)}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
