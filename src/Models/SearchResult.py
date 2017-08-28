class SearchResult(object):
    """
        Object that contains grouped all data of the code
    """

    def __init__(self, id, documentation, source_link):
        self.id = id
        self.source_link = source_link
        self.documentation = documentation if documentation else []
        self.codes = []

    def add_code(self, code):
        self.codes.append(code)