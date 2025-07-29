class User:
    
    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password
        
    def set_username(self, username):
        self.username = username
        
    def set_email(self, email):
        self.email = email
        
    def set_password(self, password):
        self.password = password
        
    def login(self, usr, pwd) -> bool:
        if usr == self.username & pwd == self.password: 
            if usr == "" | pwd == "": 
                print("Create Login")
                return False
            else: 
                return True
        else: 
            return False
        
class Seller(User):

    def __init__(self, username="", email="", password=""):
        super().__init__(username, email, password)
        self.product_listings = {Product}
        self.sales = {Product}

    def add_product(self, product, quantity):
        self.product_listings[product] += quantity
    
    def remove_product(self, product, quantity):
        current_quantity = self.product_listings[product]
        self.product_listings[product] = current_quantity - quantity
        
    def add_sale(self, product, quantity): 
        self.sales[product] += quantity
        self.remove_product(product, quantity)
    
    def view_sales(self):
        print(self.sales)
    
class Buyer(User):
    
    def __init__(self, username="", email="", password=""):
        super().__init__(username, email, password)
        self.cart = Cart()
        self.order_history = {Product}
        self.balance = 0
        
    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)
        
    def remove_from_cart(self, product, quantity): 
        self.cart.remove_product(product, quantity)
        
    def deposit(self, amount):
        self.balance += amount
        
    def checkout(self): 
        if self.cart.total_price() < self.balance: 
            print("Insufficient Funds")
        else:
            # charge buyer 
            self.balance -= self.cart.total_price()
            
            # buy products
            for product in self.cart.products: 
                quantity = self.cart.products[product]
                product.buy(quantity)
                self.order_history[product] += quantity
            
            # empty cart    
            self.cart= Cart()
        
class Product: 
    
    def __init__(self, name, price, seller : Seller):
        self.name = name 
        self.price = price
        self.seller = seller
        self.sold = False
        
    def buy(self, quantity):
        self.sold = True
        self.seller.add_sale(self, quantity)
        
class Cart:
    
    def __init__(self):
        self.products = {Product}
        
    def add_product(self, product, quantity):
        self.products[product] = quantity
        
    def remove_product(self, product, quantity):
        current_quantity = self.products[product]
        self.products[product] = current_quantity - quantity
        
    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price * self.products[product]
        

        
    
        