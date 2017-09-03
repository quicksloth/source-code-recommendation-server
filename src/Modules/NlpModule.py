from Modules.AbstractModule import AbstractModule
from Modules.Concepts.ComplexNetwork import ComplexNetwork

t1 = 'Lorem ipsum dolor sit amet Nullam metus.'
t2 = 'Lorem ipsum Consectetur adipiscing elit.'
textual = [t1, t2]


class NlpModule(AbstractModule):
    """
        Module to extract natural language
        distance between searched code and
        documentation and user code
    """

    def __init__(self, internal_weights=[1, 1, 1, 1, 1], weight=1, complex_network=ComplexNetwork()):
        AbstractModule.__init__(self, internal_weights, weight)
        self.complex_network = complex_network

    def evaluate_code(self, input_bus_vo, search_result_id, code_id):
        #  TODO evaluate code in nlo
        return self.complex_network.get_contextual_distance(one_word="lorem", second_word="ipsum")

# t = NlpModule([1], 3)
# t.evaluate_code("t", 12)
