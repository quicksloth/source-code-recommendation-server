import json


class RequestCode(object):
    """
        Object that contains request code
    """

    def __init__(self, query, libs, comments, language):
        self.query = query
        self.libs = libs if libs else []
        self.comments = comments if comments else []
        self.language = language if language else 'Python'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def toRequestJSON(self, request_id):
        request = {
            'request_id': request_id,
            'query': self.query,
            'language': self.language,
        }
        return json.dumps(request)
