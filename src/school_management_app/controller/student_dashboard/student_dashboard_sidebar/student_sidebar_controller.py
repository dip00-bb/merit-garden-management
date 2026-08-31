class StudentDashboardController:
        def __init__(self,view,model,app):
            self.view=view
            self.model=model
            self.app=app
        
        def get_selected_task(self,key="attendance"):
            print(key)
            selected_task=self.model.check_task(key)
            
            if(selected_task=="attendance"):
                self.app.attach_attendance_frame()
            elif (selected_task=="result_monitor"):
                self.app.attach_school_result_monitor_frame()
            elif(selected_task=="board_result_monitor"):
                self.app.attach_board_result_monitor_frame()
            elif (selected_task=="admit_student"):
                self.app.attach_admit_student_frame()
            elif(selected_task=="fees_management"):
                self.app.attach_fees_management_frame()
            elif (selected_task=="result_management"):
                self.app.attach_result_management_frame()
            elif (selected_task=="show_result"):
                self.app.attach_show_result_frame()
                