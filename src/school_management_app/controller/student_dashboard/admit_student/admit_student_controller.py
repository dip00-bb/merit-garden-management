from ....utilitis import bangladesh

class AdmitStudentController:
    def __init__(self,personal_information,present_information,permanent_information,admission_information,submit_button,model):
        
        self.personal_information=personal_information
        self.present_information=present_information
        self.permanent_information=permanent_information
        self.admission_information=admission_information
        self.submit_button=submit_button
        self.model=model
        
    def collect_personal_information(self):
        
        # student personal information
        student_name=self.personal_information.student_name_entry.get()
        mother_name=self.personal_information.student_mother_name_entry.get()
        father_name=self.personal_information.student_father_name_entry.get()
        date_of_birth=self.personal_information.date_of_birth_entry.get()
        gender=self.personal_information.selected_gender.get()
        phone_number=self.personal_information.student_phone_number_entry.get()
        whats_app_number=self.personal_information.student_whatsapp_number_entry.get()
        email=self.personal_information.student_email_entry.get()
        blood_group=self.personal_information.student_blood_group_option.get()
        religion=self.personal_information.student_religion_option.get()
        
        # student present address information 
        present_division=self.present_information.student_present_division_option.get()
        present_district=self.present_information.student_present_district_option.get()
        present_upazila=self.present_information.student_present_upazila_option.get()
        present_address=self.present_information.student_present_address_entry.get()
        

        
                
        # set personal information to model
        
        self.model.student_name=student_name
        self.model.mother_name=mother_name
        self.model.father_name=father_name
        self.model.date_of_birth=date_of_birth
        self.model.gender=gender
        self.model.phone_number=phone_number
        self.model.whats_app_number=whats_app_number
        self.model.email=email
        self.model.blood_group=blood_group
        self.model.religion=religion
        
        # set present address information to model 
        
        self.model.present_division=present_division
        self.model.present_district=present_district
        self.model.present_upazila=present_upazila
        self.model.present_address=present_address
       
       
        if (self.model.same_as_present):
            self.model.permanent_division=present_division
            self.model.permanent_district=present_district
            self.model.permanent_upazila=present_upazila
            self.model.permanent_address=present_address
        else:
            
            # student permanent address information
            permanent_division=self.permanent_information.student_permanent_division_option.get()
            permanent_district=self.permanent_information.student_permanent_district_option.get()
            permanent_upazila=self.permanent_information.student_permanent_upazila_option.get()
            permanent_address=self.permanent_information.student_permanent_address_entry.get()
            
            self.model.permanent_division=permanent_division
            self.model.permanent_district=permanent_district
            self.model.permanent_upazila=permanent_upazila
            self.model.permanent_address=permanent_address  
            
            
            
               
    def collect_present_information(self):
        print(self.model.student_name)
    
    def collect_permanent_information():
        pass 
    
    def collect_admission_information():
        pass 
    
    def mark_same_as_present(self):
        check_box_state=self.permanent_information.check_var.get()

        
        if(check_box_state=="on"):
            self.model.same_as_present=True
            
            self.permanent_information.student_permanent_division_option.set(self.present_information.student_present_division_option.get())
            self.permanent_information.student_permanent_district_option.set(self.present_information.student_present_district_option.get())
            self.permanent_information.student_permanent_upazila_option.set(self.present_information.student_present_upazila_option.get())
            self.permanent_information.student_permanent_address_entry.insert(0,self.present_information.student_present_address_entry.get())        
            
            
            
            self.permanent_information.student_permanent_division_option.configure(state="disabled")   
            self.permanent_information.student_permanent_district_option.configure(state="disabled")
            self.permanent_information.student_permanent_upazila_option.configure(state="disabled")
            self.permanent_information.student_permanent_address_entry.configure(state="disabled")
            
        else:
            
            self.model.same_as_present=False
            
            self.permanent_information.student_permanent_division_option.configure(state="enabled")   
            self.permanent_information.student_permanent_address_entry.configure(state="normal")
            self.permanent_information.student_permanent_address_entry.delete(0,"end")
            self.permanent_information.student_permanent_division_option.set("Division")
            self.permanent_information.student_permanent_district_option.set("District")
            self.permanent_information.student_permanent_upazila_option.set("Upazila")
            
    def on_division_change(self,chosen_division):
        self.present_information.selected_division=chosen_division

        # reset the variable value
        self.present_information.value_of_present_district.set("")
        self.present_information.value_of_present_upazila.set("")
        
        # reset the title 
        self.present_information.student_present_district_option.set("District")
        self.present_information.student_present_upazila_option.set("Upazila")
        
        self.present_information.student_present_district_option.configure(values=list(bangladesh[chosen_division].keys()),state="enabled")
        self.present_information.student_present_upazila_option.configure(state="disabled") 
        
        # sync with permanent if same as present are marked
        
        if(self.model.same_as_present):
            self.permanent_information.student_permanent_division_option.set(chosen_division)
        
    
    def on_district_change(self,chosen_district):
        self.present_information.student_present_upazila_option.set("Upazila")
        self.present_information.student_present_upazila_option.configure(values=list(bangladesh[self.present_information.selected_division][chosen_district]),state="enabled") 

        if(self.model.same_as_present):
            self.permanent_information.student_permanent_district_option.set(chosen_district)
    
    
    def on_upazila_change(self,selected_upazila):

        if(self.model.same_as_present):
            self.permanent_information.student_permanent_upazila_option.set(selected_upazila)
    
    def on_address_field_focus_out(self,x=""):
        if(self.model.same_as_present):
            present_address=self.present_information.value_of_present_address.get()
            self.permanent_information.student_permanent_address_entry.configure(state="normal")
            self.permanent_information.student_permanent_address_entry.delete(0,"end")
            self.permanent_information.student_permanent_address_entry.insert(0,present_address)
            self.permanent_information.student_permanent_address_entry.configure(state="disabled")
            
            
            
            
            
            