import os
import sys

# TODO: try to find another way to solve this problem
# issue 12 https://github.com/quicksloth/source-code-recommendation-server/issues/11
# Necessary to import modules in the same level
from Models.Code import Code
from Models.SearchResult import SearchResult

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import server
from uuid import uuid4
from Models.RequestCode import RequestCode
from Models.db.RequestDB import RequestDB
from Models.InputBus import InputBus


class EvaluatorController(object):
    """
        Controller of the evaluator model
    """

    modules_weights = []

    @staticmethod
    def init_get_recommendation_code():
        request_id = str(uuid4())

        # TODO: remove mocked data - get from request
        rc = RequestCode(query='read file', libs=['os'], comments=['comments'], language='Python',
                         request_id=request_id)
        data = rc.toRequestJSON()

        RequestDB().add(rc)
        server.get_source_codes(data=data)

    @staticmethod
    def evaluate_search_codes(request):
        request_json = request.get_json()
        results = request_json.get('searchResult')

        rc = RequestDB().get_request_by_id(request_json.get('requestID'))

        for idx, result in enumerate(results):
            request_code = RequestCode(**rc[0])
            sr = SearchResult(id=idx, source_link=result.url, documentation=result.documentation)

            input_bus = InputBus(user=request_code, searched_codes=sr)

            for code in result.sourceCode:
                ast = input_bus.code_extractor.extract_ast(code_text=code)

                libs = input_bus.code_extractor.extract_libs(ast)
                comments = input_bus.code_extractor.extract_comments(code, ast)
                variable_names = input_bus.code_extractor.extract_variables_names(ast)
                function_names = input_bus.code_extractor.extract_functions_names(ast)
                class_name = input_bus.code_extractor.extract_classes(ast)

                c = Code(libs=libs,
                         comments=comments,
                         variable_names=variable_names,
                         function_names=function_names,
                         class_name=class_name)

                sr.add_code(code)


