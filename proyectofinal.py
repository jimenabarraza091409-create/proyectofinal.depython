import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():

    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("500x550")
    reg.configure(bg="#f4f4f4")
    reg.resizable(False, False)

    # -------------------------
    # TITULO
    # -------------------------
    titulo = tk.Label(
        reg,
        text="Registro de Productos",
        font=("Arial", 20, "bold"),
        bg="#f4f4f4",
        fg="#111827"
    )
    titulo.pack(pady=15)

    # -------------------------
    # FRAME PRINCIPAL
    # -------------------------
    frame = tk.Frame(
        reg,
        bg="white",
        bd=2,
        relief="groove"
    )
    frame.pack(padx=20, pady=10, fill="both", expand=True)

    fuente_label = ("Arial", 12, "bold")
    fuente_entry = ("Arial", 12)

    # -------------------------
    # ID PRODUCTO
    # -------------------------
    lbl_id = tk.Label(
        frame,
        text="ID del Producto",
        font=fuente_label,
        bg="white"
    )
    lbl_id.pack(pady=(20, 5))

    txt_id = tk.Entry(
        frame,
        font=fuente_entry,
        width=30,
        bd=2
    )
    txt_id.pack(ipady=5)

    # -------------------------
    # DESCRIPCION
    # -------------------------
    lbl_desc = tk.Label(
        frame,
        text="Descripción",
        font=fuente_label,
        bg="white"
    )
    lbl_desc.pack(pady=(15, 5))

    txt_desc = tk.Entry(
        frame,
        font=fuente_entry,
        width=30,
        bd=2
    )
    txt_desc.pack(ipady=5)

    # -------------------------
    # PRECIO
    # -------------------------
    lbl_precio = tk.Label(
        frame,
        text="Precio",
        font=fuente_label,
        bg="white"
    )
    lbl_precio.pack(pady=(15, 5))

    txt_precio = tk.Entry(
        frame,
        font=fuente_entry,
        width=30,
        bd=2
    )
    txt_precio.pack(ipady=5)

    # -------------------------
    # CATEGORIA
    # -------------------------
    lbl_categoria = tk.Label(
        frame,
        text="Categoría",
        font=fuente_label,
        bg="white"
    )
    lbl_categoria.pack(pady=(15, 5))

    txt_categoria = tk.Entry(
        frame,
        font=fuente_entry,
        width=30,
        bd=2
    )
    txt_categoria.pack(ipady=5)

    # -------------------------
    # FUNCION GUARDAR
    # -------------------------
    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        # Validaciones
        if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
            messagebox.showwarning(
                "Campos Vacíos",
                "Por favor complete todos los campos."
            )
            return

        # Validar precio
        try:
            float(precio)
        except:
            messagebox.showerror(
                "Error",
                "El precio debe ser un número."
            )
            return

        # Guardar archivo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(archivo, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{id_prod}|{descripcion}|{precio}|{categoria}\n"
            )

        messagebox.showinfo(
            "Guardado",
            "Producto registrado correctamente."
        )

        # Limpiar campos
        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

    # -------------------------
    # BOTON GUARDAR
    # -------------------------
    btn_guardar = tk.Button(
        reg,
        text="Guardar Producto",
        command=guardar_producto,
        font=("Arial", 12, "bold"),
        bg="#111827",
        fg="white",
        activebackground="#374151",
        activeforeground="white",
        padx=20,
        pady=10,
        cursor="hand2",
        bd=0
    )

    btn_guardar.pack(pady=20)


def abrir_registro_ventas():
    messagebox.showinfo(
        "Registro de Ventas",
        "Aquí irá el módulo de registro de ventas."
    )


def abrir_reportes():
    messagebox.showinfo(
        "Reportes",
        "Aquí irá el módulo de reportes."
    )


def abrir_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0"
    )


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - softwarepuntodeventajimenanahomi")
ventana.geometry("500x600")
ventana.configure(bg="#f4f4f4")
ventana.resizable(False, False)

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    imagen = Image.open(
        os.path.join(BASE_DIR, "logo.png")
    )

    imagen = imagen.resize((250, 250))

    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg="#f4f4f4"
    )

    lbl_logo.pack(pady=20)

except:
    lbl_sin_logo = tk.Label(
        ventana,
        text="(Aquí va el logo del sistema)",
        font=("Arial", 14),
        bg="#f4f4f4"
    )

    lbl_sin_logo.pack(pady=40)

# -------------------------
# BOTONES PRINCIPALES
# -------------------------
FUENTE_BOTON = ("Arial", 12, "bold")

btn_reg_prod = tk.Button(
    ventana,
    text="Registro de Productos",
    command=abrir_registro_productos,
    bg="#111827",
    fg="white",
    font=FUENTE_BOTON,
    padx=10,
    pady=10,
    width=25,
    cursor="hand2",
    bd=0
)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = tk.Button(
    ventana,
    text="Registro de Ventas",
    command=abrir_registro_ventas,
    bg="#111827",
    fg="white",
    font=FUENTE_BOTON,
    padx=10,
    pady=10,
    width=25,
    cursor="hand2",
    bd=0
)
btn_reg_ventas.pack(pady=10)

btn_reportes = tk.Button(
    ventana,
    text="Reportes",
    command=abrir_reportes,
    bg="#111827",
    fg="white",
    font=FUENTE_BOTON,
    padx=10,
    pady=10,
    width=25,
    cursor="hand2",
    bd=0
)
btn_reportes.pack(pady=10)

btn_acerca = tk.Button(
    ventana,
    text="Acerca de",
    command=abrir_acerca_de,
    bg="#111827",
    fg="white",
    font=FUENTE_BOTON,
    padx=10,
    pady=10,
    width=25,
    cursor="hand2",
    bd=0
)
btn_acerca.pack(pady=10)

# -------------------------
# INICIO DE LA APP
# -------------------------
ventana.mainloop()