import json
import uuid
from modules.users import Users


class Products:
    def __init__(self,file_path="data/products.json"):
        self.file_path=file_path
        self.products=self.load_products()

    def load_products(self):
        try:
            with open(self.file_path,"r") as f:
                return json.load(f)
                                
        except FileNotFoundError:
            return []
        ## update products data
    def save_products(self,products):
        with open(self.file_path,"w") as f:
            return json.dump(products, f,indent=4)
    ## display products
    def display_products(self):
        products=self.load_products()
        print("All Products:")
        if products:
            for product in products:
                if product['status']=="available":
                    print(f"{product['id']}: {product['name']} ${product['price']} {product['status']}")
            return
        else:
            print("There is no Products yet")
    
    ##crete products
    def create_products(self, name,price):
            self.id=str(uuid.uuid4())[:6]
            self.status="available"
            products=self.load_products()
            new_product = {
                "id": str(uuid.uuid4())[:6],
                "name": name,
                "price": price,
                "status": "available"
            }
            products.append(new_product)
            ## save updating data in json file
            self.save_products(products)



        ## Buy products
    def buy_products(self,product_id,username):
         products=self.load_products()
         users=Users().load_users()
         for product in products:
            if product['id']==product_id:
                
                for user in users:
                    if user['username']==username and user['role']=="user":
                        product['status']="sold"
                        user['products'].append({
                            "id":product['id'],
                            "name":product['name'],
                            "price":product['price']
                        })
                        self.save_products(products)
                        Users().save_user(users)
                        print(f"You have successfully bought '{product['name']}'\n")
                        return

                print("User not found.\n")
                return

            print("Product not found.\n")
    

    ## View my products
    def view_my_products(self, username):
        users=Users().load_users()
        # Products=self.load_products()
        for user in users:
            user['username']==username
            for product in user['products']:
                print("Your Products")
                print(f"{user['products']['name']}: {user['product']['price']} ")
            else:
                print("There is no products")
            return
        ## updating products
    def update_products(self,product_id,updated_name,updated_price):
        products=self.load_products()
        updated=False
        for product in products:
            if product["id"]==product_id:
                if updated_name:
                    product["name"]=updated_name
                if updated_price:
                    product["price"]=updated_price
                updated=True
                break
        if updated:
                self.save_products(products)
                print(f"Product ID {product_id} has been updated successfully.\n")
        else:
                print("product not found")

        ## Deleting products
    def delete_products(self, product_id):
        products=self.load_products()
        products=[product for product in products if product["id"]!=product_id]
        # for product in products:
        #     if product["id"]==product_id:
        #         products.remove(product)
        self.save_products(products)
        print(f"Product {product_id} deleted successfully.")
                
   