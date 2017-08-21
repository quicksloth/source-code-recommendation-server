from Modules.AbstractModule import AbstractModule


class LowCouplingModule(AbstractModule):
    """
        Module to extract evaluate low coupling
        between searched and user code
    """

    def __init__(self, internal_weights, weight):
        AbstractModule.__init__(self, internal_weights, weight)

    def evaluate_code(self, input_bus_vo, code_id):
        #  TODO evaluate code in low coupling
        return code_id

# t = NlpModule([1], 3)
# t.evaluate_code("t", 12)
