import customtkinter as ctk 
from ...utilitis import grid_widget,show_grid
from ...utilitis import heading_text_color,heading_color,text_color
from ...utilitis import bangladesh

class PermanentAddress(ctk.CTkFrame):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        
        for i in range(12):
            self.grid_columnconfigure(i,weight=1)
        for i in range(3):
            self.grid_rowconfigure(i,weight=1)  
              
        # controller
        
        self.controller=None 

        self.divisions=list(bangladesh.keys())
        self.selected_division=None
        
        # variable to hold division value
        self.value_of_permanent_division=ctk.StringVar(value="sylhet")
        
        # variable to hold the value of district
        self.value_of_permanent_district=ctk.StringVar(value=None)
        
        # variable to hold the value of upazila 
        self.value_of_permanent_upazila=ctk.StringVar(value=None)        
        
        # variable to hold the value of address
        self.value_of_permanent_address=ctk.StringVar(value="")  
        
        
        # check box (same as present)
        self.check_var=ctk.StringVar(value="off")
    
        
        self.permanent_address_section_label= ctk.CTkLabel(self,text="Permanent Address",anchor="center",font=("Arial",20),bg_color=heading_color,text_color=heading_text_color)
        grid_widget(entry=self.permanent_address_section_label,c=1,r=0,colspan=8,rowspan=1,direction="we",px=0,py=10)  
        
        # self.permanent_permanent_same_check= ctk.CTkCheckBox(self,text="Same As permanent",font=("Arial",20),text_color=text_color)
        # grid_widget(entry=self.permanent_permanent_same_check,c=5,r=0,colspan=8,rowspan=1,direction="e",px=320,py=10)   
         
        self.student_permanent_division_label= ctk.CTkLabel(self,text="Division:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_division_label,c=0,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_permanent_division_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),variable=self.value_of_permanent_division,font=("Arial", 18))
        grid_widget(entry=self.student_permanent_division_option,c=1,r=1,colspan=2,rowspan=1,direction="we",px=5,py=10)
        self.student_permanent_division_option.set("Division")
        
        self.student_permanent_district_label= ctk.CTkLabel(self,text="District:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_district_label,c=3,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_permanent_district_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),variable=self.value_of_permanent_district,font=("Arial", 18),state="disabled")
        grid_widget(entry=self.student_permanent_district_option,c=4,r=1,colspan=2,rowspan=1,direction="we",px=0,py=10)
        self.student_permanent_district_option.set("District")        
        self.student_permanent_upazila_label= ctk.CTkLabel(self,text="Upazila:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_upazila_label,c=6,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_permanent_upazila_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18), font=("Arial", 18),variable=self.value_of_permanent_upazila,state="disabled")
        grid_widget(entry=self.student_permanent_upazila_option,c=7,r=1,colspan=2,rowspan=1,direction="we",px=0,py=10)
        self.student_permanent_upazila_option.set("Upazila")
        
        self.student_permanent_address_label= ctk.CTkLabel(self,text="Address:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_address_label,c=0,r=2,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_permanent_address_entry= ctk.CTkEntry(self,font=("Arial",20),textvariable=self.value_of_permanent_address)
        grid_widget(entry=self.student_permanent_address_entry,c=1,r=2,colspan=8,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)
        
        self.mark_same_as_present=ctk.CTkCheckBox(self,text="Same As Present",variable=self.check_var,offvalue="off",onvalue="on")
        grid_widget(entry=self.mark_same_as_present,c=1,r=3,colspan=1,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)
        

        

    def set_controller(self,controller):
        self.controller=controller
        self.student_permanent_division_option.configure(command=controller.on_permanent_division_change)
        self.student_permanent_district_option.configure(command=controller.on_permanent_district_change)
        self.mark_same_as_present.configure(command=controller.mark_same_as_present)