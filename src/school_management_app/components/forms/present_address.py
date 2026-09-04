import customtkinter as ctk 
from ...utilitis import grid_widget

class PresentAddress(ctk.CTkFrame):
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
         
                
        self.present_address_section_label= ctk.CTkLabel(self,text="Present Address",anchor="w",font=("Arial",20))
        grid_widget(entry=self.present_address_section_label,c=0,r=0,colspan=11,rowspan=1,direction="we",px=40,py=10)  
         
        self.student_present_division_label= ctk.CTkLabel(self,text="Division:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_present_division_label,c=0,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_present_division_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_present_division_option,c=1,r=1,colspan=2,rowspan=1,direction="we",px=5,py=10)
        
        self.student_present_district_label= ctk.CTkLabel(self,text="District:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_present_district_label,c=3,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_present_district_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_present_district_option,c=4,r=1,colspan=2,rowspan=1,direction="we",px=0,py=10)
                
        self.student_present_upazila_label= ctk.CTkLabel(self,text="Upazila:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_present_upazila_label,c=6,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_present_upazila_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_present_upazila_option,c=7,r=1,colspan=2,rowspan=1,direction="we",px=0,py=10)
        
        
        self.student_present_address_label= ctk.CTkLabel(self,text="Address:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_present_address_label,c=0,r=2,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_present_address_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_present_address_entry,c=1,r=2,colspan=8,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)
        