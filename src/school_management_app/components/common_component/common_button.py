import customtkinter as ctk

class CommonButton(ctk.CTkButton):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, text=text, **kwargs)
        pass