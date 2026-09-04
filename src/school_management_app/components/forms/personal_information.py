import customtkinter as ctk
from ...utilitis.place_grid import grid_widget  

class PersonalInformation(ctk.CTkFrame):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        
        for i in range(12):
            self.grid_columnconfigure(i,weight=1)
        for i in range (4):
            self.grid_rowconfigure(i,weight=1)
            
        self.selected_gender=ctk.StringVar(value="male")
        
        self.personal_information_label= ctk.CTkLabel(self,text="Personal Information",anchor="center",font=("Arial",20))
        grid_widget(entry=self.personal_information_label,c=0,r=0,colspan=11,rowspan=1,direction="we",px=5,py=10)  
                    
        self.student_name_label= ctk.CTkLabel(self,text="Student Name:",anchor="e",font=("Arial",20),)
        grid_widget(entry=self.student_name_label,c=0,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_name_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_name_entry,c=1,r=1,colspan=8,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)
        
        self.student_mother_name_label= ctk.CTkLabel(self,text="Mother Name:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_mother_name_label,c=0,r=2,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_mother_name_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_mother_name_entry,c=1,r=2,colspan=8,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)

        self.student_father_name_label= ctk.CTkLabel(self,text="Father Name:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_father_name_label,c=0,r=3,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_father_name_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_father_name_entry,c=1,r=3,colspan=8,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)
        
        self.date_of_birth_label= ctk.CTkLabel(self,text="Date Of Birth:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.date_of_birth_label,c=0,r=4,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.date_of_birth_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.date_of_birth_entry,c=1,r=4,colspan=3,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)
        
        self.student_gender_label= ctk.CTkLabel(self,text="Gender:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_gender_label,c=4,r=4,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_gender_male_radio_button= ctk.CTkRadioButton(self,text="Male",value="male",variable=self.selected_gender)
        grid_widget(entry=self.student_gender_male_radio_button,c=5,r=4,colspan=1,rowspan=1,direction="we",px=0,py=10)
        
        self.student_gender_female_radio_button= ctk.CTkRadioButton(self,text="Female",value="female",variable=self.selected_gender)
        grid_widget(entry=self.student_gender_female_radio_button,c=7,r=4,colspan=1,rowspan=1,direction="we",px=0,py=10) 