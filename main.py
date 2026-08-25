import customtkinter as ctk

from school_management_app.components import TkCanvas
from school_management_app.components import Login
from school_management_app.utilitis import load_image_and_resize
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # screen size
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()

        self.geometry(f"{screen_width}x{screen_height}")
        self.resizable(False,False)

        # title
        self.title("Merit Garden Girls School And College Management")

        # welcome canvas
        canvas_image=load_image_and_resize(
            screen_width,
            screen_height,
            "merit_icon.png"
            )
        
        canvas=TkCanvas(
            self,
            screen_width,
            screen_height,
            background_image=canvas_image
            )
        canvas.pack(fill="both",expand=True)
        login=Login(
                parent=self,
                width=250,
                height=200
                )     
        def show_login():
            canvas.destroy()
            login.pack(
                    anchor="center",
                    expand=True
                )
            
        canvas.after(2000,show_login)
        
 
        
        
        
if __name__=="__main__":
    app=App()
    
    app.mainloop()