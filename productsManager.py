class Product:
    def __init__(self, productName, productPrice, productQuantity, productId):
        # Ініціалізація продукту з ім'ям, ціною, кількістю та ID.
        try:
            self.productName = str(productName)  # Переконання, що productName є рядком
            self.productPrice = float(productPrice)  # Переконання, що productPrice є числом з плаваючою комою
            self.productQuantity = int(productQuantity)  # Переконання, що productQuantity є цілим числом
            self.productId = int(productId)  # Переконання, що productId є цілим числом
        except ValueError as e:
            print(f"Помилка ініціалізації продукту: {e}")

    def __str__(self):
        # Представлення продукту у рядковому вигляді.
        return f"ID: {self.productId}, Ім'я: {self.productName}, Ціна: ${self.productPrice}, Кількість: {self.productQuantity}"


class Admin:
    def __init__(self):
        # Ініціалізація пустого словника для зберігання продуктів.
        self.productList = {}

    def addProduct(self, product):
        # Додавання нового продукту до системи.
        try:
            if product.productId in self.productList:
                print(f"Продукт з ID {product.productId} вже існує.")
            else:
                self.productList[product.productId] = product
                print(f"Продукт {product.productName} додано успішно!")
        except AttributeError:
            print("Неправильний продукт. Переконання, що об'єкт продукту має дійсні атрибути.")
        except Exception as e:
            print(f"Помилка при додаванні продукту: {e}")

    def updateProduct(self, productId, productName=None, productPrice=None, productQuantity=None):
        # Оновлення інформації про продукт.
        try:
            if productId in self.productList:
                product = self.productList[productId]
                if productName:
                    product.productName = str(productName)  # Переконання, що ім'я є рядком
                if productPrice:
                    product.productPrice = float(productPrice)  # Переконання, що ціна є числом з плаваючою комою
                if productQuantity:
                    product.productQuantity = int(productQuantity)  # Переконання, що кількість є цілим числом
                print(f"Продукт {productId} успішно оновлено!")
            else:
                print(f"Продукт з ID {productId} не знайдено.")
        except ValueError as e:
            print(f"Неправильне значення для оновлення продукту: {e}")
        except KeyError:
            print(f"Продукт з ID {productId} не знайдено.")
        except Exception as e:
            print(f"Помилка при оновленні продукту: {e}")

    def deleteProduct(self, productId):
        # Видалення продукту із системи.
        try:
            if productId in self.productList:
                del self.productList[productId]
                print(f"Продукт {productId} успішно видалено!")
            else:
                print(f"Продукт з ID {productId} не знайдено.")
        except KeyError:
            print(f"Продукт з ID {productId} не знайдено.")
        except Exception as e:
            print(f"Помилка при видаленні продукту: {e}")

    def viewProducts(self):
        # Перегляд усіх продуктів у системі.
        try:
            if not self.productList:
                print("Продуктів немає.")
            else:
                for product in self.productList.values():
                    print(product)
        except Exception as e:
            print(f"Помилка при перегляді продуктів: {e}")