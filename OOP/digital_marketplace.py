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
        if usr == self.username and pwd == self.password: 
            if usr == "" or pwd == "": 
                print("Create Login")
                return False
            else: 
                return True
        else: 
            return False
        
class Seller(User):

    def __init__(self, username="", email="", password=""):
        super().__init__(username, email, password)
        self.product_listings = {}
        self.sales = {}

    def add_product(self, product, quantity):
        self.product_listings[product] = self.product_listings.get(product, 0) + quantity

    
    def remove_product(self, product, quantity):
        current_quantity = self.product_listings[product]
        self.product_listings[product] = current_quantity - quantity
        
    def add_sale(self, product, quantity): 
        self.sales[product] += quantity
        self.remove_product(product, quantity)
    
    def view_sales(self):
        print(self.sales)
        
    def view_listings(self):
        print(self.product_listings)
    
class Buyer(User):
    
    def __init__(self, username="", email="", password=""):
        super().__init__(username, email, password)
        self.cart = Cart()
        self.order_history = {}
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
                self.order_history[product] = self.order_history.get(product, 0) + quantity

            # empty cart    
            self.cart= Cart()
        
    def view_cart(self):
        print(self.cart)
        
    def view_order_history(self):
        print(self.order_history)
        
class Product: 
    
    def __init__(self, name, price, seller : Seller):
        self.name = name 
        self.price = price
        self.seller = seller
        self.sold = False
    
    def __str__(self):
        return f"{self.seller.username}'s {self.name}: £{self.price}"
    
    def buy(self, quantity):
        self.sold = True
        self.seller.add_sale(self, quantity)
        
class Cart:
    
    def __init__(self):
        self.products = {}
    
    def __str__(self):
        return "\n".join(f"{p.name} x {q}" for p, q in self.products.items())

    
    def add_product(self, product, quantity):
        self.products[product] = quantity
        
    def remove_product(self, product, quantity):
        current_quantity = self.products[product]
        self.products[product] = current_quantity - quantity
        
    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price * self.products[product]
        return total

def main(): 
    
    seller = Seller(username="Seller")
    product = Product("Football", 10, seller)
    seller.add_product(product, 5)
    seller.view_listings()
    seller.view_sales()
    
    buyer = Buyer(username="Buyer")
    buyer.deposit(100)
    buyer.add_to_cart(product, 2)
    buyer.view_cart()
    buyer.checkout()
    buyer.view_order_history()
    

if __name__ == "__main__":
    main()
