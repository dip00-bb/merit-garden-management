import customtkinter as ctk 
from ...utilitis import grid_widget,show_grid
from ...utilitis import heading_text_color,heading_color,text_color

from ...utilitis import bangladesh

class PresentAddress(ctk.CTkFrame):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        
        for i in range(12):
            self.grid_columnconfigure(i,weight=1)
        for i in range(3):
            self.grid_rowconfigure(i,weight=1)  




        # controller
        self.controller=None


        self.divisions=list(bangladesh.keys())
        self.selected_division=""
        
        # variable to hold division value
        self.value_of_present_division=ctk.StringVar(value="")
        
        # variable to hold the value of district
        self.value_of_present_district=ctk.StringVar(value="")
        
        # variable to hold the value of upazila 
        self.value_of_present_upazila=ctk.StringVar(value="")
        
        # variable to hold the value of address
        self.value_of_present_address=ctk.StringVar(value="")
        
        
        # present address dictionary
        self.present_address_dictionary={}
                
        self.present_address_section_label= ctk.CTkLabel(self,text="Present Address",anchor="center",font=("Arial",20),bg_color=heading_color,text_color=heading_text_color)
        grid_widget(entry=self.present_address_section_label,c=1,r=0,colspan=8,rowspan=1,direction="we",px=0,py=10)  
         
        self.student_present_division_label= ctk.CTkLabel(self,text="Division:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_present_division_label,c=0,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_present_division_option= ctk.CTkOptionMenu(self,values=self.divisions,variable=self.value_of_present_division, dropdown_font=("Arial", 18),font=("Arial", 18))
        self.student_present_division_option.set("Division")
        grid_widget(entry=self.student_present_division_option,c=1,r=1,colspan=2,rowspan=1,direction="we",px=5,py=10)
        
        self.student_present_district_label= ctk.CTkLabel(self,text="District:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_present_district_label,c=3,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_present_district_option= ctk.CTkOptionMenu(self , variable=self.value_of_present_district, dropdown_font=("Arial", 18),font=("Arial", 18),state="disabled")
        self.student_present_district_option.set("District")
        grid_widget(entry=self.student_present_district_option,c=4,r=1,colspan=2,rowspan=1,direction="we",px=0,py=10)
                
        self.student_present_upazila_label= ctk.CTkLabel(self,text="Upazila:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_present_upazila_label,c=6,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_present_upazila_option= ctk.CTkOptionMenu(self, variable=self.value_of_present_upazila, dropdown_font=("Arial", 18), font=("Arial", 18),state="disabled")
        self.student_present_upazila_option.set("Upazila")
        grid_widget(entry=self.student_present_upazila_option,c=7,r=1,colspan=2,rowspan=1,direction="we",px=0,py=10)
        
        
        self.student_present_address_label= ctk.CTkLabel(self,text="Address:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_present_address_label,c=0,r=2,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_present_address_entry= ctk.CTkEntry(self,font=("Arial",20),textvariable=self.value_of_present_address)
        grid_widget(entry=self.student_present_address_entry,c=1,r=2,colspan=8,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)

        
        

        
    
    def set_controller(self,controller):
        self.controller=controller
        self.student_present_division_option.configure(command=controller.on_division_change)
        self.student_present_district_option.configure(command=controller.on_district_change)
        self.student_present_upazila_option.configure(command=controller.on_upazila_change)
        self.student_present_address_entry.bind(
            "<FocusOut>",
            controller.on_address_field_focus_out
        )