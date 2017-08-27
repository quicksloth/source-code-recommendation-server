# from src.Modules.LowCouplingModule import LowCouplingModule
import server

# TODO search how to import from another folder in the same level

class EvaluatorController(object):
    """
        Controller of the evaluator model
    """

    modules_weights = []

    # modules = [Controllers.t([1], 1)]

    def evaluate_all_code(self):
        server.get_source_codes()
        return []

# t = EvaluatorController()
# print t.modules
