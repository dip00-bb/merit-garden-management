import customtkinter as ctk 
from ...utilitis import grid_widget,show_grid
from ...utilitis import heading_text_color,heading_color,text_color
class PermanentAddress(ctk.CTkFrame):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        
        for i in range(12):
            self.grid_columnconfigure(i,weight=1)
        for i in range(3):
            self.grid_rowconfigure(i,weight=1)  
              
            
        self.divisions = [
            "Barishal",
            "Chattogram",
            "Dhaka",
            "Khulna",
            "Mymensingh",
            "Rajshahi",
            "Rangpur",
            "Sylhet"
            ]   
        
        
        self.permanent_address_section_label= ctk.CTkLabel(self,text="Permanent Address",anchor="center",font=("Arial",20),bg_color=heading_color,text_color=heading_text_color)
        grid_widget(entry=self.permanent_address_section_label,c=0,r=0,colspan=5,rowspan=1,direction="we",px=0,py=10)  
        
        self.permanent_present_same_check= ctk.CTkCheckBox(self,text="Same As Present",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.permanent_present_same_check,c=5,r=0,colspan=8,rowspan=1,direction="e",px=320,py=10)   
         
        self.student_permanent_division_label= ctk.CTkLabel(self,text="Division:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_division_label,c=0,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_permanent_division_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_permanent_division_option,c=1,r=1,colspan=2,rowspan=1,direction="we",px=5,py=10)
        
        self.student_permanent_district_label= ctk.CTkLabel(self,text="District:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_district_label,c=3,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_permanent_district_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_permanent_district_option,c=4,r=1,colspan=2,rowspan=1,direction="we",px=0,py=10)
                
        self.student_permanent_upazila_label= ctk.CTkLabel(self,text="Upazila:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_upazila_label,c=6,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_permanent_upazila_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_permanent_upazila_option,c=7,r=1,colspan=2,rowspan=1,direction="we",px=0,py=10)
        
        
        self.student_permanent_address_label= ctk.CTkLabel(self,text="Address:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_address_label,c=0,r=2,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_permanent_address_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_permanent_address_entry,c=1,r=2,colspan=8,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)