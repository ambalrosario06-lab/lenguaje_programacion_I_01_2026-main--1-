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
