from Modules.AbstractModule import AbstractModule
from Modules.Concepts.ComplexNetwork import ComplexNetwork


class NlpModule(AbstractModule):
    """
        Module to extract natural language
        distance between searched code and
        documentation and user code
    """

    def __init__(self, internal_weights=None, weight=1, complex_network=None):
        if internal_weights is None:
            internal_weights = [0.5, 0.125, 0.05, 0.2, 0.125]
        AbstractModule.__init__(self, internal_weights, weight)

        if complex_network is None:
            complex_network = ComplexNetwork()
        self.complex_network = complex_network

    def __get_score_by_doc_combination(self, first_doc, second_doc):
        return 1 - self.complex_network.get_contextual_distance_between_docs(first_doc, second_doc)

    def __evaluate_query_vs_doc(self, query, doc, pos):
        score = self.__get_score_by_doc_combination(query, doc)
        return self.internal_weights[pos] * score

    def __evaluate_query_vs_comments(self, query, user_comments, pos):
        grouped_comments = " ".join(user_comments)
        score = self.__get_score_by_doc_combination(query, grouped_comments)
        return self.internal_weights[pos] * score

    def __evaluate_comments_vs_comments(self, user_comments, code_comments, pos):
        grouped_user_comments = " ".join(user_comments)
        grouped_code_comments = " ".join(code_comments)
        score = self.__get_score_by_doc_combination(grouped_user_comments, grouped_code_comments)
        return self.internal_weights[pos] * score

    def __evaluate_comments_vs_doc(self, user_comments, doc, pos):
        grouped_user_comments = " ".join(user_comments)
        score = self.__get_score_by_doc_combination(grouped_user_comments, doc)
        return self.internal_weights[pos] * score

    def __evaluate_query_vs_code(self, query, code_dto, pos):
        grouped_variable = " ".join(code_dto.variable_names)
        grouped_functions = " ".join(code_dto.function_names)
        grouped_classes = " ".join(code_dto.class_name)
        # print('grouped_variable ', grouped_variable)
        # print('grouped_functions ', grouped_functions)
        # print('grouped_classes ', grouped_classes)
        code = grouped_variable + ' ' + grouped_functions + ' ' + grouped_classes
        # print('code ', code)
        score = self.__get_score_by_doc_combination(query, code)
        return self.internal_weights[pos] * score

    def evaluate_code(self, input_bus_vo, search_result_id, code_id):
        score = 0

        # Search Query vs Doc
        score += self.__evaluate_query_vs_doc(input_bus_vo.user.query,
                                              input_bus_vo.searched_codes[search_result_id].documentation, 0)

        # User Comments vs Doc
        score += self.__evaluate_comments_vs_doc(input_bus_vo.user.comments,
                                                 input_bus_vo.searched_codes[search_result_id].documentation, 1)

        # Search Query vs Classes, Functions and Variables
        score += self.__evaluate_query_vs_code(input_bus_vo.user.query,
                                               input_bus_vo.searched_codes[search_result_id].codes[code_id], 2)

        # Search Query vs Comments
        score += self.__evaluate_query_vs_comments(input_bus_vo.user.query,
                                                   input_bus_vo.searched_codes[search_result_id].codes[
                                                       code_id].comments, 3)

        # User Comments vs Comments
        score += self.__evaluate_comments_vs_comments(input_bus_vo.user.comments,
                                                      input_bus_vo.searched_codes[search_result_id].codes[
                                                          code_id].comments, 4)

        return self.weight * score
