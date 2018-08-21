class Node(object):
    """
    Node in the graph. This class contains only info that defines the node.
    The basic information is name which uniquely identifies the node in the graph,
    and the initial weight.
    """

    def __init__(self, name: str, initial_weight: float = 1) -> None:
        """
        Create new node info, will contain all the information that will
        define the node as separate entity.

        :param name: name of the node, unique identifier in the graph.
        :param initial_weight: weight which will be used as initial value. Can change in the future.
        """
        self.name = name
        self.weight = initial_weight

    def get_name(self) -> str:
        """
        :return: name of this node, unique identifier in the graph.

        """
        return self.name

    def get_weight(self) -> float:
        """
        :return: current weight of this node.
        """
        return self.weight

    def set_weight(self, new_weight: float):
        """
        Set the weight of this node.
        :param new_weight: which will be used as weight of this node in the future.
        """
        self.weight = new_weight

    def __str__(self):
        return self.get_name() + ": " + self.get_weight().__str__()

    def __hash__(self):
        return hash(self.get_name())

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if other.get_name() == self.get_name():
            return True
        return False
