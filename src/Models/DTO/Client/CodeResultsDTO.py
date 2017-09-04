from flask import json


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

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
