class CodeResultsDTO(object):
    """
        Object to transfer all
        code recommendations
    """

    def __init__(self, codes=None):
        if codes is None:
            codes = []
        self.codes = codes

    def add_code(self, code):
        self.codes.append(code)

        # def serialize:
        # TODO serialize this object to string
