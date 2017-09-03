import os
import sys
from uuid import uuid4

# TODO: try to find another way to solve this problem
# issue 12 https://github.com/quicksloth/source-code-recommendation-server/issues/11
# Necessary to import modules in the same level

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import server
from Modules.LowCouplingModule import LowCouplingModule
from Modules.UnderstandingModule import UnderstandingModule
from Models.RequestCode import RequestCode
from Models.db.RequestDB import RequestDB
from Models.InputBus import InputBus
from Models.Code import Code
from Models.SearchResult import SearchResult


class EvaluatorController(object):
    """
        Controller of the evaluator model
    """

    modules_weights = []
    lowCouplingModule = LowCouplingModule(weight=1)
    understandingModule = UnderstandingModule(weight=1)

    @staticmethod
    def init_get_recommendation_code():
        request_id = str(uuid4())

        # TODO: remove mocked data - get from request
        rc = RequestCode(query='read file', libs=['json', 'requests'], comments=['comments'], language='Python',
                         request_id=request_id)
        data = rc.toRequestJSON()

        RequestDB().add(rc)
        server.get_source_codes(data=data)

    @classmethod
    def evaluate_search_codes(cls, request):
        request_json = request.get_json()
        results = request_json.get('searchResult')

        request_id = request_json.get('requestID')
        rc = RequestDB().get_request_by_id(request_id)
        request_code = RequestCode(**rc[0])
        RequestDB().remove(request_id)

        ib = cls.map_crawler_result(request_code, results)

        for idx, searched_code in enumerate(ib.searched_codes):
            for idy, code in enumerate(searched_code.codes):
                low_coupling_score = cls.lowCouplingModule.evaluate_code(input_bus_vo=ib, search_result_id=idx,
                                                                         code_id=idy)

                understanding_score = cls.understandingModule.evaluate_code(input_bus_vo=ib, search_result_id=idx,
                                                                            code_id=idy)

                sum_weight = (cls.lowCouplingModule.weight + cls.understandingModule.weight)
                final_score = (low_coupling_score + understanding_score) / sum_weight
                code.score = final_score

                # TODO: continue here => modules

                # for idx, searched_code in enumerate(ib.searched_codes):
                #     for idy, code in enumerate(searched_code.codes):
                #         print(code.score)

    @staticmethod
    def map_crawler_result(request_code, results):
        input_bus = InputBus(user=request_code)
        for idx, result in enumerate(results):
            sr = SearchResult(id=idx, source_link=result.get('url'), documentation=result.get('documentation'))

            for code_idx, code in enumerate(result.get('sourceCode')):
                # TODO: maybe extract ast in different threads
                ast = input_bus.code_extractor.extract_ast(code_text=code)

                libs = input_bus.code_extractor.extract_libs(ast)
                comments = input_bus.code_extractor.extract_comments(code, ast)
                variable_names = input_bus.code_extractor.extract_variables_names(ast)
                function_names = input_bus.code_extractor.extract_functions_names(ast)
                class_name = input_bus.code_extractor.extract_classes(ast)
                lines = input_bus.code_extractor.extract_number_of_lines(code_text=code)

                sr.add_code(Code(id=code_idx,
                                 libs=libs,
                                 comments=comments,
                                 variable_names=variable_names,
                                 function_names=function_names,
                                 class_name=class_name,
                                 lines_number=lines))

            input_bus.add_searched_code(sr)

        input_bus.set_distance_min_max_lines_size()
        return input_bus
