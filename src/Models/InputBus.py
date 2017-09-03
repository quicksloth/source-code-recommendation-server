from Models.CodeExtractors.PythonCodeExtractor import PythonCodeExtractor


class InputBus:
    """
        Object that contains data of the user and list of searchedCode
        to extract more data from these
    """

    def __init__(self: object, user=None, searched_codes=None, language: object = 'python') -> object:
        if searched_codes is None:
            searched_codes = []

        if user is None:
            user = {}

        self.user = user
        self.searched_codes = searched_codes
        self.code_max_lines = 0
        self.code_min_lines = 0

        if language.lower() == 'python':
            self.code_extractor = PythonCodeExtractor()

    def add_searched_code(self, sc):
        self.searched_codes.append(sc)

    def set_distance_min_max_lines_size(self):
        lines = []
        for doc in self.searched_codes:
            for code in doc.codes:
                lines.append(code.lines_number)

        self.code_max_lines = max(lines)
        self.code_min_lines = min(lines)

