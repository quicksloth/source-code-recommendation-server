from Modules.AbstractModule import AbstractModule


class LowCouplingModule(AbstractModule):
    """
        Module to extract evaluate low coupling
        between searched and user code
    """

    def __init__(self, internal_weights=1, weight=1):
        AbstractModule.__init__(self, internal_weights, weight)

    def evaluate_code(self, input_bus_vo, search_result_id, code_id):
        user_libs = input_bus_vo.user.libs
        code_libs = input_bus_vo.searched_codes[search_result_id].codes[code_id].libs

        diff = set(code_libs).difference(set(user_libs))
        code_libs_size = len(code_libs)

        result = 1
        if code_libs_size > 0:
            result -= (len(diff) / code_libs_size)

        return result * self.weight
