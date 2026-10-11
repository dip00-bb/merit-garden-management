import customtkinter as ctk

class ManageFee(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg_color="lightgray", **kwargs)
        self.pack_propagate(False)
        
        