# Classe que representa um serviço de pagamento
class PaymentService:
    def process_payment(self, amount):
        print(f"Processando pagamento de {amount} reais.")

# Classe que representa um carrinho de compras
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
    
    def checkout(self, payment_service):
        total_amount = self.calculate_total()
        payment_service.process_payment(total_amount)
        print("Pagamento concluído. Obrigado por comprar!")

# Classe que representa um item de compra
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Uso das classes

# Criação de um serviço de pagamento
payment_service = PaymentService()

# Criação de um carrinho de compras
cart = ShoppingCart()

# Adição de itens ao carrinho
item1 = Item("Camiseta", 29.90)
item2 = Item("Calça", 79.90)

cart.add_item(item1)
cart.add_item(item2)

# Realização do checkout
cart.checkout(payment_service)
