from Models.CodeExtractors.PythonCodeExtractor import PythonCodeExtractor


class InputBus:
    """
        Object that contains data of the user and list of searchedCode
        to extract more data from these
    """

    def __init__(self, user=None, searched_codes=None, language='python'):
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
        print('set_distance_min_max_lines_size')
        lines = []
        for doc in self.searched_codes:
            print('doc', doc)
            for code in doc.codes:
                print('code', code)
                print('code.lines_number', code.lines_number)
                lines.append(code.lines_number)

        print('lines', lines)
        self.code_max_lines = max(lines)
        print('max', max(lines))
        print('code_max_lines', self.code_max_lines)
        self.code_min_lines = min(lines)
        print('min', min(lines))
        print('code_min_lines', self.code_min_lines)
