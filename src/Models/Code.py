class Code(object):
    """
        Object that contains grouped all data of the code
    """

    def __init__(self, code_id, libs, comments, variable_names, function_names, class_name, documentation, source_link):
        self.code_id = code_id
        self.libs = libs if libs else []
        self.comments = comments if comments else []
        self.variable_names = variable_names if variable_names else []
        self.function_names = function_names if function_names else []
        self.class_name = class_name if class_name else []
        self.documentation = documentation if documentation else []
        self.source_link = source_link if source_link else ''
