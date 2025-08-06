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
    def save_user(self, users):
        self.users = users
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
        self.save_user(user)
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

    ## User Profile
    def user_profile(self,username):
        users=self.load_users()
        for user in users:
            if user['username']==username:
                print("Your Profile")
                print(f"name: {user['name']} Username: {user['username']}")
                return user
        print("There is no user found")

        ## Update user profile

    def update_user_profile(self,username, new_name,new_username,new_password ):
        users=self.load_users()
        for user in users:
            if user['username']==username:
                user["name"]=new_name
                user["username"]=new_username
                user["password"]=new_password
                print(f"Your name and your username has been updated")
                self.save_user(users)


