import os
import pickle
import numpy

dirname = os.path.dirname(os.path.abspath(__file__))


class ComplexNetwork(object):
    """A ComplexNetwork of Words build by sites text about computer science and programming.
        This will be used to measure words contextual distance.
    Static Attribute:
        complex_network_file
    Attributes:
        textual_train_base: A array of strings to train complex network based on co-occurrence
    """
    complex_network_file = os.path.join(dirname, "adjacency_list_complex_network.pickle")
    # complex_network_file_last_version = os.path.join(dirname, "adjacency_list_complex_network_last_version.pickle")

    mcl_file_input = os.path.join(dirname, "mcl_input.txt")
    mcl_file_output = os.path.join(dirname, "mcl_output.txt")

    default_weight = 1
    neighbor_distance = 1

    def __init__(self):
        self.adjacency_list = dict([])
        self.cluster_list = dict([])
        self.cluster_count = 0
        self.__load_clusters()
        # self.load_complex_network()

    def __load_complex_network(self, filename=None):
        """Load complex network by file"""
        try:
            pfile = open((filename or self.complex_network_file), 'rb+')
            self.adjacency_list = pickle.load(pfile)
        except:
            print('create new empty file')
            self.__save_complex_network(filename=filename)

    def __save_complex_network(self, filename=None):
        """Save complex network by file"""
        try:
            # Save complex network on original format
            pfile = open((filename or self.complex_network_file), 'wb+')
            pickle.dump(self.adjacency_list, pfile)
        except:
            print('error in dump dict')

    def __save_mcl_input_data(self, filename=None):
        """Save mcl input data in file"""
        try:
            # Save complex network on MCL format
            mcl_input = open(filename or self.mcl_file_input, 'w')
            for first_word in self.adjacency_list:
                for second_word in self.adjacency_list[first_word]:
                    line = first_word + " " + second_word + " " + \
                           str(self.adjacency_list[first_word][second_word]) + "\n"
                    mcl_input.write(line)
            mcl_input.close()
        except:
            print('error saving mcl input data')

    def __run_mcl(self):
        """run mcl in terminal to get clustered words"""
        try:
            command = "mcl " + self.mcl_file_input + " --abc -o " + self.mcl_file_output
            os.system(command)
            print("MCL run success")
        except:
            print("Error while running MCL")

    def train_network(self, textual_train_base):
        """
        Train ComplexNetwork based on textual_train_base:
        extract co-occurrence in Nth neighbor (neighbor_distance)
        of all words of all strings in array
        At the end, save CcomplexNetwork.
        """
        # self.__save_complex_network(filename=self.complex_network_file_last_version)
        self.__load_complex_network()

        for doc in textual_train_base:
            words = doc.split()
            for idx, word in enumerate(words):
                if idx + 1 == len(words):
                    break

                for neighbor in range(1, self.neighbor_distance + 1):
                    if idx + neighbor == len(words):
                        break

                    next_word = words[idx + neighbor].lower()
                    current_word = word.lower()

                    if current_word in self.adjacency_list.keys():
                        if next_word in self.adjacency_list[current_word].keys():
                            self.adjacency_list[current_word][next_word] += self.default_weight
                        else:
                            self.adjacency_list[current_word][next_word] = self.default_weight
                    else:
                        self.adjacency_list[current_word] = {next_word: self.default_weight}

        self.__save_complex_network()
        self.__save_mcl_input_data()
        self.__run_mcl()

        return self.adjacency_list

    def get_clusters_content(self):
        with open(self.mcl_file_output, "r") as mcl_file:
            return mcl_file.read().split("\n")

    def __load_clusters(self):
        print('loading complex network (clusters)....')
        clusters_content = self.get_clusters_content()
        self.cluster_count = len(clusters_content)
        for idx, cluster in enumerate(clusters_content):
            words_cluster = cluster.split("\t")
            for word in words_cluster:
                self.cluster_list[word] = idx
        print('Complex Network Loaded')

    def get_doc_cluster_histogram(self, doc):
        # print(self.cluster_count)
        histogram = [0] * self.cluster_count
        cluster_words_count = 0

        for word in doc.split():
            # print(word)
            if word in self.cluster_list.keys():
                # print('has word = ', word)
                # print('has word', word, 'in cluster', self.cluster_list[word])
                # print('histogram in position before', histogram[self.cluster_list[word]])
                histogram[self.cluster_list[word]] += 1
                # print('histogram in position after', histogram[self.cluster_list[word]])
                cluster_words_count += 1

        # print(histogram)
        normalized_histogram = self.normalize_doc_cluster_histogram(histogram, cluster_words_count)
        # print(normalized_histogram)
        return normalized_histogram

    @staticmethod
    def normalize_doc_cluster_histogram(histogram, cluster_words_count):
        if cluster_words_count <= 0:
            return histogram

        for idx, value in enumerate(histogram):
            histogram[idx] = value / cluster_words_count
        return histogram

    def get_contextual_distance_between_docs(self, first_doc, second_doc):
        """ get euclidean distance between two non empty docs """
        if first_doc == '' or second_doc == '':
            return 1

        histogram_doc1 = numpy.array(self.get_doc_cluster_histogram(first_doc))
        histogram_doc2 = numpy.array(self.get_doc_cluster_histogram(second_doc))
        # print('histogram_doc1', histogram_doc1)
        # print('histogram_doc2', histogram_doc2)
        return numpy.linalg.norm(histogram_doc1 - histogram_doc2)

# TESTING COMPLEX NETWORK class -------
# t1 = 'Lorem ipsum dolor Lorem Lorem sit amet Nullam metus.'
# t2 = 'Lorem ipsum sit Consectetur sit adipiscing sit elit.'
# textual = [t1, t2]
# print(len(cn_al))
# textual = ["bla ble bli blo bu", "la le li lo lu"]
# cn_al = cn.train_network(textual_train_base=textual)
# print len(cn_al)
# print cn.get_contextual_distance(one_word='dolor', second_word='Lorem')
# cn.save_complex_network()
# print cn.adjacency_list
# cn.load_complex_network()
# cn_al = cn.train_network(textual_train_base=textual)
# print(cn.adjacency_list)

# cn = ComplexNetwork()
#
# doc = 'open source web pages github read file pages'
# doc2 = 'open'
#
# print('cn.get_contextual_distance_between_docs =', cn.get_contextual_distance_between_docs(doc, doc2))
