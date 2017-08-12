from AbstractModule import AbstractModule


class UnderstandingModule(AbstractModule):
    """
        Module to extract how easy is to understand
        the searched code
    """

    def __init__(self, internal_weights, weight):
        AbstractModule.__init__(self, internal_weights, weight)

    def evaluate_code(self, input_bus_vo, code_id):
        return code_id

# t = NlpModule([1], 3)
# t.evaluate_code("t", 12)
