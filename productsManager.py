class Product:
    def __init__(self, name, price, quantity, productId):
        # Ініціалізація атрибутів продукту
        self.name = name
        self.price = price
        self.quantity = quantity
        self.productId = productId


class ProductManager:
    def __init__(self):
        # Ініціалізація словника продуктів
        self.products = {}

    def addProduct(self, product):
        # Додавання продукту до словника
        self.products[product.productId] = product

    def updateProduct(self, productId, name=None, price=None, quantity=None):
        # Оновлення продукту
        if productId in self.products:
            product = self.products[productId]
            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if quantity is not None:
                product.quantity = quantity
        else:
            print(f"Продукта з ID {productId} не знайдено.")

    def deleteProduct(self, productId):
        # Видалення продукту з словника
        if productId in self.products:
            del self.products[productId]
        else:
            print(f"Продукта з ID {productId} не знайдено.")

    def viewProducts(self):
        # Перегляд всіх продуктів
        if not self.products:
            print("Немає доступних продуктів.")
        else:
            for productId, product in self.products.items():
                print(f"ID: {productId}, Назва: {product.name}, Ціна: {product.price}, Кількість: {product.quantity}")

    def getProductById(self, productId):
        # Отримання продукту за ID
        return self.products.get(productId, None)