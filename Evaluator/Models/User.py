class User(object):
    """
        Object that contains grouped all data of the user
    """

    def __init__(self, client_id, search_query, libs, comments):
        self.client_id = client_id
        self.search_query = search_query
        self.libs = libs if libs else []
        self.comments = comments if comments else []
