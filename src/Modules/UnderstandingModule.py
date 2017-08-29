from Modules.AbstractModule import AbstractModule


class UnderstandingModule(AbstractModule):
    """
        Module to extract how easy is to understand
        the searched code
    """

    threshold = 10

    def __init__(self, internal_weights=[1,1], weight=1):
        AbstractModule.__init__(self, internal_weights, weight)

    def evaluate_code(self, input_bus_vo, search_result_id, code_id):
        # input_bus_vo.searched_codes[search_result_id].codes[code_id].libs
        # print(input_bus_vo.code_max_lines)
        # print(input_bus_vo.code_min_lines)

        code_lines_score = self.evaluate_by_code_lines(code_id, input_bus_vo, search_result_id)

        score = code_lines_score*self.internal_weights[0]
        return score * self.weight

    def evaluate_by_code_lines(self, code_id, input_bus_vo, search_result_id):
        max_min_diff = input_bus_vo.code_max_lines - input_bus_vo.code_min_lines
        ti = input_bus_vo.searched_codes[search_result_id].codes[code_id].lines_number
        code_lines_score = 0
        if max_min_diff > self.threshold:
            code_lines_score = 1 - (ti - input_bus_vo.code_min_lines) * (1 / max_min_diff)
        else:
            print('do other thing')
            # code_lines_score = 1 - (self.threshold /)
        return code_lines_score

