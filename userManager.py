class User:
    def __init__(self, userName):
        self.userName = str(userName)
        self.cart = []
        self.order_history = []

    def add(self, product, quantity):
        try:
            if quantity <= 0:
                print("Кількість товару повинна бути більше нуля")
                return
            
            self.cart.append((product, quantity))
            print(f"{quantity} одиниць {product.productName} додано до кошика")
        except Exception as e:
            print(f"Помилка при додаванні товару до кошика: {e}")

    def removeFromCart(self, product):
        try:
            for item in self.cart:
                if item[0].productId == product.productId:
                    self.cart.remove(item)
                    print(f"{product.productName} видалено з кошика")
                    return
            
            print(f"{product.productName} не знайдено в кошику")
        except Exception as e:
            print(f"Помилка при видаленні товару з кошика: {e}")

    def placeOrder(self, paymentMethod):
        try:
            total = sum(item[0].productPrice * item[1] for item in self.cart)

            if paymentMethod in ["кредитна картка", "paypal"]:
                print(f"Оплата {total}$ через {paymentMethod}")
            else:
                raise ValueError("Неправильний спосіб оплати")

            for item in self.cart:
                product, quantity = item
                if product.productQuantity >= quantity:
                    product.productQuantity -= quantity
                    self.order_history.append(item)
                    print(f"Замовлення на {quantity} {product.productName} оформлено")
                else:
                    print(f"Недостатня кількість {product.productName}. Доступно: {product.productQuantity}, запитувано: {quantity}")
                    raise ValueError("Недостатня кількість товару.")

            self.cart.clear()
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Помилка при оформленні замовлення: {e}")

    def viewCart(self):
        try:
            if not self.cart:
                print("Кошик порожній.")
            else:
                print("Ваш кошик:")
                for item in self.cart:
                    product, quantity = item
                    print(f"{quantity} одиниць {product.productName} по ціні {product.productPrice}$")
        except Exception as e:
            print(f"Помилка при перегляді кошика: {e}")

    def history(self):
        try:
            if not self.order_history:
                print("Історія замовлень порожня.")
            else:
                print("Історія замовлень:")
                for item in self.order_history:
                    product, quantity = item
                    print(f"{quantity} одиниць {product.productName}")
        except Exception as e:
            print(f"Помилка при перегляді історії замовлень: {e}")