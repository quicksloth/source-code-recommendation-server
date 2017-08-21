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
        for node in extractedAst.body:
            if isinstance(node, ast.Assign):
                for node_name in node.names:
                    var_names.add(node_name.name)
            elif isinstance(node, ast.ImportFrom):
                var_names.add(node.module)
        return list(var_names)

    @staticmethod
    def extract_functions_names(extractedAst):
        # TODO: use ast.walk and implement visitor
        function_names = []
        for i_node in ast.iter_child_nodes(extractedAst):
            print i_node
            if isinstance(i_node, ast.FunctionDef):
                # print i_node
                function_names.append(i_node.name)

        return function_names

    @staticmethod
    def extract_classes(extractedAst):
        return [node.name for node in extractedAst.body if isinstance(node, ast.ClassDef)]

    @staticmethod
    def extract_libs(extractedAst):
        lib_names = Set([])
        for node in extractedAst.body:
            if isinstance(node, ast.Import):
                for node_name in node.names:
                    lib_names.add(node_name.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                lib_names.add(node.module.split('.')[0])
        return list(lib_names)