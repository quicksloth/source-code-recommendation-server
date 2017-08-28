import sys

from Modules.AbstractModule import AbstractModule


class UnderstandingModule(AbstractModule):
    """
        Module to extract how easy is to understand
        the searched code
    """

    def __init__(self, internal_weights=1, weight=1):
        AbstractModule.__init__(self, internal_weights, weight)

    @staticmethod
    def getDistanceMinMaxLinesSize(searched_codes):
        # min_lines = sys.maxint
        # max_lines = 0
        print('SADJASBDKSA')
        t = [doc.codes for doc in searched_codes]
        print(t)
        t2 = [t1.id for t1 in t]
        print(t2)
        # print([code for code in t])
        # max_lines = max([code.lines_number for code in [doc.codes for doc in searched_codes]])
        # min_lines = min([code.lines_number for code in [doc.codes for doc in searched_codes]])
        # print(max_lines)
        # print(min_lines)
        # max(path.nodes, key=lambda item: item.y)
        # https://stackoverflow.com/questions/6085467/python-min-function-with-a-list-of-objects
        # for doc in searched_codes:
        # for code in doc:
        #     min_lines = min(min_lines, code.lines_number)
        #     max_lines = min(max_lines, code.lines_number)

    def evaluate_code(self, input_bus_vo, search_result_id, code_id):
        # input_bus_vo.searched_codes[search_result_id].codes[code_id].libs
        UnderstandingModule().getDistanceMinMaxLinesSize(input_bus_vo.searched_codes)
        return code_id
