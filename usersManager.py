import productsManager
from productsManager import Product, ProductManager

class User:
    def __init__(self, userName, userId, bankAccountBalance):
        """
        Ініціалізуємо користувача з іменем, унікальним ID та балансом банківського рахунку.
        """
        try:
            self.userName = str(userName)  # Зберігаємо ім'я користувача
            self.userId = int(userId)  # Зберігаємо унікальний ID користувача
            self.cart = []  # Ініціалізуємо порожній кошик для покупок
            self.orderHistory = []  # Ініціалізуємо порожню історію замовлень
            self.bankAccountBalance = float(bankAccountBalance)  # Ініціалізуємо баланс банківського рахунку користувача
        except ValueError as e:
            print(f"Помилка під час ініціалізації користувача: {e}")

    def add(self, product, quantity):
        """Додаємо товар до кошика користувача."""
        if quantity <= 0:
            print("Кількість повинна бути більшою за нуль.")
            return
        
        self.cart.append((product, quantity))  # Додаємо товар до кошика
        print(f"{quantity} одиниць {product.productName} додано до кошика")

    def removeFromCart(self, product):
        """Видаляємо товар з кошика користувача."""
        for item in self.cart:
            if item[0].productId == product.productId:
                self.cart.remove(item)  # Видаляємо товар з кошика
                print(f"{product.productName} видалено з кошика")
                return
        
        print(f"{product.productName} не знайдено в кошику")

    def placeOrder(self, paymentMethod):
        """Оформлюємо замовлення."""
        total = sum(item[0].productPrice * item[1] for item in self.cart)  # Розраховуємо загальну вартість

        if total > self.bankAccountBalance:
            print("Недостатньо коштів для оформлення замовлення.")
            return

        if paymentMethod not in ["credit card", "paypal"]:
            print("Неправильний метод оплати.")
            return

        print(f"Оплата {total}$ через {paymentMethod}")
        self.bankAccountBalance -= total  # Віднімаємо суму з банківського рахунку

        for product, quantity in self.cart:
            if product.productQuantity >= quantity:
                product.productQuantity -= quantity  # Зменшуємо кількість товару на складі
                self.orderHistory.append((product, quantity))  # Додаємо замовлення в історію
                print(f"Замовлення на {quantity} одиниць {product.productName} оформлено.")
            else:
                print(f"Недостатньо товару {product.productName}. Доступно: {product.productQuantity}, запитано: {quantity}")

        # Очищаємо кошик після оформлення замовлення
        self.cart.clear()

    def viewCart(self):
        """Переглядаємо поточні товари у кошику користувача."""
        if not self.cart:
            print("Кошик порожній.")
            return

        print("Ваш кошик:")
        for product, quantity in self.cart:
            print(f"{quantity} одиниць {product.productName} за {product.productPrice}$ кожен")

    def viewOrderHistory(self):
        """Переглядаємо історію замовлень користувача."""
        if not self.orderHistory:
            print("Історія замовлень порожня.")
            return

        print("Історія замовлень:")
        for product, quantity in self.orderHistory:
            print(f"{quantity} одиниць {product.productName}")

    def addFunds(self, amount):
        """Додаємо кошти на банківський рахунок користувача."""
        if amount <= 0:
            print("Сума поповнення повинна бути більшою за нуль.")
            return
        
        self.bankAccountBalance += amount  # Додаємо кошти до балансу
        print(f"Баланс поповнено на {amount}$. Поточний баланс: {self.bankAccountBalance}$")


class UserManager:
    def __init__(self):
        """Ініціалізуємо порожній словник для зберігання користувачів."""
        self.userList = {}  # Ініціалізуємо словник для зберігання користувачів

    def addUser(self, user):
        """Додаємо нового користувача до системи."""
        if user.userId in self.userList:
            print(f"Користувач з ID {user.userId} вже існує.")
            return
        
        self.userList[user.userId] = user  # Додаємо користувача до списку
        print(f"Користувач {user.userName} успішно доданий!")

    def removeUser(self, userId):
        """Видаляємо користувача із системи."""
        if userId in self.userList:
            del self.userList[userId]  # Видаляємо користувача зі списку
            print(f"Користувач {userId} успішно видалений!")
        else:
            print(f"Користувача з ID {userId} не знайдено.")

    def viewUsers(self):
        """Переглядаємо всіх користувачів у системі."""
        if not self.userList:
            print("Користувачів не знайдено.")
            return

        print("Список користувачів:")
        for user in self.userList.values():
            print(f"ID: {user.userId}, Ім'я: {user.userName}, Баланс: {user.bankAccountBalance}$")