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
        year=["2020", "2021", "2022", "2023", "2024","2025","2026","2027","2028","2029","2030"]
            
        roll_label=ctk.CTkLabel(self, text="Roll Number:",font=("Arial", 15))
        grid_widget(entry=roll_label,c=0,r=0,py=10,px=10)
        
        roll_entry=ctk.CTkEntry(self, placeholder_text="Enter Roll Number:")
        grid_widget(entry=roll_entry,c=1,r=0,py=10,px=10)
        
        class_label=ctk.CTkLabel(self, text="Class:",font=("Arial", 15))
        grid_widget(entry=class_label,c=2,r=0,py=10,px=10)
        
        class_option=ctk.CTkOptionMenu(self, values=classes)
        grid_widget(entry=class_option,c=3,r=0,py=10,px=10)
        
        year_label=ctk.CTkLabel(self, text="Year:",font=("Arial", 15))
        grid_widget(entry=year_label,c=4,r=0,py=10,px=10)
        
        year_option=ctk.CTkOptionMenu(self, values=year)
        grid_widget(entry=year_option,c=5,r=0,py=10,px=10)