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
    def display_products(self):
        products=self.load_products()
        print("All Products:")
        for product in products:
            print(f"{product['id']}: {product['name']} ${product['price']} {product['status']}")
