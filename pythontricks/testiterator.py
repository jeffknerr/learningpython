"""
test out a simple iterator class
from Dan Bader "Python Tricks" book pg 230

J. Knerr
28Apr2021
"""


class Repeater:
    """repeat until max..."""

    def __init__(self, value, max_repeats):
        """constructor for Repeater class"""
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        """iter method for Repeater class"""
        return self

    def __next__(self):
        """get next item"""
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


def main():
    """test code for Repeater class"""
    n = 5
    rep1 = Repeater("hello", n)
    for item in rep1:
        print(item, rep1.count)


if __name__ == "__main__":
    main()
