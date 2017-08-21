class AbstractCodeExtractor:
    """
        Abstract Class to e
    """

    @staticmethod
    def extract_ast(code_text):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def extract_comments(extracted_ast):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def extract_variables_names(extracted_ast):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def extract_functions_names(extracted_ast):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def extract_classes(extracted_ast):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def extract_libs(extracted_ast):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def extract_number_of_lines(extracted_ast):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
