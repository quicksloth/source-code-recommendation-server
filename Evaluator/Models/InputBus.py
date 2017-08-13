class InputBus(object):
    """
        Object that contains data of the user and list of searchedCode
        to extract more data from these
    """

    def __init__(self, user, searched_codes):
        self.user = user
        self.searched_codes = searched_codes

    def extract_ast(self, code_text):
        # TODO extract ast from a code
        return code_text

    def extract_comments_from_ast(self, ast):
        # TODO extract comments from ast
        return ast

    def extract_variables_from_ast(self, ast):
        # TODO extract variables from ast
        return ast

    def extract_functions_from_ast(self, ast):
        # TODO extract functions from ast
        return ast

    def extract_classes_from_ast(self, ast):
        # TODO extract classes from ast
        return ast
