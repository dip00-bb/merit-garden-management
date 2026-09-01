import customtkinter as ctk
from .student_dashboard_sidebar.student_sidebar import StudentDashboardSidebar
from ...utilitis import grid_widget
from ...utilitis import show_grid
from .student_dashboard_task_frame.attendance import Attendance
from .student_dashboard_task_frame.result_management import ResultManagement
from .student_dashboard_task_frame.show_result import ShowResult
from .student_dashboard_task_frame.result_monitor import ResultMonitor
from .student_dashboard_task_frame.board_result import BoardResult
from .student_dashboard_task_frame.admit_new_student import AdmitNewStudent
from .student_dashboard_task_frame.fees_management import FeesManagement

from ...controller import StudentDashboardController
from ...model import StudentDashboardModel

class StudentDashboard(ctk.CTkFrame):
    def __init__(self,parent,height,weight,**kwargs):
        super().__init__(parent,height=height,width=weight,**kwargs)
        
        self.pack_propagate(False)
        # frames
        self.attendance_frame=Attendance(
            self
        )
        self.school_result_monitor_frame=ResultMonitor(
            self
        )
        self.board_result_monitor_frame=BoardResult(
            self
        )
        self.admit_student_frame=AdmitNewStudent(
            self
        )
        self.fees_management_frame=FeesManagement(
            self
        )
        self.result_management_frame=ResultManagement(
            self
        )
        self.show_result_frame=ShowResult(
            self
        )   
        
        self.current_frame=self.attendance_frame
        grid_widget(
            entry=self.attendance_frame,
            c=1,
            colspan=11,
            r=0,
            rowspan=24,
            direction="nsew",
            px=0,
            py=0,
        )
        
        for i in range(12):
            self.grid_columnconfigure(i,weight=1)
        for i in range (24):
            self.grid_rowconfigure(i,weight=1)
            
        # sidebar
        self.student_dashboard_model=StudentDashboardModel()
        self.student_sidebar_view=StudentDashboardSidebar(
            self,
        )
        # sidebar controller
        sidebar_controller=StudentDashboardController(self.student_sidebar_view,self.student_dashboard_model,self)
        self.student_sidebar_view.set_controller(sidebar_controller)
        
        # attaching sidebar with dashboard
        grid_widget(
            entry=self.student_sidebar_view,
            c=0,
            colspan=1,
            r=0,
            rowspan=24,
            px=0,
            py=0,
            direction="nsew"
        )        
    # attaching frames with dashboard
     
    def attach_attendance_frame(self):    
        
        if self.current_frame is not None:
            self.current_frame.grid_forget()
        self.current_frame=self.attendance_frame
        
        grid_widget(
            entry=self.attendance_frame,
            c=1,
            colspan=11,
            r=0,
            rowspan=24,
            direction="nsew",
            px=0,
            py=0,
        )
  
    def attach_school_result_monitor_frame(self):    
        
        if self.current_frame is not None:
            self.current_frame.grid_forget()
        self.current_frame=self.school_result_monitor_frame
        
        grid_widget(
            entry=self.school_result_monitor_frame,
            c=1,
            colspan=11,
            r=0,
            rowspan=24,
            direction="nsew",
            px=0,
            py=0,
        )
    def attach_board_result_monitor_frame(self):    
        
        if self.current_frame is not None:
            self.current_frame.grid_forget()
        self.current_frame=self.board_result_monitor_frame
        
        grid_widget(
            entry=self.board_result_monitor_frame,
            c=1,
            colspan=11,
            r=0,
            rowspan=24,
            direction="nsew",
            px=0,
            py=0,
        )
    def attach_admit_student_frame(self):    
        
        if self.current_frame is not None:
            self.current_frame.grid_forget()
        self.current_frame=self.admit_student_frame
               
        grid_widget(
            entry=self.admit_student_frame,
            c=1,
            colspan=11,
            r=0,
            rowspan=24,
            direction="nsew",
            px=0,
            py=0,
        )
  
    def attach_fees_management_frame(self):    

        if self.current_frame is not None:
            self.current_frame.grid_forget()
        self.current_frame=self.fees_management_frame        
        
        grid_widget(
            entry=self.fees_management_frame,
            c=1,
            colspan=11,
            r=0,
            rowspan=24,
            direction="nsew",
            px=0,
            py=0,
        )
    def attach_result_management_frame(self):    
        if self.current_frame is not None:
            self.current_frame.grid_forget()
        self.current_frame=self.result_management_frame           
        grid_widget(
            entry=self.result_management_frame,
            c=1,
            colspan=11,
            r=0,
            rowspan=24,
            direction="nsew",
            px=0,
            py=0,
        ) 
    def attach_show_result_frame(self):    

        if self.current_frame is not None:
            self.current_frame.grid_forget()
        self.current_frame=self.show_result_frame          
        
        grid_widget(
            entry=self.show_result_frame,
            c=1,
            colspan=11,
            r=0,
            rowspan=24,
            direction="nsew",
            px=0,
            py=0,
        )