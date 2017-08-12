class AbstractModule(object):
    """ Abstraction (parent) of all module
        This class contains all generic data and functions
        for every module for EvaluatorModel
    """

    def __init__(self, weights):
        self.weights = weights

    def setWeigth(self):
