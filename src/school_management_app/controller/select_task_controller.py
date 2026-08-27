class SelectTaskController:
    def __init__(self,view,model,app):
        self.view=view
        self.model=model
        self.app=app
        
    def select(self):

        radio_value=self.view.selected

        employee_type=self.model.handle_select_task(radio_value)
        
        if employee_type=="teachers":
            print("Teachers Has Been Selected")
        elif employee_type == "students":
            print("Students Has Been Selected")
        else:
            print("Staffs Has Been Selected")