import os
import sys
from uuid import uuid4

# from flask import json

# issue 12 https://github.com/quicksloth/source-code-recommendation-server/issues/11
# Necessary to import modules in the same level
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import server
from Modules.NlpModule import NlpModule
from Modules.LowCouplingModule import LowCouplingModule
from Modules.UnderstandingModule import UnderstandingModule
from Modules.Concepts.ComplexNetwork import ComplexNetwork

from Models.DTO.Client.CodeDTO import CodeDTO
from Models.DTO.Client.CodeResultsDTO import CodeResultsDTO
from Models.DTO.Crawler.CrawlerRequestDTO import CrawlerRequestDTO
from Models.DTO.Crawler.CrawlerResultDTO import CrawlerResultDTO

from Models.db.RequestDB import RequestDB
from Models.InputBus import InputBus


class EvaluatorController(object):
    """
        Controller of the evaluator model
    """

    modules_weights = []
    complex_network = ComplexNetwork()
    low_coupling_module = LowCouplingModule(weight=5)
    understanding_module = UnderstandingModule(weight=1)
    nlp_module = NlpModule(weight=5)

    @staticmethod
    def get_recommendation_code(request_id, query, libs, comments, language):
        request_code = CrawlerRequestDTO(query=query,
                                         libs=libs,
                                         comments=comments,
                                         language=language,
                                         request_id=request_id)

        data = request_code.toRequestJSON()
        print(data)
        RequestDB().add(request_code)
        server.get_source_codes(data=data)

    @staticmethod
    def init_get_recommendation_code_with_mocked_data():
        request_id = str(uuid4())

        # TODO: remove mocked data - get from request
        request_code = CrawlerRequestDTO(query='read file',
                                         libs=['json', 'requests'],
                                         comments=['comments'],
                                         language='Python',
                                         request_id=request_id)
        data = request_code.toRequestJSON()
        print(data)
        RequestDB().add(request_code)
        server.get_source_codes(data=data)

    @classmethod
    def evaluate_search_codes(cls, request):
        request_json = request.get_json()
        # print(request_json)
        request_id = request_json.get('requestID')
        results = request_json.get('searchResult')

        rc = RequestDB().get_request_by_id(request_id)

        request_code = CrawlerRequestDTO(**rc[0])
        RequestDB().remove(request_id)

        input_bus = cls.map_crawler_result(request_code, results)
        code_results = CodeResultsDTO(request_id=request_id)

        for idx, searched_code in enumerate(input_bus.searched_codes):
            for idy, code in enumerate(searched_code.codes):
                cls.evaluate_codes(code, idx, idy, input_bus)
                code_results.add_code(CodeDTO().from_crawler_code(crawler_code=code, crawler_result=searched_code))

        code_results = code_results.toJSON()
        print(code_results)
        server.emit_code_recommendations(request_id, code_results)
        return code_results

    @classmethod
    def evaluate_codes(cls, code, idx, idy, input_bus):
        low_coupling_score = cls.low_coupling_module.evaluate_code(input_bus_vo=input_bus, search_result_id=idx,
                                                                   code_id=idy)
        understanding_score = cls.understanding_module.evaluate_code(input_bus_vo=input_bus,
                                                                     search_result_id=idx,
                                                                     code_id=idy)
        nlp_score = cls.nlp_module.evaluate_code(input_bus_vo=input_bus, search_result_id=idx,
                                                 code_id=idy)

        print('low_coupling_score', low_coupling_score / cls.low_coupling_module.weight)
        print('understanding_score', understanding_score / cls.understanding_module.weight)
        print('nlp_score', nlp_score / cls.nlp_module.weight)
        sum_weight = (cls.low_coupling_module.weight + cls.understanding_module.weight + cls.nlp_module.weight)
        print('----------')
        final_score = (low_coupling_score + understanding_score + nlp_score) / sum_weight
        code.score = final_score

    @staticmethod
    def map_crawler_result(request_code, results):
        input_bus = InputBus(user=request_code)
        ast_errors = 0
        for idx, result in enumerate(results):
            search_result = CrawlerResultDTO(request_id=idx, source_link=result.get('url'),
                                             documentation=result.get('documentation'))

            ast_errors = search_result.map_from_request(input_bus=input_bus, result=result, ast_errors=ast_errors)
            input_bus.add_searched_code(search_result)

        input_bus.set_distance_min_max_lines_size()

        if ast_errors > 0:
            print("ERROR TO EXTRACT AST ", ast_errors)

        return input_bus

    def train_network(self, train_database):
        self.complex_network.train_network(textual_train_base=train_database)

    def get_complex_network(self):
        return self.complex_network.adjacency_list
