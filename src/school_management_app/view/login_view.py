import customtkinter as ctk 

from ..utilitis import grid_widget


    
    

class Login (ctk.CTkFrame):
    def __init__(self,parent,width,height,**kwargs):
        super().__init__(parent,width=width,height=height,**kwargs)
        
        self._border_width=2
        self._corner_radius=5
        self.controller=None
        
        self.pack_propagate(False)
        
        for i in range(5):
            self.grid_rowconfigure(i,weight=1)
        self.grid_columnconfigure(0,weight=1)
        
        self.label=ctk.CTkLabel(
            self,
            text="Welcome Back",
            font=("Arial",20),
            )
        grid_widget(self.label,0,0,10,10)
        
        self.username_entry=ctk.CTkEntry(
            self,
            placeholder_text="Enter User Name"
            )
        self.password_entry=ctk.CTkEntry(
            self,
            placeholder_text="Password",
            show="*"
            )
        
        self.login_btn=ctk.CTkButton(
            self,
            text="Login",
            cursor="hand2",
            )
         
        grid_widget(self.username_entry,1,0,10,10)
        grid_widget(self.password_entry,2,0,10,10)
        grid_widget(self.login_btn,3,0,10,10)
    
    def set_controller(self,controller):
        self.controller=controller
        self.login_btn.configure(command=controller.login)