import json
import uuid
from modules.users import Users


class Products:
    def __init__(self,file_path="data/products.json"):
        self.file_path=file_path
        self.users=self.load_products()

    def load_products(self):
        try:
            with open(self.file_path,"r") as f:
                return json.load(f)
                                
        except FileNotFoundError:
            return []
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


            with open(self.file_path, "w") as f:
                return json.dump(products,f,indent=
                                 4)
        