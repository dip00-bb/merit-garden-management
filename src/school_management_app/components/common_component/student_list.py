import customtkinter as ctk
from ...utilitis import grid_widget
class StudentList(ctk.CTkFrame):
    def __init__(self, parent, student_name,student_class,student_roll,r,**kwargs):
        super().__init__(parent, **kwargs)

        
        self.row=r
        
        
        for i in range(6):
            self.grid_columnconfigure(i,weight=1,uniform="find_param")
        for i in range(1):
            self.grid_rowconfigure(i,weight=1)  
        
        
        self.student_name_label=ctk.CTkLabel(self,text="Name:",font=("Arial", 15))
        grid_widget(entry=self.student_name_label,c=0,r=self.row,py=0,px=10,colspan=1)
        
        self.student_name=ctk.CTkLabel(self,text=student_name,font=("Arial", 15),anchor="w")
        grid_widget(entry=self.student_name,c=1,r=self.row,py=10,px=0,colspan=1)
        
        self.student_class_label=ctk.CTkLabel(self,text="Class:",font=("Arial", 15))
        grid_widget(entry=self.student_class_label,c=2,r=self.row,py=10,px=0,colspan=1)
        
        self.student_class=ctk.CTkLabel(self,text=student_class,font=("Arial", 15),anchor="w")
        grid_widget(entry=self.student_class,c=3,r=self.row,py=10,px=0,colspan=1)
        
        self.student_roll_label=ctk.CTkLabel(self,text="Roll:",font=("Arial", 15))
        grid_widget(entry=self.student_roll_label,c=4,r=self.row,py=10,px=0,colspan=1)
        
        self.student_roll=ctk.CTkLabel(self,text=student_roll,font=("Arial", 15), anchor="w")
        grid_widget(entry=self.student_roll,c=5,r=self.row,py=10,px=0,colspan=1)