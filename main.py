from modules.users import Users
from modules.products import Products

user_manager=Users()
product_manager=Products()

def main():
    print("\n1. Register \n2. Login")
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
            if current_user['role'] == "admin":
                while True:
                    print("\n1. Create product \n2. Update product \n3. Delete product \n4. View products \n0. Logout")
                    admin_choice = input("Select option: ")
                    
                    if admin_choice == "1":
                        name = input("Enter product name: ")
                        price = int(input("Enter product price: "))
                        product_manager.create_products(name, price)
                        print("✅ Product has been successfully created.\n")
                    
                    elif admin_choice == "2":
                        product_id = input("Enter product ID to update: ")
                        updated_name=input("Enter product name to update: ")
                        updated_price=int(input("Enter product price to update: "))
                        product_manager.update_products(product_id,updated_name,updated_price)
                    
                    elif admin_choice == "3":
                        product_id = input("Enter product ID to delete: ")
                        product_manager.delete_products(product_id)
                    
                    elif admin_choice == "4":
                        product_manager.display_products()
                    
                    elif admin_choice == "0":
                        print("Logged out.\n")
                        break
                    else:
                        print("Invalid option.\n")


                        
        except ValueError:
            print("An error occurred. Please try again.\n")
    
if __name__ == "__main__":
    main()       

