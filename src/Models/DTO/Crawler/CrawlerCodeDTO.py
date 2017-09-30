class CrawlerCodeDTO(object):
    """
        Object that contains grouped all data of the code
    """

    def __init__(self, id, libs, comments, variable_names, function_names, class_name, lines_number, code):
        self.id = id
        self.libs = libs if len(libs) > 0 else []
        self.comments = comments if len(comments) > 0 else []
        self.variable_names = variable_names if len(variable_names) > 0 else []
        self.function_names = function_names if len(function_names) > 0 else []
        self.class_name = class_name if len(class_name) > 0 else []
        self.lines_number = lines_number if lines_number else 1
        self.score = 0.0
        self.code = code
