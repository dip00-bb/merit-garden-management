from ....utilitis import bangladesh
from ....model import AdmitStudentModel
from email_validator import EmailNotValidError
class AdmitStudentController:
    def __init__(self,
                 information_field_parent,
                 submit_button,
                 student_repo):
        
        self.same_as_present=False
        self.submit_button=submit_button
        self.student_repo=student_repo
        self.information_field_parent=information_field_parent
        
        self.student_personal_information=self.information_field_parent.student_personal_information
        self.student_present_address=self.information_field_parent.student_present_address
        self.student_permanent=self.information_field_parent.student_permanent_address
        self.student_admission_information=self.information_field_parent.admission_information
        
    def collect_student_information_and_save(self):
        
        # student personal information
        student_name=self.student_personal_information.student_name_entry.get()
        student_image=self.student_personal_information.student_image.image_data
        mother_name=self.student_personal_information.student_mother_name_entry.get()
        father_name=self.student_personal_information.student_father_name_entry.get()
        date_of_birth=self.student_personal_information.date_of_birth_entry.get()
        gender=self.student_personal_information.selected_gender.get()
        phone_number=self.student_personal_information.student_phone_number_entry.get()
        whats_app_number=self.student_personal_information.student_whatsapp_number_entry.get()
        email=self.student_personal_information.student_email_entry.get()
        blood_group=self.student_personal_information.student_blood_group_option.get()
        religion=self.student_personal_information.student_religion_option.get()
        
        # student present address information 
        present_division=self.student_present_address.student_present_division_option.get()
        present_district=self.student_present_address.student_present_district_option.get()
        present_upazila=self.student_present_address.student_present_upazila_option.get()
        present_address=self.student_present_address.student_present_address_entry.get()
        

        # student admission information
        to_admit=self.student_admission_information.student_admitted_class_option.get()
        group=self.student_admission_information.student_group_option.get()
        opt_sub=self.student_admission_information.student_optional_subject_option.get()
        previous_school=self.student_admission_information.student_previous_school_name_entry.get()
        
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
            permanent_division=self.student_permanent.student_permanent_division_option.get()
            permanent_district=self.student_permanent.student_permanent_district_option.get()
            permanent_upazila=self.student_permanent.student_permanent_upazila_option.get()
            permanent_address=self.student_permanent.student_permanent_address_entry.get()
            

        
        try:
            student_model = AdmitStudentModel(
                student_name=student_name,
                student_image=student_image,
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
        except ValueError as e:
            error_msg= str(e)
            self.information_field_parent.show_error(error_msg)
            return
        self.student_repo.create_student(
            student_model
        )
        
               
    # function of present address
            
    def on_division_change(self,chosen_division):
        self.student_present_address.selected_division=chosen_division

        # reset the variable value
        self.student_present_address.value_of_present_district.set("")
        self.student_present_address.value_of_present_upazila.set("")
        
        # reset the title 
        self.student_present_address.student_present_district_option.set("District")
        self.student_present_address.student_present_upazila_option.set("Upazila")
        
        self.student_present_address.student_present_district_option.configure(values=list(bangladesh[chosen_division].keys()),state="enabled")
        self.student_present_address.student_present_upazila_option.configure(state="disabled") 
        
        # sync with permanent if same as present are marked
        
        if(self.same_as_present):
            self.student_permanent.student_permanent_division_option.set(chosen_division)
        
    
    def on_district_change(self,chosen_district):
        self.student_present_address.student_present_upazila_option.set("Upazila")
        self.student_present_address.student_present_upazila_option.configure(values=list(bangladesh[self.student_present_address.selected_division][chosen_district]),state="enabled") 

        if(self.same_as_present):
            self.student_permanent.student_permanent_district_option.set(chosen_district)
    
    
    def on_upazila_change(self,selected_upazila):

        if(self.same_as_present):
            self.student_permanent.student_permanent_upazila_option.set(selected_upazila)
    
    def on_address_field_focus_out(self,x=""):
        if(self.same_as_present):
            present_address=self.student_present_address.value_of_present_address.get()
            self.student_permanent.student_permanent_address_entry.configure(state="normal")
            self.student_permanent.student_permanent_address_entry.delete(0,"end")
            self.student_permanent.student_permanent_address_entry.insert(0,present_address)
            self.student_permanent.student_permanent_address_entry.configure(state="disabled")
            
            
    # function of permanent address

    def mark_same_as_present(self):
        check_box_state=self.student_permanent.check_var.get()

        
        if(check_box_state=="on"):
            self.same_as_present=True
            
            self.student_permanent.student_permanent_division_option.set(self.student_present_address.student_present_division_option.get())
            self.student_permanent.student_permanent_district_option.set(self.student_present_address.student_present_district_option.get())
            self.student_permanent.student_permanent_upazila_option.set(self.student_present_address.student_present_upazila_option.get())
            self.student_permanent.student_permanent_address_entry.insert(0,self.student_present_address.student_present_address_entry.get())        
            
            
            
            self.student_permanent.student_permanent_division_option.configure(state="disabled")   
            self.student_permanent.student_permanent_district_option.configure(state="disabled")
            self.student_permanent.student_permanent_upazila_option.configure(state="disabled")
            self.student_permanent.student_permanent_address_entry.configure(state="disabled")
            
        else:
            
            self.same_as_present=False
            
            self.student_permanent.student_permanent_division_option.configure(state="enabled")   
            self.student_permanent.student_permanent_address_entry.configure(state="normal")
            self.student_permanent.student_permanent_address_entry.delete(0,"end")
            self.student_permanent.student_permanent_division_option.set("Division")
            self.student_permanent.student_permanent_district_option.set("District")
            self.student_permanent.student_permanent_upazila_option.set("Upazila")
    
    def on_permanent_division_change(self,chosen_division):
        self.student_permanent.selected_division=chosen_division
        self.student_permanent.student_permanent_district_option.set("District")
        self.student_permanent.student_permanent_district_option.configure(values=list(bangladesh[chosen_division].keys()),state="enabled")                    
            
            
    def on_permanent_district_change (self,chosen_district):       
        
        self.student_permanent.student_permanent_upazila_option.set("Upazila")
        self.student_permanent.student_permanent_upazila_option.configure(values=list(bangladesh[self.student_permanent.selected_division][chosen_district]),state="enabled")   