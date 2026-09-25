import customtkinter as ctk
from ....components import ManageFee
class FeesManagement(ctk.CTkFrame):
    def __init__ (self,parent,**kwargs):
        super().__init__(parent,fg_color="green",**kwargs) 
        
        
        self.pack_propagate(False)
        
        # self.label=ctk.CTkLabel(
        #     self,
        #     text="Fees Management",
        #     font=("Arial",50)
        # )
        
        # self.label.pack(
        #     fill="both",
        #     expand=True
        # )
        
        self.fees_view=ManageFee(self)
        self.fees_view.pack(padx=10)