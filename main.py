import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Tareas")
ventana.geometry("500x400")

# Funciones de los botones
def agregar_tarea():
    print("Agregar tarea")

def eliminar_tarea():
    print("Eliminar tarea")

def completar_tarea():
    print("Tarea completada")

# Título
titulo = tk.Label(
    ventana,
    text="Sistema de Gestión de Tareas",
    font=("Arial", 16)
)
titulo.pack(pady=20)

# Botón agregar
btn_agregar = tk.Button(
    ventana,
    text="Agregar Tarea",
    command=agregar_tarea
)
btn_agregar.pack(pady=10)

# Botón eliminar
btn_eliminar = tk.Button(
    ventana,
    text="Eliminar Tarea",
    command=eliminar_tarea
)
btn_eliminar.pack(pady=10)

# Botón completar
btn_completar = tk.Button(
    ventana,
    text="Completar Tarea",
    command=completar_tarea
)
btn_completar.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()