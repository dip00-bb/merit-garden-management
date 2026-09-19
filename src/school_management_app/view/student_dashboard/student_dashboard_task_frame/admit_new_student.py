import customtkinter as ctk
from ....utilitis import grid_widget
from ....utilitis import show_grid

from ....components import PersonalInformation
from ....components import PresentAddress
from ....components import PermanentAddress
from ....components import AdmissionInformation
from ....controller import AdmitStudentController
from CTkMessagebox import CTkMessagebox
class AdmitNewStudent(ctk.CTkFrame):
    def __init__ (self,parent,student_repo,**kwargs):
        super().__init__(parent,**kwargs) 
        

        self.controller=None
        self.pack_propagate(False)
        self.student_repo=student_repo
        
        
        # ------------------------------------------------------------ student personal information section -----------------------------------------------
        self.student_personal_information=PersonalInformation(self)
        self.student_personal_information.pack(fill="both",expand=True)
         # ------------------------------------------------------------ student present address -----------------------------------------------
        self.student_present_address=PresentAddress(self)
        self.student_present_address.pack(fill="both",expand=True)
        # ------------------------------------------------------------ student permanent address -----------------------------------------------
        self.student_permanent_address=PermanentAddress(self)
        self.student_permanent_address.pack(fill="both",expand=True)
        # ------------------------------------------------------------ student admission information -----------------------------------------------                
        self.admission_information=AdmissionInformation(self)
        self.admission_information.pack(fill="both",expand=True)     
        # ------------------------------------------------------------ submit button -----------------------------------------------
        self.submit_information=ctk.CTkButton(self,text="Add Student")
        self.submit_information.pack(ipadx=10,ipady=10)
        
        
        admit_student_controller=AdmitStudentController(
            information_field_parent=self,
            submit_button=self.submit_information,
            student_repo=self.student_repo
            )
           
        self.student_permanent_address.set_controller(admit_student_controller)
        self.student_present_address.set_controller(admit_student_controller)    



        self.submit_information.configure(command=admit_student_controller.collect_student_information_and_save)
        
    def show_error(self,message):
        self.error_message=CTkMessagebox(self,title="Error",message=message,icon="cancel")
        screen_x = self.winfo_screenmmwidth()
        screen_y = self.winfo_screenheight()/3
        
        self.error_message.geometry(f"+{screen_x}+{screen_y}")            