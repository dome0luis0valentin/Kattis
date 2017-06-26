import sys
class Word:
    """
    A class that contains words with extra counter field
    """
    def __init__(self, word, c=1):
        self.word = word
        self.count = c
        self.mk = True

    def inc(self,c=1):
        self.count += c
    def mark(self):
        self.mk = False
    def __eq__(self,other):
        """
        Need this to use == operator
        """
        if type(other)==type(""):
            return self.word == other
        return self.word == other.word

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        """
        Need this for sets
        """
        return self.word.__hash__()

    def __gt__(self, other):
        """
        implement > operator (internally used in sort function). A word is
        greater that another word, if the count is greater. for equal counts
        we use alphabetic order
        """

        if self.count == other.count:
            return self.word < other.count
        return self.count > other.count

    def __str__(self):
        return str(self.word)


def main():



if __name__ == '__main__':
    main()
