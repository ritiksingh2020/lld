from abc import ABC , abstractmethod
from typing import Dict

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, card_cvv: int, cardholder_name: str) -> None:
        self.card_number = card_number
        self.card_cvv =  card_cvv
        self.cardholder_name = cardholder_name

    def pay(self, amount:float):
        print(f"Payment done from creditcard ending with number {self.card_number[-4:]} and total amount {amount}")

class CashPayment(PaymentStrategy):
    def __init__(self, buyers_name: str) -> None:
        self.buyers_name = buyers_name

    def pay(self, amount: float):
        print(f"Amount paid by cash by payers {self.buyers_name} and total amount {amount}")

class UPIPayment(PaymentStrategy):
    def __init__(self,upi_id) -> None:
        self.upi_id = upi_id

    def pay(self, amount: float):
        print(f"paid by upi from upi id {self.upi_id} and total amount {amount}")

class Product:
    def __init__(self, name:str , price:float) -> None:
        self.name = name
        self.price = price
        self.quantity = 0

class Cart:
    def __init__(self) -> None:
        self.products:Dict[str,Product] = dict()

    def add_product(self, product:Product, quantity:int):
        name = product.name
        if name in self.products:
            self.products[name].quantity+=quantity
        else:
            product.quantity = quantity
            self.products[name] = product
    
    def remove_product(self, product:Product, quantity:int):
        name = product.name
        if name in self.products:
            if quantity >product.quantity:
                raise ValueError("quantity is more than the current quantity")
            self.products[name].quantity-=quantity
        else:
            raise ValueError("product not added to cart")
        
    def display_cart(self):
        for _,item in self.products.items():
            print(f"product name {item.name} with quantity {item.quantity}")

    def calculate_total(self):
        total_amount = sum(item.price*item.quantity for _,item in self.products.items())
        return total_amount

    def payment(self, paymentType:PaymentStrategy):
        amount = self.calculate_total()
        paymentType.pay(amount)

product1 = Product("paste", 10)
product2 = Product("maggie", 12)
cart = Cart()
cart.add_product(product1, 10)
cart.add_product(product2,20)
cart.calculate_total()
cart.display_cart()
creditCardPayment = CreditCardPayment("441535463364564736", 111, "ritiksingh")
cart.payment(creditCardPayment)