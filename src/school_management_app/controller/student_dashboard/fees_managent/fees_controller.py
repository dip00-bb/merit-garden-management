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
            self.view.student_list=StudentList(self.view,
                                               student_id=student['student_id'],
                                               student_name=student['student_name'],
                                               student_class=student['current_class'],
                                               student_roll=student['class_roll'],
                                               r=len(students))
            
            self.view.student_list.set_controller(self)
            self.view.student_list.pack(pady=10,padx=20,fill="x")
        

    def print_student_id(self,student_id):
        print(f"Student ID: {student_id}")