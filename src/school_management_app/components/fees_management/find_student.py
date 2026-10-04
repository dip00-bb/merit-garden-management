import customtkinter as ctk
from ...utilitis import grid_widget


class FindStudent(ctk.CTkFrame):
    def __init__(self,parent,**kwargs):
        super().__init__(parent, **kwargs)
        
        
        for i in range(6):
            self.grid_columnconfigure(i,weight=1,uniform="find_param")
        for i in range(3):
            self.grid_rowconfigure(i,weight=1)  
        
        # class 
        classes=["1", "2", "3","4","5 ","6","7","8","9","10"]
            
        self.roll_label=ctk.CTkLabel(self, text="Roll Number:",font=("Arial", 15))
        grid_widget(entry=self.roll_label,c=0,r=0,py=10,px=10,colspan=1)
        
        self.roll_entry=ctk.CTkEntry(self, placeholder_text="Enter Roll Number:")
        grid_widget(entry=self.roll_entry,c=1,r=0,py=10,px=10,colspan=1)
        
        self.class_label=ctk.CTkLabel(self, text="Class:",font=("Arial", 15))
        grid_widget(entry=self.class_label,c=2,r=0,py=10,px=10,colspan=1)
        
        self.class_option=ctk.CTkOptionMenu(self, values=classes)
        grid_widget(entry=self.class_option,c=3,r=0,py=10,px=10,colspan=1)
        
        self.year_label=ctk.CTkLabel(self, text="Year:",font=("Arial", 15))
        grid_widget(entry=self.year_label,c=4,r=0,py=10,px=10,colspan=1)
        
        self.year_entry=ctk.CTkEntry(self, placeholder_text="Enter Year:")
        grid_widget(entry=self.year_entry,c=5,r=0,py=10,px=10,colspan=1)
        
        self.search_button=ctk.CTkButton(self,text="Search")
        grid_widget(entry=self.search_button,c=6,r=0,py=10,px=10,colspan=1)
        
    def set_controller(self,controller):
        self.controller=controller
        
        self.search_button.configure(command=controller.search_for_student)
