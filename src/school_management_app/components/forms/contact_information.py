import customtkinter as ctk 
from ...utilitis import grid_widget,show_grid
from ...utilitis import text_color,heading_text_color,heading_color

class ContactInformation(ctk.CTkFrame):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        self.blood_groups=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        self.religions=["Islam", "Hinduism", "Buddhism", "Christianity", "Other"]
        
       
        
        for i in range(12):
            self.grid_columnconfigure(i,weight=1)
        for i in range (4):
            self.grid_rowconfigure(i,weight=1)
            
        self.contact_and_other_information_section_label= ctk.CTkLabel(self,text="Student Contact And Other Information",anchor="center",font=("Arial",20),bg_color=heading_color,text_color=heading_text_color)
        grid_widget(entry=self.contact_and_other_information_section_label,c=0,r=0,colspan=8,rowspan=1,direction="we",px=0,py=10)  

        self.student_phone_number_label=ctk.CTkLabel(self,text="Phone Number:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_phone_number_label,c=0,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_phone_number_entry=ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_phone_number_entry,c=1,r=1,colspan=4,rowspan=1,direction="we",px=5,py=10)
        
        self.student_whatsapp_number_label=ctk.CTkLabel(self,text="Whatsapp Number:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_whatsapp_number_label,c=5,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_whatsapp_number_entry=ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_whatsapp_number_entry,c=6,r=1,colspan=3,rowspan=1,direction="we",px=5,py=10,ipadx=0,ipady=5)
        
        self.student_email_label=ctk.CTkLabel(self,text="Email:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_email_label,c=0,r=2,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_email_entry=ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_email_entry,c=1,r=2,colspan=4,rowspan=1,direction="we",px=5,py=10,ipadx=0,ipady=5)
        
        self.student_blood_group_label=ctk.CTkLabel(self,text="Blood Group:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_blood_group_label,c=5,r=2,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_blood_group_option=ctk.CTkOptionMenu(self,values= self.blood_groups,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_blood_group_option,c=6,r=2,colspan=3,rowspan=1,direction="we",px=5,py=10)

        self.student_religion_label=ctk.CTkLabel(self,text="Religion:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_religion_label,c=0,r=3,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_religion_option=ctk.CTkOptionMenu(self,values= self.religions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_religion_option,c=1,r=3,colspan=4,rowspan=1,direction="we",px=5,py=10)
        
        