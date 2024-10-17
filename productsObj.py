from productsManager import Product,ProductManager
productManager = ProductManager()

product1 = Product("Яблука", 2.99, 50, 101)
product2 = Product("Банани", 1.99, 30, 102)
product3 = Product("Апельсини", 3.49, 20, 103)
product4 = Product("Груші", 2.49, 40, 104)
product5 = Product("Ківі", 4.99, 25, 105)
productManager.addProduct(product1)
productManager.addProduct(product2)
productManager.addProduct(product3)
productManager.addProduct(product4)
productManager.addProduct(product5)

productManager.viewProducts()
