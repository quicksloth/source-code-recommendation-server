from sets import Set
import ast

class PythonAstExtractor:
    """
        Class to extract data of Python code (string)
    """

    @staticmethod
    def extract_ast(code_text):
        try:
            return ast.parse(code_text)
        except:
            raise Exception('Error in parsing extractedAst')

    @staticmethod
    def extract_comments(extractedAst):
        # TODO extract comments from extractedAst
        return ""

    @staticmethod
    def extract_variables_names(extractedAst):
        var_names = Set([])
        for node in ast.walk(extractedAst):
            if isinstance(node, ast.Assign):
                for node_target in node.targets:
                    if isinstance(node_target, ast.Name):
                        var_names.add(node_target.id)
                    elif isinstance(node_target, ast.Tuple):
                        for elt in node_target.elts:
                            var_names.add(elt.id)
        return list(var_names)

    @staticmethod
    def extract_functions_names(extractedAst):
        return extract_by_type(extractedAst, ast.FunctionDef)

    @staticmethod
    def extract_classes(extractedAst):
        return extract_by_type(extractedAst, ast.ClassDef)

    @staticmethod
    def extract_libs(extractedAst):
        lib_names = Set([])
        for node in extractedAst.body:
            if isinstance(node, ast.Import):
                for node_name in node.names:
                    lib_names.add(split_by_point(node_name.name))
            elif isinstance(node, ast.ImportFrom):
                lib_names.add(split_by_point(node.module))
        return list(lib_names)

def split_by_point(text):
    return text.split('.')[0]

def extract_by_type(extractedAst, type):
    return [node.name for node in ast.walk(extractedAst) if isinstance(node, type)]

