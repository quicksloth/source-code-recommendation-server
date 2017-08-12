from Evaluator.Modules.LowCouplingModule import LowCouplingModule


class EvaluatorController(object):
    """
        Controller of the evaluator model
    """

    modules_weights = []
    modules = [LowCouplingModule([1], 1)]


t = EvaluatorController()
print t.modules
