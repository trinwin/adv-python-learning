# ----------------------------------------------------------------------
# Name:    homework6
# Purpose: Practice working with Python class
#
# Author(s): Mandeep Pabla and Trinh Nguyen
# ----------------------------------------------------------------------


class Product:
    """
    Represent a Product

    Arguments:
    description (string): description of product
    list_price (float): price of product

    Attributes:
    description (string): description of product
    list_price (float): price of product
    stock (int): number of items in stock
    sales (list): a list of actual sale prices
    reviews (list of tuples): a list of user reviews. Each review
    is a tuple containing the text of the review and the number
    of stars given by the reviewer.
    id (string): product id consists of category and serial number

    """
    # class variable
    category = 'GN'
    next_serial_number = 1

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.stock = 0
        self.sales = []
        self.reviews = []  # list of tuples
        self.id = self.generate_product_id()

    def restock(self, quantity):
        """
        Add new stock of product
        :param quantity: new stock number
        :return: None
        """
        self.stock += quantity

    def review(self, stars, text):
        """
        Add new review to review list
        :param stars: number of stars given in review
        :param text: review comment
        :return: None
        """
        self.reviews.append(tuple([text, stars]))

    def sell(self, quantity, sale_price):
        """
        Add new sale
        :param quantity: number of product sold
        :param sale_price: price it was sold at
        :return: None
        """
        sale_list = [sale_price for sale_num in range(quantity)
                     if sale_num < self.stock]

        if quantity > self.stock:
            self.stock = 0
        else:
            self.stock -= quantity

        self.sales.extend(sale_list)

    @classmethod
    def generate_product_id(cls):
        """
        Generate product id with product category and serial number
        :return (string): product id
        """
        product_id = f'{cls.category}{cls.next_serial_number:06}'
        cls.next_serial_number += 1
        return product_id

    def __str__(self):
        return f'{self.description}\n' \
               f'Product ID: {self.id}\n' \
               f'List price: ${self.list_price:,.2f}\n' \
               f'Available in stock: {self.stock}'

    def __add__(self, other):
        return Bundle(self, other)

    @property
    def lowest_price(self):
        """
        :return (int): lowest price out of all the sales
        """
        if not self.sales:
            return None
        return min(self.sales)

    @property
    def average_rating(self):
        """
        :return (int): Average star's rating of product
        """
        if not self.reviews:
            return None
        ratings = [stars[1] for stars in self.reviews]
        return sum(ratings) / len(ratings)


class VideoGame(Product):
    """
    Represent a Video Game Product
    Inherits from: Product

    Arguments:
    description (string): description of product
    list_price (float): price of product

    Attributes:
    description (string): description of product
    list_price (float): price of product
    stock (int): number of items in stock
    sales (list): a list of actual sale prices
    reviews (list of tuples): a list of user reviews. Each review
    is a tuple containing the text of the review and the number
    of stars given by the reviewer.
    id (string): product id consists of category and serial number

    """
    # class variable
    category = 'VG'
    next_serial_number = 1


class Book(Product):
    """
    Represent a book product with author's name and numbers of pages
    Inherits from: Product

    Arguments:
    author (string): the author's name
    pages (int): the book's number of pages
    description (string): description of product
    list_price (float): price of product

    Attributes:
    author (string): the author's name
    pages (int): the book's number of pages
    description (string): description of product
    list_price (float): price of product
    stock (int): number of items in stock
    sales (list): a list of actual sale prices
    reviews (list of tuples): a list of user reviews. Each review
    is a tuple containing the text of the review and the number
    of stars given by the reviewer.
    id (string): product id consists of category and serial number
    """
    # class variables
    category = 'BK'
    next_serial_number = 1

    def __init__(self, description, author, pages, list_price):
        self.author = author
        self.pages = pages
        super().__init__(description, list_price)

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages


class Bundle(Product):
    """
    Represent a Bundle of Products
    Inherits from: Product

    Arguments:
    description (string): description of product
    list_price (float): price of product

    Attributes:
    description (string): description of product
    list_price (float): price of product
    stock (int): number of items in stock
    sales (list): a list of actual sale prices
    reviews (list of tuples): a list of user reviews. Each review
    is a tuple containing the text of the review and the number
    of stars given by the reviewer.
    id (string): product id consists of category and serial number

    """
    # class variables
    category = 'BL'
    next_serial_number = 1
    bundle_discount = 20

    def __init__(self, p1, p2, *products):
        """
        Initialize Bundle with 2 or more Products
        :param p1: First Product of Bundle
        :param p2: Second Product of Bundle
        :param products: More Products of Bundle
        """
        self.description = f'{p1.description} & {p2.description}'
        total = p1.list_price + p2.list_price
        for product in products:
            self.description = f'{self.description} & {product.description}'
            total += product.list_price
        self.list_price = total - (self.bundle_discount / 100 * total)
        super().__init__(self.description, self.list_price)

    # What is the product id corresponding to the best_bundle? 
    # Answer: product id of best_bundle is BL000006
    # Why do you think that is the case?
    # Answer: We call __add__ function 3 times and create 3 Bundle objects
    # when we call "best_bundle = sunglasses + headphones + book1 + mario"
    # Bundle id = BL000004 has sunglasses + headphones
    # Bundle id = BL000005 has (sunglasses + headphones) + book1
    # Bundle id = BL000006 has (sunglasses + headphones + book1) + mario
