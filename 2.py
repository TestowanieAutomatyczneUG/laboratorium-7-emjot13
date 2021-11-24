class Password:
    def ValidPassword(self, password):
        length, uppercase, special_char, number = False, False, False, False
        if len(password) > 7:
            length = True
        for char in password:
            if char.isupper():
                uppercase = True
            if char.isdigit():
                number = True
            if char in ["@", "$", "!", "?", "_"]:
                special_char = True