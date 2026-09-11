import customtkinter as ctk
from ....utilitis import grid_widget
from ....utilitis import show_grid

from ....components import PersonalInformation
from ....components import PresentAddress
from ....components import PermanentAddress
from ....components import AdmissionInformation
from ....controller import AdmitStudentController
from ....model import AdmitStudentModel

class AdmitNewStudent(ctk.CTkFrame):
    def __init__ (self,parent,**kwargs):
        super().__init__(parent,**kwargs) 
        

        self.controller=None
        self.pack_propagate(False)
        self.student_permanent_address=""
        
        
        
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
        
        self.admit_student_model=AdmitStudentModel()
        admit_student_controller=AdmitStudentController(
            
            personal_information=self.student_personal_information,
            present_information=self.student_present_address,
            permanent_information=self.student_permanent_address,
            admission_information=self.admission_information,
            submit_button=self.submit_information,
            model=self.admit_student_model
            )
           
        self.student_permanent_address.set_controller(admit_student_controller)
        self.student_present_address.set_controller(admit_student_controller)    



        self.submit_information.configure(command=admit_student_controller.collect_personal_information)
           