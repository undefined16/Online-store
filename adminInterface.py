from productsManager import ProductManager, Product
from usersManager import UserManager, User

class Admin:
    def __init__(self):
        # Ініціалізація менеджерів продуктів і користувачів
        self.productManager = ProductManager()
        self.userManager = UserManager()

    def displayMenu(self):
        # Відображення меню для користувача
        print("\n=== Меню Керування Магазином ===")
        print("1. Додати продукт")
        print("2. Оновити продукт")
        print("3. Видалити продукт")
        print("4. Переглянути всі продукти")
        print("5. Додати користувача")
        print("6. Оновити користувача")
        print("7. Видалити користувача")
        print("8. Переглянути всіх користувачів")
        print("9. Додати продукт до кошика")
        print("10. Видалити продукт з кошика")
        print("11. Оформити замовлення")
        print("12. Додати кошти користувачу")
        print("0. Вийти")

    def run(self):
        # Запуск менеджера магазину з введенням користувача та обробкою виключень
        while True:
            self.displayMenu()  # Відображення меню
            choice = input("Введіть свій вибір: ")

            try:
                if choice == '1':
                    # Додавання продукту
                    name = input("Введіть назву продукту: ")
                    price = self.getValidFloat("Введіть ціну продукту: ")
                    quantity = self.getValidInt("Введіть кількість продукту: ")
                    productId = input("Введіть ID продукту: ")
                    self.addProduct(name, price, quantity, productId)

                elif choice == '2':
                    # Оновлення продукту
                    productId = input("Введіть ID продукту для оновлення: ")
                    name = input("Введіть нову назву (або залиште порожнім): ")
                    price = self.getOptionalFloat("Введіть нову ціну (або залиште порожнім): ")
                    quantity = self.getOptionalInt("Введіть нову кількість (або залиште порожнім): ")
                    self.updateProduct(productId, name or None, price, quantity)

                elif choice == '3':
                    # Видалення продукту
                    productId = input("Введіть ID продукту для видалення: ")
                    self.deleteProduct(productId)

                elif choice == '4':
                    # Перегляд усіх продуктів
                    self.viewProducts()

                elif choice == '5':
                    # Додавання користувача
                    userName = input("Введіть ім'я користувача: ")
                    userId = input("Введіть ID користувача: ")
                    bankAccountBalance = self.getValidFloat("Введіть баланс банківського рахунку: ")
                    self.addUser(userName, userId, bankAccountBalance)

                elif choice == '6':
                    # Оновлення користувача
                    userId = input("Введіть ID користувача для оновлення: ")
                    userName = input("Введіть нове ім'я (або залиште порожнім): ")
                    bankAccountBalance = self.getOptionalFloat("Введіть новий баланс (або залиште порожнім): ")
                    self.updateUser(userId, userName or None, bankAccountBalance)

                elif choice == '7':
                    # Видалення користувача
                    userId = input("Введіть ID користувача для видалення: ")
                    self.removeUser(userId)

                elif choice == '8':
                    # Перегляд усіх користувачів
                    self.viewUsers()

                elif choice == '9':
                    # Додавання продукту до кошика
                    userId = input("Введіть ID користувача: ")
                    productId = input("Введіть ID продукту: ")
                    quantity = self.getValidInt("Введіть кількість для додавання: ")
                    self.addProductToCart(userId, productId, quantity)

                elif choice == '10':
                    # Видалення продукту з кошика
                    userId = input("Введіть ID користувача: ")
                    productId = input("Введіть ID продукту: ")
                    self.removeProductFromCart(userId, productId)

                elif choice == '11':
                    # Оформлення замовлення
                    userId = input("Введіть ID користувача: ")
                    self.checkoutUser(userId)

                elif choice == '12':
                    # Додавання коштів користувачу
                    userId = input("Введіть ID користувача: ")
                    amount = self.getValidFloat("Введіть суму для додавання: ")
                    self.addFundsToUser(userId, amount)

                elif choice == '0':
                    # Вихід з програми
                    print("Вихід...")
                    break

                else:
                    print("Невірний вибір. Спробуйте ще раз.")

            except Exception as e:
                print(f"Сталася помилка: {e}")

    def getValidFloat(self, prompt):
        # Отримання дійсного значення float
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Невірний ввід. Введіть дійсне число.")

    def getValidInt(self, prompt):
        # Отримання дійсного значення int
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Невірний ввід. Введіть дійсне ціле число.")

    def getOptionalFloat(self, prompt):
        # Отримання дійсного значення float або None, якщо порожнє
        value = input(prompt)
        if value == "":
            return None
        try:
            return float(value)
        except ValueError:
            print("Невірний ввід. Повертається None.")
            return None

    def getOptionalInt(self, prompt):
        # Отримання дійсного значення int або None, якщо порожнє
        value = input(prompt)
        if value == "":
            return None
        try:
            return int(value)
        except ValueError:
            print("Невірний ввід. Повертається None.")
            return None

    # Методи ProductManager
    def addProduct(self, name, price, quantity, productId):
        # Додавання нового продукту
        product = Product(name, price, quantity, productId)
        self.productManager.addProduct(product)

    def updateProduct(self, productId, name=None, price=None, quantity=None):
        # Оновлення деталей продукту
        self.productManager.updateProduct(productId, name, price, quantity)

    def deleteProduct(self, productId):
        # Видалення продукту
        self.productManager.deleteProduct(productId)

    def viewProducts(self):
        # Перегляд усіх продуктів
        self.productManager.viewProducts()

    def getProductById(self, productId):
        # Отримання продукту за ID
        return self.productManager.getProductById(productId)

    # Методи UserManager
    def addUser(self, userName, userId, bankAccountBalance):
        # Додавання нового користувача
        user = User(userName, userId, bankAccountBalance)
        self.userManager.addUser(user)

    def updateUser(self, userId, userName=None, bankAccountBalance=None):
        # Оновлення деталей користувача
        self.userManager.updateUser(userId, userName, bankAccountBalance)

    def removeUser(self, userId):
        # Видалення користувача
        self.userManager.removeUser(userId)

    def viewUsers(self):
        # Перегляд усіх користувачів
        self.userManager.viewUsers()

    def getUserById(self, userId):
        # Отримання користувача за ID
        return self.userManager.users.get(userId, None)

    # Методи для роботи з кошиком і транзакціями
    def addProductToCart(self, userId, productId, quantity):
        # Додавання продукту до кошика користувача
        user = self.getUserById(userId)
        product = self.getProductById(productId)
        if user and product:
            user.addToCart(product, quantity)

    def removeProductFromCart(self, userId, productId):
        # Видалення продукту з кошика користувача
        user = self.getUserById(userId)
        if user:
            user.removeFromCart(productId)

    def checkoutUser(self, userId):
        # Оформлення замовлення користувача
        user = self.getUserById(userId)
        if user:
            user.checkout()

    def addFundsToUser(self, userId, amount):
        # Додавання коштів на рахунок користувача
        user = self.getUserById(userId)
        if user:
            user.addFunds(amount)