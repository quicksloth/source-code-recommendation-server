from tinydb import TinyDB, where
import os

dirname = os.path.dirname(os.path.abspath(__file__))


class RequestDB(object):
    def __init__(self):
        self.db = TinyDB(os.path.join(dirname, 'requestdb.json'))

    def add(self, request):
        if self.db.contains(where('request_id') == request.request_id):
            self.db.update(request.__dict__, where('request_id') == request.request_id)
        else:
            self.db.insert(request.__dict__)

    def get_request_by_id(self, request_id):
        return self.db.search(where('request_id') == request_id)