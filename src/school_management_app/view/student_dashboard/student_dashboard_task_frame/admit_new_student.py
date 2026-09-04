import customtkinter as ctk
from ....utilitis import grid_widget
from ....utilitis import show_grid
class AdmitNewStudent(ctk.CTkFrame):
    def __init__ (self,parent,**kwargs):
        super().__init__(parent,**kwargs) 
        
        for i in range(12):
            self.grid_columnconfigure(i,weight=1)
        for i in range(42):
            self.grid_rowconfigure(i,weight=1)
        
        # show_grid(self=self,ctk=ctk,c=12,r=24)
        # division option:
        
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
        self.blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        self.religions = ["Islam", "Hinduism", "Buddhism", "Christianity"]
            
        # ------------------------------------------------------------ student personal information section -----------------------------------------------
        self.selected_gender=ctk.StringVar(value="male")
        
        self.present_address_section_label= ctk.CTkLabel(self,text="Personal Information",anchor="center",font=("Arial",20))
        grid_widget(entry=self.present_address_section_label,c=0,r=0,colspan=8,rowspan=1,direction="we",px=5,py=0)  
                    
        self.student_name_label= ctk.CTkLabel(self,text="Student Name:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_name_label,c=0,r=1,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_name_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_name_entry,c=1,r=1,colspan=8,rowspan=1,direction="we",px=0,py=0)
        
        self.student_mother_name_label= ctk.CTkLabel(self,text="Mother Name:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_mother_name_label,c=0,r=2,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_mother_name_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_mother_name_entry,c=1,r=2,colspan=8,rowspan=1,direction="we",px=0,py=0)

        self.student_father_name_label= ctk.CTkLabel(self,text="Father Name:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_father_name_label,c=0,r=3,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_father_name_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_father_name_entry,c=1,r=3,colspan=8,rowspan=1,direction="we",px=0,py=0)
        
        self.date_of_birth_label= ctk.CTkLabel(self,text="Date Of Birth:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.date_of_birth_label,c=0,r=4,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.date_of_birth_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.date_of_birth_entry,c=1,r=4,colspan=3,rowspan=1,direction="we",px=0,py=0)
        
        self.student_gender_label= ctk.CTkLabel(self,text="Gender:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_gender_label,c=4,r=4,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_gender_male_radio_button= ctk.CTkRadioButton(self,text="Male",value="male",variable=self.selected_gender)
        grid_widget(entry=self.student_gender_male_radio_button,c=5,r=4,colspan=1,rowspan=1,direction="we",px=0,py=0)
        
        self.student_gender_female_radio_button= ctk.CTkRadioButton(self,text="Female",value="female",variable=self.selected_gender)
        grid_widget(entry=self.student_gender_female_radio_button,c=7,r=4,colspan=1,rowspan=1,direction="we",px=0,py=0) 
        
        
         # ------------------------------------------------------------ student present address -----------------------------------------------
         
        self.present_address_section_label= ctk.CTkLabel(self,text="Present Address",anchor="w",font=("Arial",20))
        grid_widget(entry=self.present_address_section_label,c=0,r=5,colspan=8,rowspan=1,direction="we",px=40,py=0)  
         
        self.student_present_division_label= ctk.CTkLabel(self,text="Division:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_present_division_label,c=0,r=6,colspan=1,rowspan=1,direction="we",px=5,py=0) 
        
        self.student_present_division_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_present_division_option,c=1,r=6,colspan=2,rowspan=1,direction="we",px=5,py=0)
        
        self.student_present_district_label= ctk.CTkLabel(self,text="District:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_present_district_label,c=3,r=6,colspan=1,rowspan=1,direction="we",px=5,py=0) 
        
        self.student_present_district_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_present_district_option,c=4,r=6,colspan=2,rowspan=1,direction="we",px=0,py=0)
                
        self.student_present_upazila_label= ctk.CTkLabel(self,text="Upazila:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_present_upazila_label,c=6,r=6,colspan=1,rowspan=1,direction="we",px=5,py=0) 
        
        self.student_present_upazila_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_present_upazila_option,c=7,r=6,colspan=2,rowspan=1,direction="we",px=0,py=0)
        
        
        self.student_present_address_label= ctk.CTkLabel(self,text="Address:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_present_address_label,c=0,r=7,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_present_address_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_present_address_entry,c=1,r=7,colspan=8,rowspan=1,direction="we",px=0,py=0)
        
        
        # ------------------------------------------------------------ student permanent address -----------------------------------------------
        
        self.permanent_address_section_label= ctk.CTkLabel(self,text="Permanent Address",anchor="w",font=("Arial",20))
        grid_widget(entry=self.permanent_address_section_label,c=0,r=8,colspan=5,rowspan=1,direction="we",px=40,py=0)  
        
        self.permanent_present_same_check= ctk.CTkCheckBox(self,text="Same As Present",font=("Arial",20))
        grid_widget(entry=self.permanent_present_same_check,c=5,r=8,colspan=8,rowspan=1,direction="e",px=320,py=0)   
         
        self.student_permanent_division_label= ctk.CTkLabel(self,text="Division:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_permanent_division_label,c=0,r=9,colspan=1,rowspan=1,direction="we",px=5,py=0) 
        
        self.student_permanent_division_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_permanent_division_option,c=1,r=9,colspan=2,rowspan=1,direction="we",px=5,py=0)
        
        self.student_permanent_district_label= ctk.CTkLabel(self,text="District:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_permanent_district_label,c=3,r=9,colspan=1,rowspan=1,direction="we",px=5,py=0) 
        
        self.student_permanent_district_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_permanent_district_option,c=4,r=9,colspan=2,rowspan=1,direction="we",px=0,py=0)
                
        self.student_permanent_upazila_label= ctk.CTkLabel(self,text="Upazila:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_permanent_upazila_label,c=6,r=9,colspan=1,rowspan=1,direction="we",px=5,py=0) 
        
        self.student_permanent_upazila_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_permanent_upazila_option,c=7,r=9,colspan=2,rowspan=1,direction="we",px=0,py=0)
        
        
        self.student_permanent_address_label= ctk.CTkLabel(self,text="Address:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_permanent_address_label,c=0,r=10,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_permanent_address_entry= ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_permanent_address_entry,c=1,r=10,colspan=8,rowspan=1,direction="we",px=0,py=0)
        
# ------------------------------------------------------------ student contact and other information -----------------------------------------------        

        self.contact_and_other_information_section_label= ctk.CTkLabel(self,text="Student Contact And Other Information",anchor="w",font=("Arial",20))
        grid_widget(entry=self.contact_and_other_information_section_label,c=0,r=11,colspan=8,rowspan=1,direction="we",px=40,py=0)  

        self.student_phone_number_label=ctk.CTkLabel(self,text="Phone Number:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_phone_number_label,c=0,r=12,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_phone_number_entry=ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_phone_number_entry,c=1,r=12,colspan=4,rowspan=1,direction="we",px=5,py=0)
        
        self.student_whatsapp_number_label=ctk.CTkLabel(self,text="Whatsapp Number:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_whatsapp_number_label,c=5,r=12,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_whatsapp_number_entry=ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_whatsapp_number_entry,c=6,r=12,colspan=3,rowspan=1,direction="we",px=5,py=0)
        
        self.student_email_label=ctk.CTkLabel(self,text="Email:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_email_label,c=0,r=13,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_email_entry=ctk.CTkEntry(self,font=("Arial",20))
        grid_widget(entry=self.student_email_entry,c=1,r=13,colspan=4,rowspan=1,direction="we",px=5,py=0)
        
        self.student_blood_group_label=ctk.CTkLabel(self,text="Blood Group:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_blood_group_label,c=5,r=13,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_blood_group_option=ctk.CTkOptionMenu(self,values= self.blood_groups,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_blood_group_option,c=6,r=13,colspan=3,rowspan=1,direction="we",px=5,py=0)

        self.student_religion_label=ctk.CTkLabel(self,text="Religion:",anchor="e",font=("Arial",20))
        grid_widget(entry=self.student_religion_label,c=0,r=14,colspan=1,rowspan=1,direction="we",px=5,py=0)
        
        self.student_religion_option=ctk.CTkOptionMenu(self,values= self.religions,dropdown_font=("Arial", 18),font=("Arial", 18))
        grid_widget(entry=self.student_religion_option,c=1,r=14,colspan=4,rowspan=1,direction="we",px=5,py=0)