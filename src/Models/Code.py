class Code(object):
    """
        Object that contains grouped all data of the code
    """

    def __init__(self, libs, comments, variable_names, function_names, class_name):
        self.libs = libs if libs else []
        self.comments = comments if comments else []
        self.variable_names = variable_names if variable_names else []
        self.function_names = function_names if function_names else []
        self.class_name = class_name if class_name else []
