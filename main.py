from modules.users import Users

user_manager=Users()

def main():
    choice=input("Enter option: ")
    while True:
        try:
            if choice == "q":
                break
            if choice=="1":
                name=input("Name: ")
                username=input("Username: ")
                password=input("Password: ")
                user_manager.register_user(name,username,password)
            if choice=="2":
                username=input("Username: ")
                password=input("Password: ")
                
                current_user=user_manager.login(username, password)
                if current_user:              
                    print(f"\nWelcome Name: {current_user['name']} Role: {current_user['role']}")
                    break
                elif choice == "0":
                    print("Goodbye!")
                    break

            else:
             print("❌ Invalid option")
            
        except ValueError:
            print("An error occurred. Please try again.\n")
    
if __name__ == "__main__":
    main()       

