import customtkinter as ctk

class SelectTask(ctk.CTkFrame):
    def __init__(self,parent,width,height,**kwargs):
        super().__init__(parent,width=width,height=height,**kwargs)

        self.pack_propagate(False)
        self.label=ctk.CTkLabel(
            self,
            text="Please Select An Option",
            font=("Arial",20),
            pady=10
        )
        self.label.pack()
        
        options=ctk.CTkOptionMenu(
            self,
            values=["Teacher","Student","Office Staff"],
            dropdown_font=("Arial",15),
            dropdown_hover_color="olive"
        )
        
        options.pack()
        