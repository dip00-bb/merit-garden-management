import customtkinter as ctk
from ....utilitis import grid_widget,show_grid
from ....utilitis import text_color,heading_text_color,heading_color

class AdmissionInformation(ctk.CTkFrame):
    def __init__(self,parent,**kwarg):
        super().__init__(parent,**kwarg)

        for i in range(12):
            self.grid_columnconfigure(i,weight=1)
        for i in range(3):
            self.grid_rowconfigure(i,weight=1) 
                   
        
        self.classes=["1","2","3","4","5","6","7","8","9","10"]
        self.groups=["Science","Arts","Commerce"]
        self.optional_subject=["Higher Math","Agriculture","Biology"] 
     
     
        self.student_admission_form_label= ctk.CTkLabel(self,text="Student Admission Information",anchor="center",font=("Arial",20),bg_color=heading_color,text_color=heading_text_color)
        grid_widget(entry=self.student_admission_form_label,c=1,r=0,colspan=8,rowspan=1,direction="we",px=0,py=10)  
        
        self.student_admitted_class_label=ctk.CTkLabel(self,text="Which Class Wanted To Be Admitted:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_admitted_class_label,c=0,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_religion_option=ctk.CTkOptionMenu(self,values= self.classes,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_religion_option,c=1,r=1,colspan=4,rowspan=1,direction="we",px=5,py=10)        
        
        self.student_admitted_group_label=ctk.CTkLabel(self,text="Group:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_admitted_group_label,c=5,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_group_option=ctk.CTkOptionMenu(self,values= self.groups,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_group_option,c=6,r=1,colspan=3,rowspan=1,direction="we",px=5,py=10)  
        
        self.student_optional_subject_label=ctk.CTkLabel(self,text="Optional Subject:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_optional_subject_label,c=0,r=2,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_optional_subject_option=ctk.CTkOptionMenu(self,values= self.optional_subject,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_optional_subject_option,c=1,r=2,colspan=4,rowspan=1,direction="we",px=5,py=10)  
        
        self.student_previous_school_name_label=ctk.CTkLabel(self,text="Previous School Name:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_previous_school_name_label,c=5,r=2,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_previous_school_name_entry=ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_previous_school_name_entry,c=6,r=2,colspan=3,rowspan=1,direction="we",px=5,py=10,ipadx=0,ipady=5)      