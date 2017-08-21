import numpy as np


class ComplexNetwork(object):
    """A ComplexNetwork of Words build by sites text about computer science and programming.
        This will be used to measure words contextual distance.
    Static Attribute:
        complex_network_file
    Attributes:
        textual_train_base: A array of strings to train complex network based on co-occurrence
    """
    complex_network_file = "adjacency_list_complex_network.npy"
    complex_network_file_last_version = "adjacency_list_complex_network_last_version.npy"
    default_weight = 1
    neighbor_distance = 1

    def __init__(self):
        self.adjacency_list = dict([])

    def __load_complex_network(self, filename=None):
        """Load complex network by file"""
        np_file = open(filename or self.complex_network_filee, 'r')
        self.adjacency_list = np.load(np_file)

    def __save_complex_network(self, filename=None):
        """Save complex network by file"""
        np_file = open(filename or self.complex_network_file, 'w')
        np.save(np_file, self.adjacency_list)

    def train_network(self, textual_train_base):
        """
        Train ComplexNetwork based on textual_train_base:
        extract co-occurrence in Nth neighbor (neighbor_distance)
        of all words of all strings in array
        At the end, save CcomplexNetwork.
        """
        # TODO fix logic of saving
        self.__save_complex_network(filename=self.complex_network_file_last_version)

        for doc in textual_train_base:
            words = doc.split()
            for idx, word in enumerate(words):
                if idx + 1 == len(words):
                    break

                for neighbor in range(1, self.neighbor_distance + 1):
                    # TODO improve this logic inside range
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
        # print self.adjacency_list
        return self.adjacency_list

    def get_contextual_distance(self, one_word, second_word):
        """Get distance between one_word to another (second_word) """
        one_word = one_word.lower()
        second_word = second_word.lower()
        if one_word in self.adjacency_list.keys() \
                and second_word in self.adjacency_list[one_word].keys():
            return 1.0 / self.adjacency_list[one_word][second_word]
        else:
            return 0


# TESTING COMPLEX NETWORK class -------
t1 = 'Lorem ipsum dolor Lorem Lorem sit amet Nullam metus.'
t2 = 'Lorem ipsum sit Consectetur sit adipiscing sit elit.'
textual = [t1, t2]
cn = ComplexNetwork()
cn_al = cn.train_network(textual_train_base=textual)
# print len(cn_al)

textual = ["bla ble bli blo bu", "la le li lo lu"]
cn_al = cn.train_network(textual_train_base=textual)
# print len(cn_al)

# print cn.get_contextual_distance(one_word='dolor', second_word='Lorem')

# cn.save_complex_network()
# print cn.adjacency_list
# cn.load_complex_network()
# print cn.adjacency_list
