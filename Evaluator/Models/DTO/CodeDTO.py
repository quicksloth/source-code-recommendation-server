class CodeDTO(object):
    """
        Object to transfer code with score
        and all complementary data to client
    """

    def __init__(self, code_id, code_text, score, source_link, client_id):
        self.code_id = code_id
        self.code_text = code_text if code_text else ''
        self.score = score if score else 0.0
        self.source_link = source_link if source_link else ''
        self.client_id = client_id if client_id else ''

    # def serialize:
    # TODO serialize this object to string
