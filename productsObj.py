from productsManager import Product, ProductManager

# Ensure productManager is an instance of ProductManager
productManager = ProductManager()

def addProducts():
    # Adding products
    product1 = Product("Яблука", 2.99, 50, 101)
    product2 = Product("Банани", 1.99, 30, 102)
    product3 = Product("Апельсини", 3.49, 20, 103)
    
    productManager.addProduct(product1)
    productManager.addProduct(product2)
    productManager.addProduct(product3)

# Call the function to add products

