from Models.ASTExtractors.PythonAstExtractor import PythonAstExtractor


class InputBus:
    """
        Object that contains data of the user and list of searchedCode
        to extract more data from these
    """

    def __init__(self: object, user: object = {}, searched_codes: object = {}, language: object = 'python') -> object:
        self.user = user
        self.searched_codes = searched_codes
        if language == 'python':
            self.ast_extractor = PythonAstExtractor()

    def extract_ast(self, code_text):
        return self.ast_extractor.extract_ast(code_text=code_text)

    def extract_comments_from_ast(self, code_text):
        _ast = self.extract_ast(code_text)
        return self.ast_extractor.extract_comments(_ast)

    def extract_variables_from_ast(self, code_text):
        _ast = self.extract_ast(code_text)
        return self.ast_extractor.extract_variables_names(_ast)

    def extract_functions_from_ast(self, code_text):
        _ast = self.extract_ast(code_text)
        return self.ast_extractor.extract_functions_names(_ast)

    def extract_classes_from_ast(self, code_text):
        _ast = self.extract_ast(code_text)
        return self.ast_extractor.extract_classes(_ast)

    def extract_libs_from_ast(self, code_text):
        _ast = self.extract_ast(code_text)
        return self.ast_extractor.extract_libs(_ast)


# Python------
expr = """
import ast
import os
import collections.OrderedDict as od
import javalang
from os import *
# Teste comment
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
        print ('ola')
"""

inputBus = InputBus()
extracted_ast = inputBus.extract_ast(expr)
# print extracted_ast.__dict__
# print ast.iter_child_nodes(extracted_ast)
print(inputBus.extract_functions_from_ast(expr))
print(inputBus.extract_classes_from_ast(expr))
print(inputBus.extract_libs_from_ast(expr))
print(inputBus.extract_variables_from_ast(expr))
# print ast.dump(extracted_ast)
