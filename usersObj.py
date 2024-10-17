from usersManager import User

users = [
    User("Олександр Іванов", 1, 100.00),
    User("Марія Петрова", 2, 250.50),
    User("Ігор Коваленко", 3, 175.75),
    User("Катерина Сидорова", 4, 300.00),
    User("Андрій Мельник", 5, 50.00)
]

# Перегляд інформації про користувачів та їх кошики
for user in users:
    print(f"Ім'я: {user.userName}, ID: {user.userId}, Баланс: {user.bankAccountBalance}$, Кошик: {user.cart}")
