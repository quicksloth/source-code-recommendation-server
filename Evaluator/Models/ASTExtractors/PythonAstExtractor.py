import ast

class PythonAstExtractor:
    """
        Class to extract data of Python code (string)
    """

    @staticmethod
    def extract_ast(code_text):
        return ast.parse(code_text)

    @staticmethod
    def extract_comments(ast):
        return ""

    @staticmethod
    def extract_variables_names(ast):
        # TODO extract variables from ast
        return ast
# Assign
    @staticmethod
    def extract_functions_names(ast):
        function_definitions = [node for node in ast.body if isinstance(node, ast.FunctionDef)]
        return [f.name for f in function_definitions]

    @staticmethod
    def extract_classes(ast):
        # TODO extract classes from ast
        return ast

    @staticmethod
    def extract_libs(ast):
        libs = [node for node in ast.body if isinstance(node, ast.Import)]
        return libs


# JAVA------
# javafile  = "BufferedReader br = new BufferedReader(new FileReader(\"file.txt\")); " \
#             "try {" \
#             "StringBuilder sb = new StringBuilder();" \
#             "String line = br.readLine();" \
#             "while (line != null) {" \
#             "sb.append(line);" \
#             "sb.append(System.lineSeparator());" \
#             "line = br.readLine();" \
#             "}" \
#             "String everything = sb.toString();" \
#             "} finally {" \
#             "br.close();" \
#             "}"
#
# tokens = javalang.tokenizer.tokenize("FileInputStream inputStream = new FileInputStream(\"foo.txt\");")
# parser = javalang.parser.Parser(tokens)
# t = parser.parse_expression()
# print t
#  -------

# JAVA2------
# import plyj.parser as plyj

# print tree.package.name
# print tree
#  -------

# Python------
# code = '''def extract_ast(code_text): return code_text'''
expr="""
import ast
import os
import javalang
test = "teste"
def foo():
   print("hello world")
   ast.parse("def bar(t): return t")
"""
# expr2 = "import ast\ntest = \"teste\"\ndef foo():\nprint(\"hello world\")\nast.parse(\"def bar(t): return t\")"
# tree = ast.parse(code)
tree2 = ast.parse(expr)
# tree3 = ast.parse(expr2)

print tree2.__dict__
imports = [node for node in tree2.body if isinstance(node, ast.Import)]
print imports

# print tree3.__dict__

# [node for node in module.body if isinstance(node, ast.FunctionDef)]

# print tree
# print tree.__dict__
# print tree2

# t = ast.dump(tree)


#  -------