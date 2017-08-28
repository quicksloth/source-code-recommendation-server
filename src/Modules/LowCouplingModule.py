from Modules.AbstractModule import AbstractModule


class LowCouplingModule(AbstractModule):
    """
        Module to extract evaluate low coupling
        between searched and user code
    """

    def __init__(self, internal_weights=1, weight=1):
        AbstractModule.__init__(self, internal_weights, weight)

    def evaluate_code(self, input_bus_vo, search_result_id, code_id):
        #  TODO TEST THIS => evaluate code in low coupling
        # DEBUGGING
        user_libs = input_bus_vo.user.libs
        print(user_libs)
        code_libs = input_bus_vo.searched_codes[search_result_id].codes[code_id].libs
        print(code_libs)
        result = set(code_libs).difference(set(user_libs))
        print("result = %d" % len(result))
        return len(result)

# t = NlpModule([1], 3)
# t.evaluate_code("t", 12)
