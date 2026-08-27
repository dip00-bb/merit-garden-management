class UserModel:
    def authenticate(self,username,password):
        if username=="admin" and password=="1234":
            return True
         
        return False 

