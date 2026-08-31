class StudentDashboardModel:
    def check_task(self,task_type):
        if task_type =="attendance":
            return "attendance"
        elif task_type == "board_result_monitor":
            return "board_result_monitor"
        elif task_type == "admit_student":
            return "admit_student"
        elif task_type == "fees_management":
            return "fees_management"
        elif task_type == "result_management":
            return "result_management"
        elif task_type == "show_result":
            return "show_result"
        else:
            return       
