import tkinter as tk

ventana = tk.Tk()
ventana.title("Programa para subir a Repositorio")
ventana.geometry("420x260")
ventana.configure(bg="#0f172a")  # Fondo moderno oscuro

# Marco para centrar mejor el contenido
frame = tk.Frame(ventana, bg="#0f172a")
frame.pack(expand=True)

# Texto estilizado
etiqueta = tk.Label(
    frame,
    text="Este programa es de\nJimena y Nahomi",
    font=("Arial", 18, "bold"),
    fg="#22c55e",   # Verde brillante
    bg="#0f172a",
    justify="center"
)

etiqueta.pack(pady=20)

# Línea decorativa
linea = tk.Frame(frame, bg="#38bdf8", height=3, width=200)
linea.pack(pady=10)

ventana.mainloop()