import customtkinter as ctk
from ....components import ManageFee
from ....components import FindStudent
from ....controller import FeesController
from ....components import StudentList

from ....utilitis import grid_widget

class FeesManagement(ctk.CTkFrame):
    def __init__ (self,parent,fees_repo, student_repo, fees_model,**kwargs):
        super().__init__(parent,fg_color="green",**kwargs) 
        
        
        self.pack_propagate(False)
        
        self.model=fees_model
        self.fees_repo=fees_repo
        self.student_repo=student_repo
        self.grid_widget=grid_widget

        
        self.fetched_information=[]
        
        self.find_student= FindStudent(self)
        self.find_student.pack(pady=10)
        
        self.fees_view=ManageFee(self)
        if (len(self.fetched_information)>1):
            self.fees_view.pack(pady=10)
        
        


       
        self.fees_management_controller=FeesController(
            view=self,
            model=self.model,
            student_repo=self.student_repo,
            app=parent
        )
        
        self.find_student.set_controller(self.fees_management_controller)
        self.fees_view.set_controller(self.fees_management_controller)