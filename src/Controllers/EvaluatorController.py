import sys
import os

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
        return []

t = EvaluatorController()
print(t.init_get_recommendation_code())
