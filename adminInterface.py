import productsManager
import userManager
from productsManager import Product, ProductManager
from userManager import User, UserManager

class Admin:
    def __init__(self, productManager, userManager):
        # Ініціалізація менеджера продуктів та користувачів
        self.productManager = productManager
        self.userManager = userManager

    def displayMenu(self):
        # Відображення меню
        print("\n--- Управління Онлайн Магазином ---")
        print("1. Додати продукт")
        print("2. Оновити продукт")
        print("3. Видалити продукт")
        print("4. Переглянути всі продукти")
        print("5. Додати користувача")
        print("6. Оновити користувача")
        print("7. Видалити користувача")
        print("8. Переглянути всіх користувачів")
        print("9. Додати кошти користувачу")
        print("10. Переглянути історію замовлень користувача")
        print("11. Переглянути деталі користувача")
        print("12. Додати продукт до кошика користувача")
        print("13. Видалити продукт з кошика користувача")
        print("14. Оформити замовлення для користувача")
        print("15. Вийти")

    def getUserInput(self, prompt, castType=str):
        # Отримання вводу користувача та переведення до потрібного типу, обробка помилок
        while True:
            try:
                userInput = input(prompt)
                return castType(userInput) if userInput else None
            except ValueError:
                print(f"Невірне значення. Очікувалося {castType.__name__}.")

    def addProduct(self):
        # Додавання нового продукту
        try:
            name = input("Введіть назву продукту: ")
            price = self.getUserInput("Введіть ціну продукту: ", float)
            quantity = self.getUserInput("Введіть кількість продукту: ", int)
            productId = self.getUserInput("Введіть ID продукту: ", int)

            # Перевірка правильності введених даних
            if all([name, price is not None, quantity is not None, productId is not None]):
                product = Product(name, price, quantity, productId)
                self.productManager.addProduct(product)
                print("Продукт успішно додано.")
            else:
                print("Не вдалося додати продукт. Переконайтесь, що всі дані введені правильно.")
        except Exception as e:
            print(f"Виникла помилка при додаванні продукту: {e}")

    def updateProduct(self):
        # Оновлення існуючого продукту
        try:
            productId = self.getUserInput("Введіть ID продукту для оновлення: ", int)
            if productId is not None:
                name = input("Введіть нову назву продукту (або натисніть Enter, щоб пропустити): ")
                price = self.getUserInput("Введіть нову ціну продукту (або натисніть Enter, щоб пропустити): ", float)
                quantity = self.getUserInput("Введіть нову кількість продукту (або натисніть Enter, щоб пропустити): ", int)

                # Передача даних для оновлення продукту
                self.productManager.updateProduct(productId, name, price, quantity)
                print("Продукт успішно оновлено.")
            else:
                print("Невірний ID продукту.")
        except Exception as e:
            print(f"Виникла помилка при оновленні продукту: {e}")

    def deleteProduct(self):
        # Видалення продукту
        try:
            productId = self.getUserInput("Введіть ID продукту для видалення: ", int)
            if productId is not None:
                self.productManager.deleteProduct(productId)
                print("Продукт успішно видалено.")
            else:
                print("Невірний ID продукту.")
        except Exception as e:
            print(f"Виникла помилка при видаленні продукту: {e}")

    def viewProducts(self):
        # Перегляд всіх продуктів
        try:
            self.productManager.viewProducts()
        except Exception as e:
            print(f"Виникла помилка при перегляді продуктів: {e}")

    def addUser(self):
        # Додавання нового користувача
        try:
            userName = input("Введіть ім'я користувача: ")
            userId = self.getUserInput("Введіть ID користувача: ", int)
            bankAccountBalance = self.getUserInput("Введіть баланс користувача: ", float)

            # Перевірка правильності введених даних
            if all([userName, userId is not None, bankAccountBalance is not None]):
                user = User(userName, userId, bankAccountBalance)
                self.userManager.addUser(user)
                print("Користувача успішно додано.")
            else:
                print("Не вдалося додати користувача. Переконайтесь, що всі дані введені правильно.")
        except Exception as e:
            print(f"Виникла помилка при додаванні користувача: {e}")

    def updateUser(self):
        # Оновлення існуючого користувача
        try:
            userId = self.getUserInput("Введіть ID користувача для оновлення: ", int)
            if userId is not None:
                userName = input("Введіть нове ім'я користувача (або натисніть Enter, щоб пропустити): ")
                bankAccountBalance = self.getUserInput("Введіть новий баланс користувача (або натисніть Enter, щоб пропустити): ", float)

                # Передача даних для оновлення користувача
                self.userManager.updateUser(userId, userName, bankAccountBalance)
                print("Користувача успішно оновлено.")
            else:
                print("Невірний ID користувача.")
        except Exception as e:
            print(f"Виникла помилка при оновленні користувача: {e}")

    def deleteUser(self):
        # Видалення користувача
        try:
            userId = self.getUserInput("Введіть ID користувача для видалення: ", int)
            if userId is not None:
                self.userManager.removeUser(userId)
                print("Користувача успішно видалено.")
            else:
                print("Невірний ID користувача.")
        except Exception as e:
            print(f"Виникла помилка при видаленні користувача: {e}")

    def viewUsers(self):
        # Перегляд всіх користувачів
        try:
            self.userManager.viewUsers()
        except Exception as e:
            print(f"Виникла помилка при перегляді користувачів: {e}")

    def addFundsToUser(self):
        # Додавання коштів до користувача
        try:
            userId = self.getUserInput("Введіть ID користувача, якому потрібно додати кошти: ", int)
            amount = self.getUserInput("Введіть суму для поповнення: ", float)

            # Перевірка наявності користувача
            if userId in self.userManager.userList:
                user = self.userManager.userList[userId]
                user.addFunds(amount)
                print("Кошти успішно додано.")
            else:
                print(f"Користувача з ID {userId} не знайдено.")
        except Exception as e:
            print(f"Виникла помилка при додаванні коштів: {e}")

    def viewUserOrderHistory(self):
        # Перегляд історії замовлень конкретного користувача
        try:
            userId = self.getUserInput("Введіть ID користувача для перегляду історії замовлень: ", int)

            # Перевірка наявності користувача
            if userId in self.userManager.userList:
                user = self.userManager.userList[userId]
                user.viewOrderHistory()
            else:
                print(f"Користувача з ID {userId} не знайдено.")
        except Exception as e:
            print(f"Виникла помилка при перегляді історії замовлень: {e}")

    def viewUserDetails(self):
        # Перегляд детальної інформації про користувача
        try:
            userId = self.getUserInput("Введіть ID користувача для перегляду деталей: ", int)

            # Перевірка наявності користувача
            if userId in self.userManager.userList:
                user = self.userManager.userList[userId]
                print(f"ID: {user.userId}, Name: {user.userName}, Balance: {user.bankAccountBalance}$")
                print("Cart:")
                user.viewCart()
                print("Order History:")
                user.viewOrderHistory()
            else:
                print(f"Користувача з ID {userId} не знайдено.")
        except Exception as e:
            print(f"Виникла помилка при перегляді деталей користувача: {e}")

    def addProductToUserCart(self):
        # Додавання продукту до кошика конкретного користувача
        try:
            userId = self.getUserInput("Введіть ID користувача для додавання продукту до кошика: ", int)
            productId = self.getUserInput("Введіть ID продукту для додавання: ", int)
            quantity = self.getUserInput("Введіть кількість: ", int)

            if userId in self.userManager.userList:
                user = self.userManager.userList[userId]
                product = self.productManager.getProductById(productId)  # Fetch product by ID
                if product:
                    user.add(product, quantity)
                else:
                    print(f"Продукт з ID {productId} не знайдено.")
            else:
                print(f"Користувача з ID {userId} не знайдено.")
        except Exception as e:
            print(f"Виникла помилка при додаванні продукту до кошика: {e}")

    def removeProductFromUserCart(self):
        # Видалення продукту з кошика конкретного користувача
        try:
            userId = self.getUserInput("Введіть ID користувача для видалення продукту з кошика: ", int)
            productId = self.getUserInput("Введіть ID продукту для видалення: ", int)

            if userId in self.userManager.userList:
                user = self.userManager.userList[userId]
                product = self.productManager.getProductById(productId)  # Fetch product by ID
                if product:
                    user.removeFromCart(product)
                else:
                    print(f"Продукт з ID {productId} не знайдено.")
            else:
                print(f"Користувача з ID {userId} не знайдено.")
        except Exception as e:
            print(f"Виникла помилка при видаленні продукту з кошика: {e}")

    def placeOrderForUser(self):
        # Оформлення замовлення для конкретного користувача
        try:
            userId = self.getUserInput("Введіть ID користувача для оформлення замовлення: ", int)
            paymentMethod = input("Введіть метод оплати (кредитна картка або PayPal): ")

            if userId in self.userManager.userList:
                user = self.userManager.userList[userId]
                user.placeOrder(paymentMethod)
            else:
                print(f"Користувача з ID {userId} не знайдено.")
        except Exception as e:
            print(f"Виникла помилка при оформленні замовлення: {e}")

    def run(self):
        # Головний цикл для роботи адміністратора
        while True:
            self.displayMenu()
            choice = self.getUserInput("Виберіть опцію: ", int)

            if choice == 1:
                self.addProduct()
            elif choice == 2:
                self.updateProduct()
            elif choice == 3:
                self.deleteProduct()
            elif choice == 4:
                self.viewProducts()
            elif choice == 5:
                self.addUser()
            elif choice == 6:
                self.updateUser()
            elif choice == 7:
                self.deleteUser()
            elif choice == 8:
                self.viewUsers()
            elif choice == 9:
                self.addFundsToUser()
            elif choice == 10:
                self.viewUserOrderHistory()
            elif choice == 11:
                self.viewUserDetails()
            elif choice == 12:
                self.addProductToUserCart()
            elif choice == 13:
                self.removeProductFromUserCart()
            elif choice == 14:
                self.placeOrderForUser()
            elif choice == 15:
                print("Вихід з програми.")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

# Ініціалізація класів для управління продуктами та користувачами
productManager = ProductManager()
userManager = UserManager()
admin = Admin(productManager, userManager)

# Запуск програми
admin.run()
