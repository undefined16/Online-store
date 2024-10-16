import productsManager
from productsManager import Product, ProductManager

class Admin:
    def __init__(self, productManager):
        # Ініціалізація менеджера продуктів
        self.productManager = productManager

    def displayMenu(self):
        # Відображення меню
        print("\n--- Управління Онлайн Магазином ---")
        print("1. Додати продукт")
        print("2. Оновити продукт")
        print("3. Видалити продукт")
        print("4. Переглянути всі продукти")
        print("5. Вийти")

    def getUserInput(self, prompt, castType=str):
        # Отримання вводу користувача та переведення до потрібного типу, обробка помилок
        try:
            userInput = input(prompt)
            return castType(userInput) if userInput else None
        except ValueError:
            print(f"Невірне значення. Очікувалося {castType.__name__}.")
            return None

    def addProduct(self):
        # Додавання нового продукту
        name = input("Введіть назву продукту: ")
        price = self.getUserInput("Введіть ціну продукту: ", float)
        quantity = self.getUserInput("Введіть кількість продукту: ", int)
        productId = self.getUserInput("Введіть ID продукту: ", int)
        
        # Перевірка правильності введених даних
        if all([name, price, quantity, productId]):
            product = Product(name, price, quantity, productId)
            self.productManager.addProduct(product)
        else:
            print("Не вдалося додати продукт. Переконайтесь, що всі дані введені правильно.")

    def updateProduct(self):
        # Оновлення існуючого продукту
        productId = self.getUserInput("Введіть ID продукту для оновлення: ", int)
        if productId is not None:
            name = input("Введіть нову назву продукту (або натисніть Enter, щоб пропустити): ")
            price = self.getUserInput("Введіть нову ціну продукту (або натисніть Enter, щоб пропустити): ", float)
            quantity = self.getUserInput("Введіть нову кількість продукту (або натисніть Enter, щоб пропустити): ", int)
            
            # Передача даних для оновлення продукту
            self.productManager.updateProduct(productId, name, price, quantity)
        else:
            print("Невірний ID продукту.")

    def deleteProduct(self):
        # Видалення продукту
        productId = self.getUserInput("Введіть ID продукту для видалення: ", int)
        if productId is not None:
            self.productManager.deleteProduct(productId)
        else:
            print("Невірний ID продукту.")

    def viewProducts(self):
        # Перегляд всіх продуктів
        self.productManager.viewProducts()

    def run(self):
        # Запуск основного циклу програми
        actions = {
            '1': self.addProduct,
            '2': self.updateProduct,
            '3': self.deleteProduct,
            '4': self.viewProducts
        }

        while True:
            self.displayMenu()
            choice = self.getUserInput("Оберіть опцію (1-5): ")
            
            # Виконання відповідної дії на основі вибору користувача
            if choice in actions:
                actions[choice]()
            elif choice == '5':
                print("Вихід з системи.")
                break
            else:
                print("Невірний вибір, будь ласка, спробуйте ще раз.")

            print("\nЗавдання завершено. Повернення до меню.")
            
productManager = ProductManager()
Admin = Admin(productManager)
Admin.run()
