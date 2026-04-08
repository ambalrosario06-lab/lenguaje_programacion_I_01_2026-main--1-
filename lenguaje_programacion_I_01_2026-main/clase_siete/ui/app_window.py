import tkinter as tk
from tkinter import messagebox

class AppWindow:
    def __init__(self, service):
        self.service = service

        
        self.root = tk.Tk()
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        
        self.label_title = tk.Label(self.root, text="Título:")
        self.label_title.pack()

        self.entry_title = tk.Entry(self.root, width=40)
        self.entry_title.pack()

        self.label_desc = tk.Label(self.root, text="Descripción:")
        self.label_desc.pack()

        self.entry_desc = tk.Entry(self.root, width=40)
        self.entry_desc.pack()

        self.btn_add = tk.Button(self.root, text="Agregar Tarea", command=self.add_task)
        self.btn_add.pack(pady=10)

       
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=10)

      
        self.load_tasks()

    def add_task(self):
        title = self.entry_title.get()
        description = self.entry_desc.get()

        if not title or not description:
            messagebox.showwarning("Error", "Debe completar todos los campos")
            return

        # Crear tarea
        self.service.create_task(title, description)

        # Limpiar inputs
        self.entry_title.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

        # Recargar lista
        self.load_tasks()

    def load_tasks(self):
        self.listbox.delete(0, tk.END)

        tasks = self.service.get_tasks()
        for task in tasks:
            text = f"{task['id']}: {task['title']} - {task['description']}"
            self.listbox.insert(tk.END, text)

    def run(self):
        self.root.mainloop()

