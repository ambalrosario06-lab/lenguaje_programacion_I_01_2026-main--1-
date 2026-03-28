# type:ignore
import tkinter as tk
from dotenv import load_dotenv
import os

load_dotenv()
user_password = os.getenv("USER_PASSWORD")

def capturar_valor():
    valor_usuario = campo_entrada_usuario.get()
    valor_password = campo_entrada_password.get()
    print(valor_usuario, valor_password)


ventana = tk.Tk()  # Instanciando la clase Tk de Tkinter
ventana.title("Mi primera app en tkinter")
ventana.geometry("500x500")

# Label o texto que se muestra
label_usuario = tk.Label(ventana, text="Usuario", foreground="#FF0000")
label_usuario.pack()

# Campo de entrada -> input
campo_entrada_usuario = tk.Entry(ventana)
campo_entrada_usuario.pack()

label_password = tk.Label(ventana, text="Password")
label_password.pack()

campo_entrada_password = tk.Entry(ventana, show="*")
campo_entrada_password.pack()

# Botón
boton = tk.Button(ventana, text="Capturar", command=capturar_valor)
boton.pack()

# Bucle principal que está en escucha de eventos
ventana.mainloop()
