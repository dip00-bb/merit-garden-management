import sqlite3
import customtkinter as ctk
from PIL import ImageTk
# models 
from school_management_app.model import UserModel
from school_management_app.model import SelectTaskModel

# views (ui)
from school_management_app.components import TkCanvas
from school_management_app.view import Login
from school_management_app.view import SelectTask
from school_management_app.view import StudentDashboard

# controllers
from school_management_app.controller import LoginController
from school_management_app.controller import SelectTaskController

# utilities functions
from school_management_app.utilitis import load_image_and_resize


# database
from school_management_app.database import Database
# repository

from school_management_app.database import StudentRepository
from school_management_app.database import FeesRepository


# schema
from school_management_app.database import STUDENT_SCHEMA,STUDENT_FEE


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # database
        database=Database()
        connection=None
        
        
        try:
            connection=database.connect()
            cursor=connection.cursor()
            

            cursor.execute(STUDENT_SCHEMA)
            cursor.execute(STUDENT_FEE) 
            
            connection.commit()
        except sqlite3.Error as e:
            print("Error",e)
        
        
            
        # repository
        self.student_repo=StudentRepository(database)
        self.fee_repo=FeesRepository(database)
        
        
        # screen size
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()

        # self.geometry("200x200")
        self.geometry(f"{screen_width}x{screen_height}")
        self.resizable(True,True)

        # title
        self.title("Merit Garden Girls School And College Management")

        
    
        

        # dashboard
        self.student_dashboard=StudentDashboard(
            self,
            height=screen_height,
            weight=screen_width,
            student_repo=self.student_repo,
            fees_repo=self.fee_repo,
        )
        self.student_dashboard.pack(
            fill="both",expand=True
        )

    def on_login_success(self):
        self.login_view.destroy()
        self.select_task_view.pack(
            anchor="center",
            expand=True
            )


        

        
        
if __name__=="__main__":
    app=App()
    
    app.mainloop()