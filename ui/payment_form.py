import tkinter as tk
from tkinter import messagebox
from ui.style import style_button, style_label
from models import Pago

class PaymentForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("SGE(Sistema de Gestión de Empatican)")
        self.geometry("400x400")
        self.configure(bg="#f0f0f0")
        self.iconbitmap("empatican/logemp.ico")  # Ruta a tu archivo .ico

        # Etiquetas y campos de entrada
        tk.Label(self, text="Client ID:").grid(row=0, column=0, padx=10, pady=10)
        self.client_id_entry = tk.Entry(self)
        self.client_id_entry.grid(row=0, column=1)

        tk.Label(self, text="Date:").grid(row=1, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=1, column=1)

        tk.Label(self, text="Amount:").grid(row=2, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=2, column=1)

        tk.Label(self, text="Payment Method:").grid(row=3, column=0, padx=10, pady=10)
        self.payment_method_entry = tk.Entry(self)
        self.payment_method_entry.grid(row=3, column=1)

        tk.Label(self, text="Concept:").grid(row=4, column=0, padx=10, pady=10)
        self.concept_entry = tk.Entry(self)
        self.concept_entry.grid(row=4, column=1)

          # Etiqueta y campo para notas
        tk.Label(self, text="Notas:").grid(row=5, column=0, padx=10, pady=10)

        # Cambiar Entry a Text para notas
        self.notes_text = tk.Text(self, height=5, width=30)  # Aquí definimos el tamaño
        self.notes_text.grid(row=5, column=1, padx=10, pady=10)
        # Al guardar
        notas = self.notes_text.get("1.0", tk.END)  # Obtener texto desde la primera línea hasta el final


        # Botón para guardar
        save_button = tk.Button(self, text="Save Payment", command=self.save_payment)
        style_button(save_button)
        save_button.grid(row=7, column=0, columnspan=2, pady=20)

    def save_payment(self):
        client_id = self.client_id_entry.get()
        date = self.date_entry.get()
        amount = self.amount_entry.get()
        payment_method = self.payment_method_entry.get()
        concept = self.concept_entry.get()
        notes = self.notes_text.get("1.0", tk.END).strip()  # Obtener texto desde la primera línea hasta el final


        if client_id and date and amount:
            # Crear una instancia de Pago y guardar en la base de datos
            pago = Pago(cliente_id=client_id, fecha=date, monto=amount, metodo_pago=payment_method, concepto=concept, nota=notes)
            pago.save()

            messagebox.showinfo("Success", "Payment saved successfully!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Client ID, Date, and Amount are required.")
