import customtkinter as ctk
from ..utilitis import grid_widget
class SelectTask(ctk.CTkFrame):
    def __init__(self,parent,width,height,**kwargs):
        super().__init__(parent,width=width,height=height,**kwargs)

        self.pack_propagate(False)
        
        self.grid_columnconfigure((0,1,2),weight=1)
        self.grid_rowconfigure((0,1,2),weight=1)
        
        self.label=ctk.CTkLabel(
            self,
            text="Please Select An Option",
            font=("Arial",20),
            pady=10
        )

        grid_widget(entry=self.label,r=0,c=0,py=10,px=10,colspan=3)
        


        self.radio_var=ctk.StringVar(value="teachers")
        self.selected="teachers"
        
        def radio_command():
            self.selected=self.radio_var.get()
  
            
        self.teacher_radio_button=ctk.CTkRadioButton(
            self,
            text="Teachers",
            variable=self.radio_var,
            value="teachers",
            command=radio_command
            )   
        grid_widget(entry=self.teacher_radio_button,r=1,c=0,py=10,px=10)
        
        self.student_radio_button=ctk.CTkRadioButton(
            self,
            text="Students",
            variable=self.radio_var,
            value="students",
            command=radio_command
            )
        
        grid_widget(entry=self.student_radio_button,r=1,c=1,py=10,px=10)
        
        self.staff_radio_button=ctk.CTkRadioButton(
            self,
            text="Staffs",
            variable=self.radio_var,
            value="staffs",
            command=radio_command
            )          
        grid_widget(entry=self.staff_radio_button,r=1,c=2,py=10,px=10)
        
        
        self.proceed_button=ctk.CTkButton(
            self,
            text="Proceed"
        )
        
        grid_widget(entry=self.proceed_button,r=2,c=0,py=10,px=10,colspan=3)
        
        
    def set_controller(self,controller):
        self.controller=controller
        self.proceed_button.configure(command=controller.select)