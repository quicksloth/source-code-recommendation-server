class CodeDTO(object):
    """
        Object to transfer code with score
        and all complementary data to client
    """

    def __init__(self, code=None, score=None, source_link=None):
        self.code = code if code else ''
        self.score = score if score else 0.0
        self.source_link = source_link if source_link else ''

    @staticmethod
    def from_crawler_code(crawler_result, crawler_code):
        return CodeDTO(source_link=crawler_result.source_link,
                       code=crawler_code.code,
                       score=crawler_code.score)

    # def serialize:
    # TODO serialize this object to string
