class vowels:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    @staticmethod
    def mapper(ch):
        mapper = {"A", "a",
                  "E", "e",
                  "I", "i",
                  "O", "o",
                  "Y", "y",
                  "U", "u"}
        if ch in mapper:
            return ch

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        ch = self.text[self.index]
        self.index += 1
        if not self.mapper(ch):
            return self.__next__()
        return ch


my_string = vowels('AbcedifuyyYOo')
for char in my_string:
    print(char)
