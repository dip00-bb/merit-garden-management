import customtkinter as ctk
from ...utilitis import grid_widget,load_image_and_resize
class StudentList(ctk.CTkFrame):
    def __init__(self, parent, student_id,student_name,student_class,student_roll,r,**kwargs):
        super().__init__(parent, **kwargs)

        self.pack_propagate(False)
        self.row=r
        self.student_id=student_id
        
        for i in range(6):
            self.grid_columnconfigure(i,weight=1,uniform="find_param")
        for i in range(1):
            self.grid_rowconfigure(i,weight=1)  
        
        self.icon=load_image_and_resize(20,20,f"fees_management/tickets.png")
            
        self.task_icon=ctk.CTkImage(
                light_image=self.icon,
                size=(25,25),)
        
        self.student_name_label=ctk.CTkLabel(self,text="Name:",font=("Arial", 15),anchor="e")
        grid_widget(entry=self.student_name_label,c=0,r=self.row,py=0,px=10,colspan=1)
        
        self.student_name=ctk.CTkLabel(self,text=student_name,font=("Arial", 15),anchor="w")
        grid_widget(entry=self.student_name,c=1,r=self.row,py=10,px=0,colspan=1)
        
        self.student_class_label=ctk.CTkLabel(self,text="Class:",font=("Arial", 15),anchor="e")
        grid_widget(entry=self.student_class_label,c=2,r=self.row,py=10,px=10,colspan=1)
        
        self.student_class=ctk.CTkLabel(self,text=student_class,font=("Arial", 15),anchor="w")
        grid_widget(entry=self.student_class,c=3,r=self.row,py=10,px=0,colspan=1)
        
        self.student_roll_label=ctk.CTkLabel(self,text="Roll:",font=("Arial", 15),anchor="e")
        grid_widget(entry=self.student_roll_label,c=4,r=self.row,py=10,px=10,colspan=1)
        
        self.student_roll=ctk.CTkLabel(self,text=student_roll,font=("Arial", 15), anchor="w")
        grid_widget(entry=self.student_roll,c=5,r=self.row,py=10,px=0,colspan=1)
        
        self.button=ctk.CTkButton(self,text="",image=self.task_icon,compound="left",width=20)
        grid_widget(entry=self.button,c=6,r=self.row,py=10,px=20,colspan=1)
    
    def set_controller(self,controller):
        self.controller=controller
        self.button.configure(command=lambda: self.controller.print_student_id(self.student_id))