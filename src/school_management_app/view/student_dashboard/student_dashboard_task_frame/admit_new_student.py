import customtkinter as ctk
from ....utilitis import grid_widget
from ....utilitis import show_grid

from ....components import PersonalInformation
from ....components import PresentAddress
from ....components import PermanentAddress
from ....components import ContactInformation
from ....components import AdmissionInformation

class AdmitNewStudent(ctk.CTkFrame):
    def __init__ (self,parent,**kwargs):
        super().__init__(parent,**kwargs) 
        


        self.pack_propagate(False)
        
        # ------------------------------------------------------------ student personal information section -----------------------------------------------
        self.student_personal_information=PersonalInformation(self)
        self.student_personal_information.pack(fill="both",expand=True)
         # ------------------------------------------------------------ student present address -----------------------------------------------
        self.student_present_address=PresentAddress(self)
        self.student_present_address.pack(fill="both",expand=True)
        # ------------------------------------------------------------ student permanent address -----------------------------------------------
        self.student_permanent_address=PermanentAddress(self)
        self.student_permanent_address.pack(fill="both",expand=True)
        # ------------------------------------------------------------ student contact and other information -----------------------------------------------        
        self.contact_information=ContactInformation(self)
        self.contact_information.pack(fill="both",expand=True)
        # ------------------------------------------------------------ student admission information -----------------------------------------------                
        self.admission_information=AdmissionInformation(self)
        self.admission_information.pack(fill="both",expand=True)     