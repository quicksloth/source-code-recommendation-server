from PythonCodeExtractor import PythonCodeExtractor

expr = """import ast
import os
import collections.OrderedDict as od
import javalang
from os import *
# Teste comment
bla="bla"
'''testeinasdnkansdjkas
testando comments
'''
test, test2 = "teste" # teste2 222 2
# # def foo():
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

expr4 = """
t = 1
'''tete0
teste1
teste2'''
t = 2
"""

p = PythonCodeExtractor()
print(p.extract_libs(p.extract_ast(expr3)))
print(p.extract_variables_names(p.extract_ast(expr3)))
print(p.extract_functions_names(p.extract_ast(expr3)))
print(p.extract_classes(p.extract_ast(expr3)))
print(p.extract_comments(expr, p.extract_ast(expr)))
print(p.extract_doc_strings(p.extract_ast(expr3)))
print(p.extract_number_of_lines(expr2))
