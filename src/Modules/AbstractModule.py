class AbstractModule:
    """ Abstraction (parent) of all module
        This class contains all generic data and functions
        for every module for EvaluatorModel
    """

    def __init__(self, internal_weights=[], weight=1):
        self.internal_weights = internal_weights
        self.weight = weight

    def evaluate_code(self, input_bus_vo, code_id):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abtract method")
