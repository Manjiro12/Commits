import tkinter as tk

# Lista de actividades
actividades = []

def agregar():
    actividades.append("Nueva actividad")
    lbl_info.config(text=f"Actividad agregada.\nTotal: {len(actividades)}")

def eliminar():
    if actividades:
        actividades.pop()
        lbl_info.config(text=f"Actividad eliminada.\nTotal: {len(actividades)}")
    else:
        lbl_info.config(text="No hay actividades para eliminar")

def mostrar():
    if actividades:
        lbl_info.config(text="Actividades:\n" + "\n".join(actividades))
    else:
        lbl_info.config(text="No hay actividades registradas")

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Actividades")

btn_agregar = tk.Button(ventana, text="Agregar Actividad", command=agregar)
btn_agregar.pack(pady=10)

btn_eliminar = tk.Button(ventana, text="Eliminar Actividad", command=eliminar)
btn_eliminar.pack(pady=10)

btn_mostrar = tk.Button(ventana, text="Mostrar Actividades", command=mostrar)
btn_mostrar.pack(pady=10)

# Etiqueta para mostrar información
lbl_info = tk.Label(ventana, text="Aquí aparecerá la información")
lbl_info.pack(pady=20)

ventana.mainloop()
