import customtkinter as ctk 
class Login (ctk.CTkFrame):
    def __init__(self,parent,width,height,**kwargs):
        super().__init__(parent,width,height,**kwargs)
        
        self._border_width=2
        self._corner_radius=5
        self.pack_propagate(False)
        
        self.label=ctk.CTkLabel(
            self,
            text="Welcome Back",
            font=("Arial",20)
            ).pack(
                pady=10,
                padx=10
            )
        
        user_entry=ctk.CTkEntry(
            self,
            placeholder_text="Enter User Name"
            ).pack(
                pady=10,
                padx=10,
                fill='both',
                expand=True
            )
        
        user_password=ctk.CTkEntry(
            self,
            placeholder_text="Password",
            show="*"
            ).pack(
                pady=10,
                padx=10,
                fill='both',
                expand=True
            )
        
        login_btn=ctk.CTkButton(
            self,
            text="Login",
            cursor="hand2"
        ).pack(
                pady=10,
                padx=10,
                fill='both',
                expand=True
        )        
