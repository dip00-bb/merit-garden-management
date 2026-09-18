from ....utilitis import bangladesh
from ....model import AdmitStudentModel

class AdmitStudentController:
    def __init__(self,personal_information,
                 present_information,
                 permanent_information,
                 admission_information,
                 submit_button,
                 student_repo):
        
        self.same_as_present=False
        self.personal_information=personal_information
        self.present_information=present_information
        self.permanent_information=permanent_information
        self.admission_information=admission_information
        self.submit_button=submit_button
        self.student_repo=student_repo
        
    def collect_student_information_and_save(self):
        
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
        

        # student admission information
        to_admit=self.admission_information.student_admitted_class_option.get()
        group=self.admission_information.student_group_option.get()
        opt_sub=self.admission_information.student_optional_subject_option.get()
        previous_school=self.admission_information.student_previous_school_name_entry.get()
        
        # permanent division
        
        permanent_division=""
        permanent_district=""
        permanent_upazila=""
        permanent_address=""
        
        
        # set student permanent address information
        if (self.same_as_present):
            permanent_division=present_division
            permanent_district=present_district
            permanent_upazila=present_upazila
            permanent_address=present_address
        else:
            
            # student permanent address information
            permanent_division=self.permanent_information.student_permanent_division_option.get()
            permanent_district=self.permanent_information.student_permanent_district_option.get()
            permanent_upazila=self.permanent_information.student_permanent_upazila_option.get()
            permanent_address=self.permanent_information.student_permanent_address_entry.get()
            

        
        
        student_model = AdmitStudentModel(
            student_name=student_name,
            mother_name=mother_name,
            father_name=father_name,
            date_of_birth=date_of_birth,
            gender=gender,
            phone_number=phone_number,
            whats_app_number=whats_app_number,
            email=email,
            blood_group=blood_group,
            religion=religion,

            present_division=present_address,
            present_district=present_district,
            present_upazila=present_upazila,
            present_address=present_address,

            permanent_division=permanent_address,
            permanent_district=permanent_district,
            permanent_upazila=permanent_upazila,
            permanent_address=permanent_address,

            to_admit=to_admit,
            group_name=group,
            opt_sub=opt_sub,
            previous_school=previous_school
        )
        

        self.student_repo.create_student(
            student_model
        )
        
               
    # function of present address
            
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
        
        if(self.same_as_present):
            self.permanent_information.student_permanent_division_option.set(chosen_division)
        
    
    def on_district_change(self,chosen_district):
        self.present_information.student_present_upazila_option.set("Upazila")
        self.present_information.student_present_upazila_option.configure(values=list(bangladesh[self.present_information.selected_division][chosen_district]),state="enabled") 

        if(self.same_as_present):
            self.permanent_information.student_permanent_district_option.set(chosen_district)
    
    
    def on_upazila_change(self,selected_upazila):

        if(self.same_as_present):
            self.permanent_information.student_permanent_upazila_option.set(selected_upazila)
    
    def on_address_field_focus_out(self,x=""):
        if(self.same_as_present):
            present_address=self.present_information.value_of_present_address.get()
            self.permanent_information.student_permanent_address_entry.configure(state="normal")
            self.permanent_information.student_permanent_address_entry.delete(0,"end")
            self.permanent_information.student_permanent_address_entry.insert(0,present_address)
            self.permanent_information.student_permanent_address_entry.configure(state="disabled")
            
            
    # function of permanent address

    def mark_same_as_present(self):
        check_box_state=self.permanent_information.check_var.get()

        
        if(check_box_state=="on"):
            self.same_as_present=True
            
            self.permanent_information.student_permanent_division_option.set(self.present_information.student_present_division_option.get())
            self.permanent_information.student_permanent_district_option.set(self.present_information.student_present_district_option.get())
            self.permanent_information.student_permanent_upazila_option.set(self.present_information.student_present_upazila_option.get())
            self.permanent_information.student_permanent_address_entry.insert(0,self.present_information.student_present_address_entry.get())        
            
            
            
            self.permanent_information.student_permanent_division_option.configure(state="disabled")   
            self.permanent_information.student_permanent_district_option.configure(state="disabled")
            self.permanent_information.student_permanent_upazila_option.configure(state="disabled")
            self.permanent_information.student_permanent_address_entry.configure(state="disabled")
            
        else:
            
            self.same_as_present=False
            
            self.permanent_information.student_permanent_division_option.configure(state="enabled")   
            self.permanent_information.student_permanent_address_entry.configure(state="normal")
            self.permanent_information.student_permanent_address_entry.delete(0,"end")
            self.permanent_information.student_permanent_division_option.set("Division")
            self.permanent_information.student_permanent_district_option.set("District")
            self.permanent_information.student_permanent_upazila_option.set("Upazila")
    
    def on_permanent_division_change(self,chosen_division):
        self.permanent_information.selected_division=chosen_division
        self.permanent_information.student_permanent_district_option.set("District")
        self.permanent_information.student_permanent_district_option.configure(values=list(bangladesh[chosen_division].keys()),state="enabled")                    
            
            
    def on_permanent_district_change (self,chosen_district):       
        
        self.permanent_information.student_permanent_upazila_option.set("Upazila")
        self.permanent_information.student_permanent_upazila_option.configure(values=list(bangladesh[self.permanent_information.selected_division][chosen_district]),state="enabled")   