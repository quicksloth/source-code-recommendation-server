from Modules.AbstractModule import AbstractModule
from Modules.Concepts.ComplexNetwork import ComplexNetwork
import numpy


class NlpModule(AbstractModule):
    """
        Module to extract natural language
        distance between searched code and
        documentation and user code
    """

    def __init__(self, internal_weights=None, weight=1):
        if internal_weights is None:
            internal_weights = [0.25, 0.25, 0.25, 0.25]
        AbstractModule.__init__(self, internal_weights, weight)
        self.complex_network = ComplexNetwork()
        self.clusters = self.complex_network.get_clusters_content()
        self.clustersCount = len(self.clusters)

    def __populate_histogram(self, histogram, doc):
        # Populate histogram
        words = doc.split(" ")
        for word in words:
            for i, cluster in enumerate(self.clusters):
                cluster_array = cluster.split("\t")
                if word in cluster_array:
                    histogram[i] += 1
        # Return normalized histogram
        return self.__normalize_histogram(histogram)

    @staticmethod
    def __normalize_histogram(histogram):
        histogram_sum = 0
        for value in histogram:
            histogram_sum += value
        if histogram_sum > 0:
            for i, value in enumerate(histogram):
                histogram[i] = value / histogram_sum
        return histogram

    def __evaluate_docs_distance(self, doc1, doc2):
        histogram1 = numpy.array(self.__populate_histogram([0] * self.clustersCount, doc1))
        histogram2 = numpy.array(self.__populate_histogram([0] * self.clustersCount, doc2))
        return numpy.linalg.norm(histogram1 - histogram2)

    def __evaluate_query_vs_doc(self, query, doc):
        score = 1 - self.__evaluate_docs_distance(query, doc)
        return self.internal_weights[0] * score

    def __evaluate_query_vs_comments(self, query, user_comments):
        grouped_comments = " ".join(user_comments)
        score = 1 - self.__evaluate_docs_distance(query, grouped_comments)
        return self.internal_weights[1] * score

    def __evaluate_comments_vs_comments(self, user_comments, code_comments):
        grouped_user_comments = " ".join(user_comments)
        grouped_code_comments = " ".join(code_comments)
        #print(grouped_code_comments)
        #print(grouped_user_comments)
        score = 1 - self.__evaluate_docs_distance(grouped_user_comments, grouped_code_comments)
        print("comments vs comments", score)
        return self.internal_weights[2] * score

    def __evaluate_comments_vs_doc(self, user_comments, doc):
        print("qty", self.clustersCount)
        grouped_user_comments = " ".join(user_comments)
        score = 1 - self.__evaluate_docs_distance(grouped_user_comments, doc)
        return self.internal_weights[3] * score

    def evaluate_code(self, input_bus_vo, search_result_id, code_id):
        score = 0
        # Search Query vs Doc
        score += self.__evaluate_query_vs_doc(input_bus_vo.user.query,
                                              input_bus_vo.searched_codes[search_result_id].documentation)
        # Search Query vs Comments
        score += self.__evaluate_query_vs_comments(input_bus_vo.user.query,
                                                   input_bus_vo.searched_codes[search_result_id].codes[
                                                       code_id].comments)
        # User Comments vs Doc
        score += self.__evaluate_comments_vs_doc(input_bus_vo.user.comments,
                                                 input_bus_vo.searched_codes[search_result_id].documentation)
        # User Comments vs Comments
        score += self.__evaluate_comments_vs_comments(input_bus_vo.user.comments,
                                                      input_bus_vo.searched_codes[search_result_id].codes[
                                                          code_id].comments)

        return self.weight * score
