import sys
import os

# TODO: try to find another way to solve this problem
# issue 12 https://github.com/quicksloth/source-code-recommendation-server/issues/11
# Necessary to import modules in the same level
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import server
from uuid import uuid4
from Models.RequestCode import RequestCode

rc = RequestCode(query='read file', libs=['os'], comments=['comments'], language='Python')


class EvaluatorController(object):
    """
        Controller of the evaluator model
    """

    modules_weights = []

    # modules = [Controllers.t([1], 1)]

    @staticmethod
    def init_get_recommendation_code():
        request_id = str(uuid4())
        data = rc.toRequestJSON(str(request_id))
        server.get_source_codes(data=data)

    @staticmethod
    def evaluate_search_codes(request):
        print('test')
        # print(request.__dict__)
        print(request.is_json)
        # print(request.json)
        request_json = request.get_json()
        print(request_json)
        print(request_json.get('clientID'))
        print(request_json.get('searchResult'))

