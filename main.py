from adminInterface import Admin

import usersObj
import productsObj
productsObj.addProducts()
usersObj.addUsers()

admin = Admin()
admin.run()