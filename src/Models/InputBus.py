from Models.CodeExtractors.PythonCodeExtractor import PythonCodeExtractor


class InputBus:
    """
        Object that contains data of the user and list of searchedCode
        to extract more data from these
    """

    def __init__(self: object, user=None, searched_codes=None, language: object = 'python') -> object:
        if searched_codes is None:
            searched_codes = {}

        if user is None:
            user = {}

        self.user = user
        self.searched_codes = searched_codes

        if language == 'python':
            self.code_extractor = PythonCodeExtractor()


# Testing Python------
# expr = """
# import ast
# import os
# import collections.OrderedDict as od
# import javalang
# from os import *
# # Teste comment
# bla="bla"
# test, test2 = "teste"
# def foo():
#    t = "testing"
#    print("hello world")
# def foobar():
#    t = "testing"
#    print("hello world")
# class Test:
#     def bar(self):
#         print ('ola')
# """
#
# inputBus = InputBus()
# extracted_ast = inputBus.code_extractor.extract_ast(expr)
# print(extracted_ast.__dict__)
# print(inputBus.extract_functions_from_ast(expr))
# print(inputBus.extract_classes_from_ast(expr))
# print(inputBus.extract_libs_from_ast(expr))
# print(inputBus.extract_variables_from_ast(expr))
