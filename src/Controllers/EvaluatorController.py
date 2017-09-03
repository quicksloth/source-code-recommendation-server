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
from Modules.NlpModule import NlpModule
from Modules.LowCouplingModule import LowCouplingModule
from Modules.UnderstandingModule import UnderstandingModule
from Modules.Concepts.ComplexNetwork import ComplexNetwork

from Models.RequestCode import RequestCode
from Models.db.RequestDB import RequestDB
from Models.InputBus import InputBus
from Models.SearchResult import SearchResult


class EvaluatorController(object):
    """
        Controller of the evaluator model
    """

    modules_weights = []
    complex_network = ComplexNetwork()
    low_coupling_module = LowCouplingModule(weight=1)
    understanding_module = UnderstandingModule(weight=1)
    nlp_module = NlpModule(weight=1)

    @staticmethod
    def init_get_recommendation_code():
        request_id = str(uuid4())

        # TODO: remove mocked data - get from request
        request_code = RequestCode(query='read file',
                                   libs=['json', 'requests'],
                                   comments=['comments'],
                                   language='Python',
                                   request_id=request_id)
        data = request_code.toRequestJSON()
        RequestDB().add(request_code)
        server.get_source_codes(data=data)

    @classmethod
    def evaluate_search_codes(cls, request):
        request_json = request.get_json()
        results = request_json.get('searchResult')
        request_id = request_json.get('requestID')

        rc = RequestDB().get_request_by_id(request_id)
        request_code = RequestCode(**rc[0])
        RequestDB().remove(request_id)

        input_bus = cls.map_crawler_result(request_code, results)

        for idx, searched_code in enumerate(input_bus.searched_codes):
            for idy, code in enumerate(searched_code.codes):
                low_coupling_score = cls.low_coupling_module.evaluate_code(input_bus_vo=input_bus, search_result_id=idx,
                                                                           code_id=idy)

                understanding_score = cls.understanding_module.evaluate_code(input_bus_vo=input_bus,
                                                                             search_result_id=idx,
                                                                             code_id=idy)

                nlp_score = cls.nlp_module.evaluate_code(input_bus_vo=input_bus, search_result_id=idx,
                                                         code_id=idy)

                sum_weight = (cls.low_coupling_module.weight + cls.understanding_module.weight + cls.nlp_module.weight)
                final_score = (low_coupling_score + understanding_score + nlp_score) / sum_weight
                code.score = final_score

        # TODO: continue here => modules
        for idx, searched_code in enumerate(input_bus.searched_codes):
            for idy, code in enumerate(searched_code.codes):
                print(code.score)

    @staticmethod
    def map_crawler_result(request_code, results):
        input_bus = InputBus(user=request_code)
        for idx, result in enumerate(results):
            search_result = SearchResult(request_id=idx, source_link=result.get('url'),
                                         documentation=result.get('documentation'))

            search_result.map_from_request(input_bus=input_bus, result=result)
            input_bus.add_searched_code(search_result)

        input_bus.set_distance_min_max_lines_size()
        return input_bus

    def train_network(self, train_database):
        self.complex_network.train_network(textual_train_base=train_database)
        print(self.complex_network.adjacency_list)