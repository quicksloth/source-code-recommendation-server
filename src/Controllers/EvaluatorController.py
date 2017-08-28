import os
import sys

# TODO: try to find another way to solve this problem
# issue 12 https://github.com/quicksloth/source-code-recommendation-server/issues/11
# Necessary to import modules in the same level
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
        if len(rc) == 1:
            request_code = RequestCode(**rc[0])
            input_bus = InputBus(user=request_code)
            print(input_bus.user.__dict__)
