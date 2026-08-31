import customtkinter as ctk

class ShowResult(ctk.CTkFrame):
    def __init__ (self,parent,**kwargs):
        super().__init__(parent,fg_color="green",**kwargs) 
        
        self.label=ctk.CTkLabel(
            self,
            text="Show Result",
            font=("Arial",50)
        )
        
        self.label.pack(
            fill="both",
            expand=True
        )