import customtkinter as ctk
from .student_sidebar import StudentDashboardSidebar
from ...utilitis import grid_widget
class StudentDashboard(ctk.CTkFrame):
    def __init__(self,parent,height,weight,**kwargs):
        super().__init__(parent,height=height,width=weight,fg_color="green",**kwargs)
        
        self.pack_propagate(False)

        
        for i in range(12):
            self.grid_columnconfigure(i,weight=1)
        for i in range (24):
            self.grid_rowconfigure(i,weight=1)
            
 
        self.student_sidebar=StudentDashboardSidebar(
            self,
        )
        
        grid_widget(
            entry=self.student_sidebar,
            c=0,
            colspan=1,
            r=0,
            rowspan=24,
            px=0,
            py=0,
            direction="nsew"
        )