from AbstractModule import AbstractModule
from Concepts.ComplexNetwork import ComplexNetwork

t1 = 'Lorem ipsum dolor sit amet Nullam metus.'
t2 = 'Lorem ipsum Consectetur adipiscing elit.'
textual = [t1, t2]


class NlpModule(AbstractModule):
    """
        Module to extract natural language
        distance between searched code and
        documentation and user code
    """

    def __init__(self, internal_weights, weight):
        AbstractModule.__init__(self, internal_weights, weight)
        self.complex_network = ComplexNetwork(textual_train_base=textual)

    def evaluate_code(self, input_bus_vo, code_id):
        self.complex_network.get_contextual_distance(one_word="lorem", second_word="ipsum")

# t = NlpModule([1], 3)
# t.evaluate_code("t", 12)
