# -*- coding: utf-8 -*-
__autor__ = "Francesco"
__version__ = "0101 2022/06/05"
import tkinter
from customtkinter import *
from tkinter import messagebox, scrolledtext


from ....lib import project_lib
from ....gui import main_page_enum


CONFIG_FILE = "config.json"


class RecentProjectPage(CTkFrame):
    def __init__(self, master, app):
        self.app = app
        super().__init__(master)

        # configure grid layout (3x7)
        for i in range(5):
            self.rowconfigure(i, weight=1)
        self.rowconfigure(7, weight=10)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.title = CTkLabel(master=self,
                              text="Recenti",
                              text_font=("Roboto Medium", 20))  # font name and size in px
        self.title.grid(row=0, column=1, pady=20)

        back_button = CTkButton(
            master=self,
            text=f"Indietro",
            fg_color=("gray65", "gray25"),
            command=lambda: self.app.chose_frame(main_page_enum.MainPageEnum.NEW_PROJECT))

        back_button.grid(row=7, column=0, columnspan=3,
                         padx=20, pady=20, sticky="es")
