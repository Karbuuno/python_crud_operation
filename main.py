from modules.users import Users
from modules.products import Products

user_manager=Users()
product_manager=Products()

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
                    if current_user['role']=="user":
                        product_manager.display_products()
                    elif current_user['role']=="admin":
                        name=input("Enter product name: ")
                        price=int(input("Enter product price: "))
                        product_manager.create_products(name,price)
                        print(f"Product has been successfully created")

                    break
                elif choice == "0":
                    print("Goodbye!")
            break

            
        except ValueError:
            print("An error occurred. Please try again.\n")
    
if __name__ == "__main__":
    main()       

