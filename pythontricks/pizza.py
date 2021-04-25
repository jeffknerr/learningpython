"""
4.8 class, static, and instance methods
Aprilt 25, 2021
J. Knerr
"""

# from Dan Bader's awesome Python Tricks book


class Pizza():
    """let's make some pizzas...."""
    num_pizzas_made = 0      # a class variable

    def __init__(self, ingredients):
        """instance method/constructor for pizza class"""
        self.__class__.num_pizzas_made += 1
        self.ingredients = ingredients

    def __repr__(self):
        """every class should at least have a repr"""
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        """factory class method to make moz/tomato pizzas"""
        return cls(['mozarella', 'tomatoes'])

    @classmethod
    def hawaiian(cls):
        """factory class method to make ham/pineapple pizzas"""
        return cls(['ham', 'pineapple'])


#####################################################


def main():
    """test code for class"""
    for _ in range(10):
        pi1 = Pizza("cheese")
        print(pi1, Pizza.num_pizzas_made)


if __name__ == "__main__":
    main()
