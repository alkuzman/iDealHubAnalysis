import abc


class Data(metaclass=abc.ABCMeta):
    """
    This object represents textual data together with boost factor and an id
    """

    def get_content(self) -> str:
        """
        Get textual content of this data piece. The text is plain with no metadata.

        :return: textual representation of this piece of data
            """
        pass

    def get_boost(self) -> float:
        """
        Boost factor for this data object

        :return: boost factor of the content (describes the importance of the content)
        """
        pass

    def get_id(self) -> str:
        """
        Get the unique identifier of this object. Any object which is instance of Data and which has
        the exactly same id as this object, it represents the same object

        :return: id of this object
        """
        pass

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Data):
            return False
        if self.get_id() is None:
            return False
        return self.get_id().__eq__(other.get_id())

    def __hash__(self):
        self.get_id().__hash__()

    def __str__(self):
        result = (self.get_id(), self.get_content(), self.get_boost())
        return str(result)
