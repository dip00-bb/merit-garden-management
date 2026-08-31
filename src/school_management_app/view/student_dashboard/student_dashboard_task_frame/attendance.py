import customtkinter as ctk

class Attendance(ctk.CTkFrame):
    def __init__ (self,parent,**kwargs):
        super().__init__(parent,fg_color="green",**kwargs) 
        
        self.label=ctk.CTkLabel(
            self,
            text="This is attendance",
            font=("Arial",50)
        )
        
        self.label.pack(
            fill="both",
            expand=True
        )