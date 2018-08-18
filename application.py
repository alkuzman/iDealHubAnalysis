from abc import abstractmethod


class Application:
    """
    This class represents the entry point of the application. Use the run method to start this application.
    """

    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        """
        Runs this application. For more info see the concrete implementations of this class.
        """
        pass
