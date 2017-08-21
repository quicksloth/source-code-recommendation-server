# import javalang
import ast
from ASTExtractors.PythonAstExtractor import PythonAstExtractor

class InputBus:
    """
        Object that contains data of the user and list of searchedCode
        to extract more data from these
    """

    def __init__(self, user = {}, searched_codes = {}, language = 'python'):
        self.user = user
        self.searched_codes = searched_codes
        if language == 'python':
            self.ast_extractor = PythonAstExtractor()

    def extract_ast(self, code_text):
        return self.ast_extractor.extract_ast(code_text=code_text)

    def extract_comments_from_ast(self, extractedAst):
        return self.ast_extractor.extract_comments(extractedAst=extractedAst)

    def extract_variables_from_ast(self, extractedAst):
        return self.ast_extractor.extract_variables_names(extractedAst=extractedAst)

    def extract_functions_from_ast(self, extractedAst):
        return self.ast_extractor.extract_functions_names(extractedAst=extractedAst)

    def extract_classes_from_ast(self, extractedAst):
        return self.ast_extractor.extract_classes(extractedAst=extractedAst)

    def extract_libs_from_ast(self, extractedAst):
        return self.ast_extractor.extract_libs(extractedAst=extractedAst)

# ast.parse()

# Python------
# code = '''def extract_ast(self, code_text): return code_text'''
expr="""
import ast
import os
import collections.OrderedDict as od
import javalang
from os import *
bla="bla"
test, test2 = "teste"
def foo():
   t = "testing"
   print("hello world")
def foobar():
   t = "testing"
   print("hello world")
class Test:
    def bar(self):
        print 'ola'
"""

inputBus = InputBus()
extractedAst = inputBus.extract_ast(expr)
# print extractedAst.__dict__
# print ast.iter_child_nodes(extractedAst)
print inputBus.extract_functions_from_ast(extractedAst=extractedAst)
print inputBus.extract_classes_from_ast(extractedAst=extractedAst)
print inputBus.extract_libs_from_ast(extractedAst=extractedAst)
# print ast.dump(extractedAst)



# ---------------------------------------------------------------

# expr2 = "import ast\ntest = \"teste\"\ndef foo():\nprint(\"hello world\")\nast.parse(\"def bar(t): return t\")"
# tree = ast.parse(code)
# tree2 = ast.parse(expr)
# print tree2._fields
# tree3 = ast.parse(expr2)

# print tree2.__dict__
# print tree2.get_docstring()
# imports = [node for node in tree2.body if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom) ]
# print imports
# importsNamesDict = [importNode.__dict__ for importNode in imports]
# print importsNamesDict[0]['names'][0].name
#
# print importsNamesDict[0]._fields
#
# importsNames = [importNode.module for importNode in imports if isinstance(importNode, ast.ImportFrom)]
#
# print importsNames
# print tree3.__dict__
#
# variables = [node for node in tree2.body if isinstance(node, ast.Assign)]
# print variables[0]
# print variables[0].targets
# print variables[0].targets[0].__dict__
#
# [node for node in module.body if isinstance(node, ast.FunctionDef)]
#
# print tree
# print tree.__dict__
# print tree2
#
# t = ast.dump(tree2)
# print t
#
#  -------