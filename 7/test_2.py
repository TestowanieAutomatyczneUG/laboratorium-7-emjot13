import unittest


class Password:
    """
    >>> obj = Password()
    >>> obj.ValidPassword("osghosghg")
    False
    >>> obj.ValidPassword("AAAa1!!111")
    True
    >>> obj.ValidPassword("567Anccs!@#")
    True
    >>> obj.ValidPassword("!A7bc")
    False
    >>> obj.ValidPassword("AbAbAbAb<><>")
    False
    >>> obj.ValidPassword("MyPassLoL123!")
    True
    >>> obj.ValidPassword("")
    False
    >>> obj.ValidPassword(True)
    Traceback (most recent call last):
    ...
    ValueError: Password must be a string.
    >>> obj.ValidPassword(["dd", 55])
    Traceback (most recent call last):
    ...
    ValueError: Password must be a string.
    >>> obj.ValidPassword(gdfsdf)
    Traceback (most recent call last):
    ...
    NameError: name 'gdfsdf' is not defined
    """

    def ValidPassword(self, password):
        if type(password) is not str:
            raise ValueError("Password must be a string.")
        reqs = [False, False, False, False]
        if len(password) > 7:
            reqs[0] = True
        for char in password:
            if char.isupper():
                reqs[1] = True
            if char.isdigit():
                reqs[2] = True
            if char in ["@", "$", "!", "?", "_", "*", '&', "%"]:
                reqs[3] = True
        if False in reqs:
            return False
        return True


class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = Password()

    def test_positive_exclamation_mark(self):
        self.assertEqual(self.temp.ValidPassword("Abbbbfdbbbbb1!"), True)

    def test_positive_question_mark(self):
        self.assertEqual(self.temp.ValidPassword("Abbbbbdfbbbbb1!"), True)

    def test_positive_star_char(self):
        self.assertEqual(self.temp.ValidPassword("Abbbbbdfbbbbb1*"), True)

    def test_negative_not_long_enough(self):
        self.assertEqual(self.temp.ValidPassword("Abbb1!"), False)

    def test_negative_no_special_chars(self):
        self.assertEqual(self.temp.ValidPassword("AAAaaAAA345"), False)

    def test_negative_no_digits(self):
        self.assertEqual(self.temp.ValidPassword("aaaAAAAA!!!!"), False)

    def test_raise_value_error_float(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, 3.5)

    def test_raise_value_error_int(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, 8)

    def test_raise_value_error_list(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, [1, "g"])

    def test_raise_value_error_tuple(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, (1, "g"))

    def test_raise_value_error_none(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, None)

    def test_raise_value_error_bools(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, True)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    unittest.main()
