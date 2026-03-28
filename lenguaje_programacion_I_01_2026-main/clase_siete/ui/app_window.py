import tkinter as tk
# from tkinter import ttk
from service.task_service import TaskService

class AppWindow(tk.Tk):

    def __init__(self, task_service: TaskService) -> None:
        super().__init__()
        self._task_service = task_service

        self.title("Tkinter desde POO")
        self.geometry("500x500")
        self.resizable(False, False)

        # Widgets
        self.create_widgets()

    def create_widgets(self) -> None:
        label = tk.Label(self, text="Bienvenido a mi App")
        label.pack()

        # Inputs
        label_title = tk.Label(self, text="Título:")
        label_title.pack()
        self.title_entry = tk.Entry(self)
        self.title_entry.pack()

        label_desc = tk.Label(self, text="Descripción:")
        label_desc.pack()
        self.description_entry = tk.Entry(self)
        self.description_entry.pack()

        # Botón
        button = tk.Button(self, text="Crear tarea", command=self.create_task)
        button.pack()

        # Tabla (Treeview)
        from tkinter import ttk
        self.tree = ttk.Treeview(self, columns=("title", "description"), show="headings")

        self.tree.heading("title", text="Título")
        self.tree.heading("description", text="Descripción")

        self.tree.pack()

        # Cargar datos
        self.load_tasks()

    def create_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()

        self._task_service.create_one_task(title, description)

        self.load_tasks()
        self.clear_inputs()


    def load_tasks(self):
        self.clear_table()
        tasks = self._task_service.get_all_task()

        for task in tasks:
            self.tree.insert("", "end", values=(task.title, task.description))


    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


    def clear_inputs(self):
        self.title_entry.delete(0, "end")
        self.description_entry.delete(0, "end")