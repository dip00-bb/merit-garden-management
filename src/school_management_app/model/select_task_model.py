class SelectTaskModel:
    def handle_select_task(self,selected):
        if selected=="teachers":
            return "teachers"
        elif selected == "students":
            return "students"
        else:
            return "staffs"