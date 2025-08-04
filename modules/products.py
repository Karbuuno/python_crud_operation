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
        for product in products:
            print(f"{product['id']}: {product['name']} ${product['price']} {product['status']}")
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
                
   