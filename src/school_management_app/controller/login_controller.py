

class LoginController:
    def __init__(self,view,model,app):
        self.view=view
        self.model=model
        self.app=app
        
    def login(self):
        username=self.view.username_entry.get()
        password=self.view.password_entry.get()
        
        success=self.model.authenticate(
            username,password
        )
        
        if success:
            print("Success")
            self.app.on_login_success()
        else:
            print("Failed")
            
            return