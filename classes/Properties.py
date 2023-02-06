class Product:
    def __init__(self, price) -> None:
        self.price = price

    # Getter for property 'price'. Decorator automatically adds property to object
    @property
    def price(self):
        return self.__price

    # Setter for property 'price'.
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value


product = Product(10)
print(product.price)

product = Product(-10)
