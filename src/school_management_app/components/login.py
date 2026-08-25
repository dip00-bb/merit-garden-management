import customtkinter as ctk 

def grid_widget(entry,r,c,py,px,direction="ew"):
    entry.grid(
        row=r, 
        column=c,
        pady=py,
        padx=px,
        sticky=direction
    )
    

def match_password(
    self,
    entry1:ctk.CTkEntry,
    entry2:ctk.CTkEntry,
    u_username,
    u_password,

    ):
    
    username=entry1.get()
    password=entry2.get()
    
    if( username!=u_username or password!= u_password ):
        self.warning_label=ctk.CTkLabel(
            self,
            text="Incorrect username or password",
            font=("Arial",15),
            text_color="red"
        )
        grid_widget(self.warning_label,4,0,10,10)
    else:
        self.warning_label.destroy()
        pass
    
    

class Login (ctk.CTkFrame):
    def __init__(self,parent,width,height,**kwargs):
        super().__init__(parent,width=width,height=height,**kwargs)
        
        username="dipchondo"
        password="123456"
        
        self._border_width=2
        self._corner_radius=5
    
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
        
        username_entry=ctk.CTkEntry(
            self,
            placeholder_text="Enter User Name"
            )
        user_password_entry=ctk.CTkEntry(
            self,
            placeholder_text="Password",
            show="*"
            )
        login_btn=ctk.CTkButton(
            self,
            text="Login",
            cursor="hand2",
            command=lambda:match_password(self,username_entry,user_password_entry,username,password)
            )
         
        grid_widget(username_entry,1,0,10,10)
        grid_widget(user_password_entry,2,0,10,10)
        grid_widget(login_btn,3,0,10,10)
    
    