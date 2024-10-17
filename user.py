# Імпорт класу User з попереднього коду (якщо це окремий файл)
from your_module import User, UserManager

# Створення екземпляра менеджера користувачів
user_manager = UserManager()

# Створення нових користувачів
user1 = User("Олександр Іванов", 1, 100.00)
user2 = User("Марія Петрова", 2, 250.50)
user3 = User("Ігор Коваленко", 3, 175.75)
user4 = User("Катерина Сидорова", 4, 300.00)
user5 = User("Андрій Мельник", 5, 50.00)

# Додавання користувачів до менеджера
user_manager.addUser(user1)
user_manager.addUser(user2)
user_manager.addUser(user3)
user_manager.addUser(user4)
user_manager.addUser(user5)

# Перегляд усіх користувачів у системі
user_manager.viewUsers()
