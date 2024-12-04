import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, filedialog
from models import Cliente, Perro, Sesion, Seminario, Pago  # Importar los modelos
from tkinter import PhotoImage
from tkinter import messagebox

class ClientCardForm(tk.Toplevel):
    def __init__(self, parent, cliente_id=None):
        super().__init__(parent)
        self.title("SGE(Sistema de Gestión de Empatican)")
        self.geometry("1300x700")
        self.iconbitmap("empatican/logemp.ico")  # Ruta a tu archivo .ico
        self.configure(bg="#f0f0f0")  # Color de fondo neutro

        self.color_principal = "#FF4500"  # Naranja fuego
        self.color_secundario = "#FFD700"  # Amarillo anaranjado
        self.texto_color = "#333333"  # Texto negro

        self.main_frame = tk.Frame(self, bg="#f0f0f0")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_left_section(self.main_frame)
        self.create_center_section(self.main_frame)
        self.create_right_section(self.main_frame)

        if cliente_id is not None:
            self.load_cliente_data(cliente_id)

    def create_left_section(self, parent):
        left_frame = tk.Frame(parent, bg="#f0f0f0")
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        tk.Label(left_frame, text="Datos del Cliente", font=("Arial", 14, "bold"), bg=self.color_principal, fg="#ffffff").grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

        tk.Label(left_frame, text="Nombre:", bg="#f0f0f0", fg=self.texto_color).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.nombre_entry = tk.Entry(left_frame)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(left_frame, text="Teléfono:", bg="#f0f0f0", fg=self.texto_color).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.telefono_entry = tk.Entry(left_frame)
        self.telefono_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(left_frame, text="Email:", bg="#f0f0f0", fg=self.texto_color).grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = tk.Entry(left_frame)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(left_frame, text="Dirección:", bg="#f0f0f0", fg=self.texto_color).grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.direccion_entry = tk.Entry(left_frame)
        self.direccion_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        tk.Label(left_frame, text="Datos del Perro", font=("Arial", 14, "bold"), bg=self.color_principal, fg="#ffffff").grid(row=5, column=0, columnspan=2, pady=10, sticky="w")

        # Agregamos combobox para los perros
        tk.Label(left_frame, text="Selecciona Perro:", bg="#f0f0f0", fg=self.texto_color).grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.perro_combobox = ttk.Combobox(left_frame, state="readonly")
        self.perro_combobox.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        self.perro_combobox.bind("<<ComboboxSelected>>", self.on_perro_selected)

        tk.Label(left_frame, text="Raza:", bg="#f0f0f0", fg=self.texto_color).grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.perro_raza_entry = tk.Entry(left_frame)
        self.perro_raza_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        tk.Label(left_frame, text="Edad:", bg="#f0f0f0", fg=self.texto_color).grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.perro_edad_entry = tk.Entry(left_frame)
        self.perro_edad_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

        tk.Label(left_frame, text="Foto del Perro:", bg="#f0f0f0", fg=self.texto_color).grid(row=9, column=0, padx=5, pady=5, sticky="w")
        self.foto_label = tk.Label(left_frame, text="No hay foto", bg="#f0f0f0")
        self.foto_label.grid(row=9, column=1, padx=5, pady=5, sticky="w")

    def create_center_section(self, parent):
        # Sección central (sesiones, seminarios, pagos)
        center_frame = tk.Frame(parent, bg="#f0f0f0")
        center_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        # SESIONES
        tk.Label(center_frame, text="Sesiones", font=("Arial", 14, "bold"), bg=self.color_secundario, fg=self.texto_color).grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

        # Menú desplegable para las sesiones
        tk.Label(center_frame, text="Selecciona Sesión:", bg="#f0f0f0", fg=self.texto_color).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.sesion_combobox = ttk.Combobox(center_frame, state="readonly")
        self.sesion_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.sesion_combobox.bind("<<ComboboxSelected>>", self.on_sesion_selected)

        tk.Label(center_frame, text="Duración:", bg="#f0f0f0", fg=self.texto_color).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.sesion_duracion_entry = tk.Entry(center_frame)
        self.sesion_duracion_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(center_frame, text="Descripción:", bg="#f0f0f0", fg=self.texto_color).grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.sesion_descripcion_text = tk.Text(center_frame, height=4, width=30)
        self.sesion_descripcion_text.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # SEMINARIOS
        tk.Label(center_frame, text="Seminarios", font=("Arial", 14, "bold"), bg=self.color_secundario, fg=self.texto_color).grid(row=4, column=0, columnspan=2, pady=10, sticky="w")

        # Menú desplegable para los seminarios
        tk.Label(center_frame, text="Selecciona Seminario:", bg="#f0f0f0", fg=self.texto_color).grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.seminario_combobox = ttk.Combobox(center_frame, state="readonly")
        self.seminario_combobox.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.seminario_combobox.bind("<<ComboboxSelected>>", self.on_seminario_selected)

        tk.Label(center_frame, text="Descripción Seminario:", bg="#f0f0f0", fg=self.texto_color).grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.seminario_descripcion_text = tk.Text(center_frame, height=4, width=30)
        self.seminario_descripcion_text.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        # PAGOS
        tk.Label(center_frame, text="Pagos", font=("Arial", 14, "bold"), bg=self.color_secundario, fg=self.texto_color).grid(row=8, column=0, columnspan=2, pady=10, sticky="w")
        tk.Label(center_frame, text="Fecha Pago:", bg="#f0f0f0", fg=self.texto_color).grid(row=9, column=0, padx=5, pady=5, sticky="w")
        self.pago_fecha_entry = tk.Entry(center_frame)
        self.pago_fecha_entry.grid(row=9, column=1, padx=5, pady=5, sticky="w")

        tk.Label(center_frame, text="Monto:", bg="#f0f0f0", fg=self.texto_color).grid(row=10, column=0, padx=5, pady=5, sticky="w")
        self.pago_monto_entry = tk.Entry(center_frame)
        self.pago_monto_entry.grid(row=10, column=1, padx=5, pady=5, sticky="w")

        tk.Label(center_frame, text="Método de Pago:", bg="#f0f0f0", fg=self.texto_color).grid(row=11, column=0, padx=5, pady=5, sticky="w")
        self.pago_metodo_entry = tk.Entry(center_frame)
        self.pago_metodo_entry.grid(row=11, column=1, padx=5, pady=5, sticky="w")

    def create_right_section(self, parent):
        right_frame = tk.Frame(parent, bg="#f0f0f0")
        right_frame.grid(row=0, column=2, padx=10, pady=10, sticky="n")

        tk.Label(right_frame, text="Lista de Clientes", font=("Arial", 14, "bold"), bg=self.color_principal, fg="#ffffff").pack(pady=10)

        self.clientes_listbox = tk.Listbox(right_frame, height=20, width=30)
        self.clientes_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(right_frame)
        scrollbar.pack(side="right", fill="y")
        self.clientes_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.clientes_listbox.yview)

        search_frame = tk.Frame(right_frame, bg="#f0f0f0")
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Buscar Cliente:", bg="#f0f0f0", fg=self.texto_color).pack(side="left")
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side="left", padx=5)

        search_button = tk.Button(search_frame, text="Buscar", command=self.search_clientes)
        search_button.pack(side="left")

        self.load_clientes()
        self.clientes_listbox.bind("<<ListboxSelect>>", self.on_cliente_selected)

    def load_clientes(self, filter_name=None):
        try:
            clientes = Cliente.get_all()
            if filter_name:
                clientes = [cliente for cliente in clientes if filter_name.lower() in cliente.nombre.lower()]

            self.clientes_listbox.delete(0, tk.END)
            for cliente in clientes:
                self.clientes_listbox.insert(tk.END, f"{cliente.id} - {cliente.nombre}")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la lista de clientes: {str(e)}")

    def search_clientes(self):
        search_term = self.search_entry.get()
        self.load_clientes(filter_name=search_term)

    def on_cliente_selected(self, event):
        seleccion = self.clientes_listbox.curselection()
        if seleccion:
            cliente_seleccionado = self.clientes_listbox.get(seleccion[0])
            cliente_id = int(cliente_seleccionado.split(" - ")[0])
            self.load_cliente_data(cliente_id)

    def load_cliente_data(self, cliente_id):
        self.clear_form()
        cliente = Cliente.get_by_id(cliente_id)
        if cliente:
            self.nombre_entry.insert(0, cliente.nombre)
            self.telefono_entry.insert(0, cliente.telefono)
            self.email_entry.insert(0, cliente.email)
            self.direccion_entry.insert(0, cliente.direccion)

            # Cargar seminarios del cliente
            seminarios = Seminario.get_by_cliente(cliente_id)
            self.seminarios = seminarios  # Guardamos las sesiones cargadas para referencia
            if seminarios:
                self.seminario_combobox['values'] = [seminario.nombre for seminario in seminarios]
                self.seminario_combobox.current(0)
                self.show_seminario_data(seminarios[0])

            # Cargar pagos del cliente
            pagos = Pago.get_by_cliente(cliente_id)
            if pagos:
                self.pago_fecha_entry.delete(0, tk.END)
                self.pago_monto_entry.delete(0, tk.END)
                self.pago_metodo_entry.delete(0, tk.END)
                for pago in pagos:
                    self.pago_fecha_entry.insert(0, pago.fecha)
                    self.pago_monto_entry.insert(0, pago.monto)
                    self.pago_metodo_entry.insert(0, pago.metodo_pago)

        perros = Perro.get_by_cliente(cliente_id)
        if perros:
            self.perros = perros
            self.perro_combobox['values'] = [perro.nombre for perro in perros]
            self.perro_combobox.current(0)
            self.show_perro_data(perros[0])

    def show_perro_data(self, perro):
        self.perro_raza_entry.delete(0, tk.END)
        self.perro_edad_entry.delete(0, tk.END)
        self.perro_raza_entry.insert(0, perro.raza)
        self.perro_edad_entry.insert(0, perro.edad)

        if perro.foto:
            ruta_foto = os.path.join(os.getcwd(), perro.foto)
            ruta_foto = os.path.abspath(ruta_foto)
            if os.path.exists(ruta_foto):
                try:
                    img = PhotoImage(file=ruta_foto)
                    self.foto_label.config(image=img, text="")
                    self.foto_label.image = img
                except Exception as e:
                    print(f"Error al cargar la imagen: {e}")
            else:
                self.foto_label.config(text="No hay foto", image="")

        # Cargar sesiones del perro
        sesiones = Sesion.get_by_perro(perro.id)
        self.sesiones = sesiones  # Guardamos las sesiones cargadas para referencia
        if sesiones:
            self.sesion_combobox['values'] = [sesion['descripcion'] for sesion in sesiones]
            self.sesion_combobox.current(0)
            self.show_sesion_data(sesiones[0])

    def show_sesion_data(self, sesion):
        self.sesion_duracion_entry.delete(0, tk.END)
        self.sesion_descripcion_text.delete("1.0", tk.END)

        self.sesion_duracion_entry.insert(0, sesion['duracion'])
        self.sesion_descripcion_text.insert(tk.END, sesion['descripcion'])

    def show_seminario_data(self, seminario):
        self.seminario_descripcion_text.delete("1.0", tk.END)
        self.seminario_descripcion_text.insert(tk.END, seminario.descripcion)

    def on_perro_selected(self, event):
        selected_index = self.perro_combobox.current()
        if selected_index >= 0:
            perro_seleccionado = self.perros[selected_index]
            self.show_perro_data(perro_seleccionado)

    def on_sesion_selected(self, event):
        selected_index = self.sesion_combobox.current()
        if selected_index >= 0:
            sesion_seleccionada = self.sesiones[selected_index]
            self.show_sesion_data(sesion_seleccionada)

    def on_seminario_selected(self, event):
        selected_index = self.seminario_combobox.current()
        if selected_index >= 0:
            seminario_seleccionado = self.seminarios[selected_index]
            self.show_seminario_data(seminario_seleccionado)

    def clear_form(self):
        self.nombre_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)

        self.perro_raza_entry.delete(0, tk.END)
        self.perro_edad_entry.delete(0, tk.END)
        self.foto_label.config(image='', text="No hay foto")

        self.sesion_duracion_entry.delete(0, tk.END)
        self.sesion_descripcion_text.delete("1.0", tk.END)

        self.seminario_descripcion_text.delete("1.0", tk.END)

        self.pago_fecha_entry.delete(0, tk.END)
        self.pago_monto_entry.delete(0, tk.END)
        self.pago_metodo_entry.delete(0, tk.END)
