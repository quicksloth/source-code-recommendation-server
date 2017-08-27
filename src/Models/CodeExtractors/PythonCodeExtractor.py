import ast
import tokenize
import numpy
from io import StringIO

from AbstractCodeExtrator import AbstractCodeExtractor


class PythonComments(Enum):
    single = '#'
    multiline = "'''"


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
    def extract_number_of_lines(code_text):
        # TODO: issues-8 (https://github.com/quicksloth/source-code-recommendation-server/issues/8)
        #  look another way to extract number of lines from ast instead of count \n
        return code_text.count('\n')

    @staticmethod
    def extract_doc_strings(extracted_ast):
        doc_strings = set([])
        for node in ast.walk(extracted_ast):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                doc_string = ast.get_docstring(node, clean=True)
                if doc_string:
                    doc_strings.add(doc_string)
        return doc_strings

    @staticmethod
    def extract_comments(code, extracted_ast):
        exclude_chars = [PythonComments.single, PythonComments.multiline]
        comments = set([])
        string_io = StringIO(code)
        multiline_started = false
        multiline_comments = ''

        # pass in stringio.readline to generate_tokens
        for toktype, tokval, begin, end, line in tokenize.generate_tokens(string_io.readline):
            if toktype == tokenize.COMMENT:
                # if it uses # or ''' is a comment in python and clean comments
                comment = "".join(filter(lambda char: char not in exclude_chars, tokval))
                # or (line.startswith("'''") and line.endswith("'''"))
                if comment and comment != '':
                    comments.add(comment)
                elif multiline_started == True and line.endswith(PythonComments.multiline):
                    comments.add()
                elif line.startswith(PythonComments.multiline):
                    multiline_started = True

        doc_strings = PythonCodeExtractor.extract_doc_strings(extracted_ast)
        return numpy.concatenate((list(comments), list(doc_strings)))

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


expr = """import ast
import os
import collections.OrderedDict as od
import javalang
from os import *
# Teste comment
bla="bla"
'''testeinasdnkansdjkas'''
test, test2 = "teste" # teste2 222 2
# # def foo():
#    t = "testing"
#    print("hello world")
def foobar():
   \"\"\"docstring\"\"\"
   t = "testing"
   print("hello world")
class Test:
    \"\"\"docstring test\"\"\"
    def bar(self):
        print ('ola')"""

expr2 = '''
import unittest
from algorithms import sorting

class Test( unittest.TestCase ):

  def testBubblesort( self ):
    A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    sorting.bubblesort( A )
    for i in range( 1, len( A ) ):
        if A[i - 1] < A[i]:
          self.fail( "bubblesort method fails." )
'''

expr3 = '''with open(fname) as f:\n    content = f.readlines()\n# you may also want to remove whitespace characters like `\\n` at the end of each line\ncontent = [x.strip() for x in content] \n'''

p = PythonCodeExtractor()
# print(p.extract_libs(p.extract_ast(expr3)))
# print(p.extract_variables_names(p.extract_ast(expr3)))
# print(p.extract_functions_names(p.extract_ast(expr3)))
# print(p.extract_classes(p.extract_ast(expr3)))
# print(p.extract_comments(expr3, p.extract_ast(expr3)))
# print(p.extract_doc_strings(p.extract_ast(expr3)))
print(p.extract_number_of_lines(expr2))
# p.extract_number_of_lines(expr)
# print (expr)
