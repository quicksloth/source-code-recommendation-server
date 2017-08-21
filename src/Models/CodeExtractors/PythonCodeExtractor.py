import ast
import tokenize

from io import StringIO

from Models.CodeExtractors.AbstractCodeExtrator import AbstractCodeExtractor


class PythonCodeExtractor(AbstractCodeExtractor):
    """
        Class to extract data of Python code (string)
    """

    @staticmethod
    def extract_ast(code_text):
        try:
            return ast.parse(code_text)
        except:
            raise Exception('Error in parsing extracted_ast')

    @staticmethod
    def extract_comments(code):
        # TODO extract comments from extracted_ast
        extract(code)
        return ""

    @staticmethod
    def extract_variables_names(extracted_ast):
        var_names = set([])
        for node in ast.walk(extracted_ast):
            if isinstance(node, ast.Assign):
                for node_target in node.targets:
                    if isinstance(node_target, ast.Name):
                        var_names.add(node_target.id)
                    elif isinstance(node_target, ast.Tuple):
                        for elt in node_target.elts:
                            var_names.add(elt.id)
        return list(var_names)

    @staticmethod
    def extract_functions_names(extracted_ast):
        return extract_by_type(extracted_ast, ast.FunctionDef)

    @staticmethod
    def extract_classes(extracted_ast):
        return extract_by_type(extracted_ast, ast.ClassDef)

    @staticmethod
    def extract_libs(extracted_ast):
        lib_names = set([])
        for node in extracted_ast.body:
            if isinstance(node, ast.Import):
                for node_name in node.names:
                    lib_names.add(split_by_point(node_name.name))
            elif isinstance(node, ast.ImportFrom):
                lib_names.add(split_by_point(node.module))
        return list(lib_names)


def split_by_point(text):
    return text.split('.')[0]


def extract_by_type(extracted_ast, type):
    return [node.name for node in ast.walk(extracted_ast) if isinstance(node, type)]


def extract(code):
    res = []
    comment = None
    string_io = StringIO(code)
    # pass in stringio.readline to generate_tokens
    for toktype, tokval, begin, end, line in tokenize.generate_tokens(string_io.readline):
        if toktype == tokenize.COMMENT:
            print(tokenize.untokenize([(toktype, tokval)]))
    print(tokenize.generate_tokens(string_io.readline))
            # print(toktype)

expr = """
import ast
import os
import collections.OrderedDict as od
import javalang
from os import *
# Teste comment
bla="bla"
test, test2 = "teste"
\"\"\"docstring\"\"\"
# # def foo():
#    t = "testing"
#    print("hello world")
def foobar():
   t = "testing"
   print("hello world")
class Test:
    def bar(self):
        print ('ola')
"""

p = PythonCodeExtractor()
p.extract_comments(expr)
# print (expr)