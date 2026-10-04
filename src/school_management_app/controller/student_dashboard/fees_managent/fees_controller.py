from ....components.common_component.student_list import StudentList

class FeesController:
    def __init__(self, view,student_repo, model,app):
        self.view = view
        self.model = model
        self.app = app 
        self.student_repo=student_repo
        
    def search_for_student(self):
        year=self.view.find_student.year_entry.get()
        class_= self.view.find_student.class_option.get()
        
        fetched_data=self.student_repo.get_students_by_class_and_year(class_,year)
        students= [dict(student) for student in fetched_data]
        
        for student in students:
            student_list=StudentList(self.view,student_name=student['student_name'],student_class=student['current_class'],student_roll=student['class_roll'],r=0)
            student_list.pack(pady=10)
        

    def print_2(self):
        print(self.view.x)