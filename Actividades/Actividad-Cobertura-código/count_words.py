class CountWords:
    def count(self, s: str) -> int:
        words = 0
        last = ' '
        string = s.lower() #cambiar a minuscula

        for char in string:
            if not char.isalpha() and (last == 's' or last == 'r'):
                words += 1
            last = char

        if last == 'r' or last == 's':
            words += 1 

        return words
