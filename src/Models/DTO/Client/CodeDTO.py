class CodeDTO(object):
    """
        Object to transfer code with score
        and all complementary data to client
    """

    def __init__(self, code, score, source_link):
        self.code = code if code else ''
        self.score = score if score else 0.0
        self.source_link = source_link if source_link else ''

    # def serialize:
    # TODO serialize this object to string
