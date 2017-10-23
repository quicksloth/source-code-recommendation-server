from Modules.AbstractModule import AbstractModule
from Modules.Concepts.ComplexNetwork import ComplexNetwork
import numpy

class NlpModule(AbstractModule):
    """
        Module to extract natural language
        distance between searched code and
        documentation and user code
    """
    def __init__(self, internal_weights=[0.25, 0.25, 0.25, 0.25], weight=1):
        AbstractModule.__init__(self, internal_weights, weight)
        self.complex_network = ComplexNetwork()
        self.clusters = self.complex_network.get_clusters_content()
        self.clustersCount = len(self.clusters)

    def populate_histogram(self, histogram, doc):
        # Populate histogram
        words = doc.split(" ")
        for word in words:
            for i, cluster in enumerate(self.clusters):
                clusterArray = cluster.split("\t")
                if word in clusterArray:
                    histogram[i] += 1
        # Normalize Histogram
        histogramSum = 0
        for value in histogram:
            histogramSum += value
        for i, value in enumerate(histogram):
            histogram[i] = value/histogramSum
        return histogram

    def evaluate_docs_distance(self, doc1, doc2):
        histogram1 = self.populate_histogram([0] * self.clustersCount, doc1)
        histogram2 = self.populate_histogram([0] * self.clustersCount, doc2)
        return numpy.linalg.norm(numpy.array(histogram1) - numpy.array(histogram2))

    def evaluate_query_vs_doc(self, query, doc):
        score = 1 - self.evaluate_docs_distance(query, doc)
        return self.internal_weights[0] * score

    def evaluate_query_vs_comments(self, query, user_comments):
        groupedComments = user_comments.join(" ")
        score = 1 - self.evaluate_docs_distance(query, groupedComments)
        return self.internal_weights[1] * score

    def evaluate_comments_vs_comments(self, user_comments, code_comments):
        grouped_user_comments = user_comments.join(" ")
        grouped_code_comments = code_comments.join(" ")
        score = 1 - self.evaluate_docs_distance(grouped_user_comments, grouped_code_comments)
        return self.internal_weights[2] * score

    def evaluate_comments_vs_doc(self, user_comments, doc):
        grouped_user_comments = user_comments.join(" ")
        score = 1 - self.evaluate_docs_distance(grouped_user_comments, doc)
        return self.internal_weights[3] * score

    def evaluate_code(self, input_bus_vo, search_result_id, code_id):
        score = 0
        # Search Query vs Doc
        score += self.evaluate_query_vs_doc(input_bus_vo.user.query,
                                   input_bus_vo.searched_codes[search_result_id].documentation)
        # Search Query vs Comments
        score += self.evaluate_query_vs_comments(input_bus_vo.user.query,
                                        input_bus_vo.searched_codes[search_result_id].codes[code_id].comments)
        # User Comments vs Doc
        score += self.evaluate_comments_vs_doc(input_bus_vo.user.comments,
                                           input_bus_vo.searched_codes[search_result_id].documentation)
        # User Comments vs Comments
        score += self.evaluate_comments_vs_comments(input_bus_vo.user.comments,
                                           input_bus_vo.searched_codes[search_result_id].codes[code_id].comments)

        return self.weight * score
