# import javalang
import ast
# from ASTExtractors.PythonAstExtractor import PythonAstExtractor

class InputBus(object):
    """
        Object that contains data of the user and list of searchedCode
        to extract more data from these
    """

    def __init__(self, user, searched_codes, language):
        self.user = user
        self.searched_codes = searched_codes
        # if language == 'python':
            # self.ast_extractor = PythonAstExtractor()

    def extract_ast(self, code_text):
        return self.ast_extractor.extract_ast(code_text=code_text)

    def extract_comments_from_ast(self, ast):
        return self.ast_extractor.extract_comments(ast=ast)

    def extract_variables_from_ast(self, ast):
        return self.ast_extractor.extract_variables_names(ast=ast)

    def extract_functions_from_ast(self, ast):
        return self.ast_extractor.extract_functions_names(ast=ast)

    def extract_classes_from_ast(self, ast):
        return self.ast_extractor.extract_classes(ast=ast)

    def extract_libs_from_ast(self, ast):
        return self.ast_extractor.extract_libs(ast=ast)


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

# ast.parse()

# Python------
# code = '''def extract_ast(self, code_text): return code_text'''
expr="""
import ast
import os
import javalang
from os import *
bla="bla"
test, test2 = "teste"
def foo():
   t = "testing"
   print("hello world")
"""
# expr2 = "import ast\ntest = \"teste\"\ndef foo():\nprint(\"hello world\")\nast.parse(\"def bar(t): return t\")"
# tree = ast.parse(code)
tree2 = ast.parse(expr)
print tree2._fields
# tree3 = ast.parse(expr2)

print tree2.__dict__
# print tree2.get_docstring()
imports = [node for node in tree2.body if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom) ]
print imports
importsNamesDict = [importNode.__dict__ for importNode in imports]
print importsNamesDict[0]
print getattr(importsNamesDict[0], 'names')

importsNames = [importNode.module for importNode in imports if isinstance(importNode, ast.ImportFrom)]

print importsNames
# print tree3.__dict__

variables = [node for node in tree2.body if isinstance(node, ast.Assign)]
print variables[0]
print variables[0].targets
# print variables[0].targets[0].__dict__

# [node for node in module.body if isinstance(node, ast.FunctionDef)]

# print tree
# print tree.__dict__
# print tree2

t = ast.dump(tree2)
print t

#  -------