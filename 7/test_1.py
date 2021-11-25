
def main(): # pragma: no cover

    def isPangram(word):
        """
        >>> isPangram("The five boxing wizards jump quickly")
        True
        >>> isPangram("Sympathizing would fix Quaker objectives")
        True
        >>> isPangram("Every day I'm shuffling")
        False
        >>> isPangram(10)
        Traceback (most recent call last):
        ...
        ValueError: incorrect data type
        >>> isPangram(gdfsdf)
        Traceback (most recent call last):
        ...
        NameError: name 'gdfsdf' is not defined
        >>> isPangram(['S', 'y', 'm', 'p', 'a', 't', 'h', 'i', 'z', 'i', 'n', 'g', ' ', 'w', 'o', 'u', 'l', 'd', ' ', 'f', 'i', 'x', ' ', 'Q', 'u', 'a', 'k', 'e', 'r', ' ', 'o', 'b', 'j', 'e', 'c', 't', 'i', 'v', 'e', 's'])
        Traceback (most recent call last):
        ...
        ValueError: incorrect data type
        """

        if type(word) is not str:
            raise ValueError("incorrect data type")
        all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                       "u", "v", "w", "x", "y", "z"]
        for letter in all_letters:
            if letter not in word.lower():
                return False
        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()