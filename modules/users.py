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
        except FileNotFoundError:
            return []
        
    ##  update user data
    def save_user(self):
        with open(self.file_path,"w") as f:
            return json.dump(self.users, f,indent=4)
    ## register  user 
    def register_user(self, name, username, password):
        for user in self.users:
           if user['username']==username:
               print("username already exist")
               return
        new_user={
               "name":name,
               "username":username,
               "password":password,
               "role": "user",
               "products": [] 
           }
        self.users.append(new_user)
        ## save user data to json fle
        self.save_user()
        # with open(self.file_path, "w") as f:
        #     json.dump(self.users,f,indent=4)  
        #     print("user registered successfully")

    ## Get user data
    def login(self,username,password):
        for user in self.users:
            if user["username"]==username and user["password"] == password:
             return user
        print("Invalid username or password.")
        return None
                

