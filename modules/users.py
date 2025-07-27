import json 
class Users:
    def __init__(self,file_path="data/users.json"):
        self.file_path=file_path
        self.users=self.load_users()

    ##get data
    def load_users(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
            print(f)
        except FileNotFoundError:
            return []
    ## save user to JSON data
    def register_user(self):
        with open(self.file_path, "w") as f:
            json.dumps(self.users,f,indent=4)  

    ## Get user data
    def login(self,username,password):
        for user in self.users:
            if user["username"]==username and user["password"] == password:
                return user

