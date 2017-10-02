from Modules.AbstractModule import AbstractModule


class UnderstandingModule(AbstractModule):
    """
        Module to extract how easy is to understand
        the searched code
    """

    D = 10
    E = 100

    def __init__(self, internal_weights=[1, 1], weight=1):
        AbstractModule.__init__(self, internal_weights, weight)
        self.sum_internal_weights = sum(self.internal_weights)

    def evaluate_code(self, input_bus_vo, search_result_id, code_id):
        code_lines_score = self.evaluate_by_code_lines(code_id, input_bus_vo, search_result_id)

        comments = input_bus_vo.searched_codes[search_result_id].codes[code_id].comments

        new_comments_lines = 0
        for comment in comments:
            new_comments_lines += comment.count('\n')

        comments_line_number = len(comments) + new_comments_lines
        count_lines = input_bus_vo.searched_codes[search_result_id].codes[code_id].lines_number

        divisor = (count_lines - comments_line_number)
        comments_score = comments_line_number / divisor if divisor > 0 else 0

        score = (code_lines_score * self.internal_weights[0]) + (comments_score * self.internal_weights[1])

        return (score / self.sum_internal_weights) * self.weight

    def evaluate_by_code_lines(self, code_id, input_bus_vo, search_result_id):
        max_min_diff = input_bus_vo.code_max_lines - input_bus_vo.code_min_lines
        ti = input_bus_vo.searched_codes[search_result_id].codes[code_id].lines_number

        if max_min_diff > self.D:
            code_lines_score = 1 - (ti - input_bus_vo.code_min_lines) * (1 / max_min_diff)
        else:
            code_lines_score = 1 - ((self.D / self.E) * (ti - input_bus_vo.code_min_lines))

        return code_lines_score
