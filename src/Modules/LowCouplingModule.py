from Modules.AbstractModule import AbstractModule


class LowCouplingModule(AbstractModule):
    """
        Module to extract evaluate low coupling
        between searched and user code
    """

    def __init__(self, internal_weights, weight):
        AbstractModule.__init__(self, internal_weights, weight)

    def evaluate_code(self, input_bus_vo, search_result_id, code_id):
        #  TODO TEST THIS => evaluate code in low coupling
        user_libs = input_bus_vo.user.libs
        code_libs = input_bus_vo.searched_codes[search_result_id].codes[code_id].libs
        result = set(user_libs).difference(code_libs)
        return result

# t = NlpModule([1], 3)
# t.evaluate_code("t", 12)
