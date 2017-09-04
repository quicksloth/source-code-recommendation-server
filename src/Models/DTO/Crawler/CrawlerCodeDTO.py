class CrawlerCodeDTO(object):
    """
        Object that contains grouped all data of the code
    """

    def __init__(self, id, libs, comments, variable_names, function_names, class_name, lines_number):
        self.id = id
        self.libs = libs if libs else []
        self.comments = comments if comments else []
        self.variable_names = variable_names if variable_names else []
        self.function_names = function_names if function_names else []
        self.class_name = class_name if class_name else []
        self.lines_number = lines_number if lines_number else []
        self.score = 0.0
