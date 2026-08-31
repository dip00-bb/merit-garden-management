import customtkinter as ctk
from ....utilitis import grid_widget
from ....utilitis import load_image_and_resize
from ....utilitis import show_grid

image_list=[
        "attendance.png",
        "school_result_monitor.png",
        "board_result_monitor.png",
        "admit_student.png",
        "fees_management.png",
        "result_management.png",
        "find_result.png"
            
    ]
        


class StudentDashboardSidebar(ctk.CTkFrame):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        
        self.pack_propagate(False)
        
        for i in range (24):
            self.grid_rowconfigure(i,weight=1)
            
        self.grid_columnconfigure(0,weight=1)
        
        
        self.icons=[]
        for icon in image_list:
            self.icon=load_image_and_resize(20,20,f"student_dashboard/student_dashboard_sidebar/{icon}")
            
            self.task_icons=ctk.CTkImage(
                light_image=self.icon,
                size=(25,25),
            )
            self.icons.append(self.task_icons)
        
        
        task_dic={
            "attendance":{
                "text":"Attendance",
                "img":self.icons[0]
            },
            
            "result_monitor":{
                "text":"Result Monitor",
                "img":self.icons[1]
            },
            
            "board_result_monitor":{
                "text":"Board Result Monitor",
                "img":self.icons[2]
            },
            
            "admit_student":{
                "text":"Admit Student",
                "img":self.icons[3]
            },
            
            "fees_management":{
                "text":"Fees Management",
                "img":self.icons[4]
            },
            
            "result_management":{
                "text":"Result Management",
                "img":self.icons[5]
            },
            
            "show_result":{
                "text":"Show Result",
                "img":self.icons[6]
            },            
            
        }
        
        

        for index , (key,value) in enumerate(task_dic.items()):
            
            self.sidebar_button=ctk.CTkButton(
                master=self,
                text=value["text"],
                border_width=0,
                corner_radius=5,
                font=("Arial", 20),
                image=value["img"],
                compound="left",
                anchor="w",
                command=lambda key=key : self.controller.get_selected_task(key)
            )
            
            grid_widget(
                entry=self.sidebar_button,
                c=0,
                r=index,
                px=0,
                py=2,
                direction="nwes"
            )
    def set_controller(self,controller):
        self.controller=controller
        