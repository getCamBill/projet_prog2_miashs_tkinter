class Piece(object):

    def __init__(self,color: str = None, shape: str = None, size: str = None, dug: int = None):
        """

        :param color:
        :param shape:
        :param size:
        :param dug:
        """

        self.color: str = color
        self.shape: str = shape
        self.size: str = size
        self.dug: int = dug
