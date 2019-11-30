class Test(object):
    def __init__(self, number):
        self.number = number

    def multiply_by_2(self):
        return self.number*2

    class Test(object):
        """
        >>> a=Test(5)
        >>> a.multiply_by_2()
        10
        """

        def __init__(self, number):
            self.number = number

        def multiply_by_2(self):
            return self.number * 2

    if __name__ == "__main__":
        import doctest
        doctest.testmod()