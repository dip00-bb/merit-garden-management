import customtkinter as ctk

# models 
from school_management_app.model import UserModel
from school_management_app.model import SelectTaskModel

# views (ui)
from school_management_app.components import TkCanvas
from school_management_app.view import Login
from school_management_app.view import SelectTask

# controllers
from school_management_app.controller import LoginController
from school_management_app.controller import SelectTaskController

# utilities functions
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
        
        #  login 
        
        user_model=UserModel()
    
        self.login_view=Login(
                parent=self,
                width=400,
                height=200,
                )     
        
        login_controller=LoginController(view=self.login_view,model=user_model,app=self)
        self.login_view.set_controller(login_controller)
        
        def show_login():
            canvas.destroy()
            self.login_view.pack(
                    anchor="center",
                    expand=True
                ) 
        canvas.after(2000,show_login)
        

        
        # select task
        
        select_task_model=SelectTaskModel()
        self.select_task_view=SelectTask(
                parent=self,
                width=500,
                height=500
            )

        select_task_controller=SelectTaskController(view=self.select_task_view,model=select_task_model,app=self)
        self.select_task_view.set_controller(select_task_controller)

    def on_login_success(self):
        self.login_view.destroy()
        self.select_task_view.pack(
            anchor="center",
            expand=True
            )


        

        
        
if __name__=="__main__":
    app=App()
    
    app.mainloop()