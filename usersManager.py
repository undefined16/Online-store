class User:
    def __init__(self, userName, userId, bankAccountBalance):
        # Ініціалізація атрибутів користувача
        self.userName = userName
        self.userId = userId
        self.bankAccountBalance = bankAccountBalance
        self.cart = {}  # Кошик для продуктів

    def addFunds(self, amount):
        # Додавання коштів на рахунок
        self.bankAccountBalance += amount

    def viewDetails(self):
        # Перегляд деталей користувача
        print(f"ID: {self.userId}, Ім'я: {self.userName}, Баланс: {self.bankAccountBalance}")

    def addToCart(self, product, quantity):
        # Додавання продукту до кошика
        if quantity > product.quantity:
            print(f"Недостатньо продуктів на складі. Доступно: {product.quantity}")
            return
        
        if product.productId not in self.cart:
            self.cart[product.productId] = {'product': product, 'quantity': 0}
        
        self.cart[product.productId]['quantity'] += quantity
        product.quantity -= quantity  # Зменшення кількості продукту при додаванні до кошика

    def removeFromCart(self, productId):
        # Видалення продукту з кошика
        if productId in self.cart:
            item = self.cart[productId]
            item['product'].quantity += item['quantity']  # Повернення кількості на склад
            del self.cart[productId]

    def checkout(self):
        # Оформлення замовлення
        totalCost = sum(item['product'].price * item['quantity'] for item in self.cart.values())
        if totalCost > self.bankAccountBalance:
            print("Недостатньо коштів на рахунку.")
        else:
            self.bankAccountBalance -= totalCost
            self.cart.clear()  # Очищення кошика після оформлення
            print("Замовлення оформлено успішно.")


class UserManager:
    def __init__(self):
        # Ініціалізація словника користувачів
        self.users = {}

    def addUser(self, user):
        # Додавання користувача до словника
        self.users[user.userId] = user

    def updateUser(self, userId, userName=None, bankAccountBalance=None):
        # Оновлення користувача
        if userId in self.users:
            user = self.users[userId]
            if userName is not None:
                user.userName = userName
            if bankAccountBalance is not None:
                user.bankAccountBalance = bankAccountBalance
        else:
            print(f"Користувача з ID {userId} не знайдено.")

    def removeUser(self, userId):
        # Видалення користувача з словника
        if userId in self.users:
            del self.users[userId]
        else:
            print(f"Користувача з ID {userId} не знайдено.")

    def viewUsers(self):
        # Перегляд всіх користувачів
        if not self.users:
            print("Немає зареєстрованих користувачів.")
        else:
            for userId, user in self.users.items():
                print(f"ID: {userId}, Ім'я: {user.userName}, Баланс: {user.bankAccountBalance}")
