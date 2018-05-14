import abc


class Keyword(metaclass=abc.ABCMeta):
    """
    Keyword is any textual phrase assigned with score
    """

    @classmethod
    def get_phrase(self) -> str:
        """
        :return: textual phrase of the keyword.
            """
        pass

    @classmethod
    def get_score(self) -> float:
        """
        :return: document which should be anticipated as cover for requested analysis.
            """
        pass

    def __str__(self):
        result = (self.get_phrase(), self.get_score())
        return str(result)

    def __hash__(self):
        return hash(self.get_phrase())

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Keyword):
            return False
        if self.get_phrase() is None:
            return False
        if self.get_score() is None:
            return False
        return self.get_phrase().lower() == other.get_phrase().lower()
