from usersManager import User, UserManager

userManager = UserManager()

def addUsers():
    # Creating users without the trailing comma
    user1 = User("Олександр Іванов", 1, 100.00)
    user2 = User("Марія Петрова", 2, 250.50)
    user3 = User("Ігор Коваленко", 3, 175.75)
    user4 = User("Катерина Сидорова", 4, 300.00)
    user5 = User("Андрій Мельник", 5, 50.00)
    
    # Adding users to the userManager instance
    userManager.addUser(user1)
    userManager.addUser(user2)
    userManager.addUser(user3)
    userManager.addUser(user4)
    userManager.addUser(user5)

# Call the addUsers function