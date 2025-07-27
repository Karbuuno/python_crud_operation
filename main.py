from modules.users import Users

user_manager=Users()

def main():
    choice=input("Enter option: ")
    while True:
        try:
            if choice == "q":
                break
            if choice=="1":
                username=input("Username: ")
                password=input("Password: ")
                
                current_user=user_manager.login(username, password)
                if not current_user:
                    print("invalid credentials")
                    return
                print(f"\nWelcome Name: {current_user['name']} Role: {current_user['role']}")
                break
            else:
                print("Invalid option\n")
        except ValueError:
            print("An error occurred. Please try again.\n")
    
if __name__ == "__main__":
    main()       

