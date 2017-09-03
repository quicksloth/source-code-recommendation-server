# import numpy as np
import pickle


def get_contextual_distance(one_word, second_word):
    return 1


class ComplexNetwork(object):
    """A ComplexNetwork of Words build by sites text about computer science and programming.
        This will be used to measure words contextual distance.
    Static Attribute:
        complex_network_file
    Attributes:
        textual_train_base: A array of strings to train complex network based on co-occurrence
    """
    complex_network_file = "adjacency_list_complex_network.pickle"
    complex_network_file_last_version = "adjacency_list_complex_network_last_version.pickle"
    default_weight = 1
    neighbor_distance = 1

    def __init__(self):
        self.adjacency_list = dict([])
        self.load_complex_network()

    def load_complex_network(self, filename=None):
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
            pfile = open((filename or self.complex_network_file), 'wb+')
            pickle.dump(self.adjacency_list, pfile)
        except:
            print('error in dump dict')

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
        return self.adjacency_list

    # TODO: use this one function when complex network it's ok
    def get_contextual_distance_right(self, one_word, second_word):
        """Get distance between one_word to another (second_word) """
        one_word = one_word.lower()
        second_word = second_word.lower()
        if one_word in self.adjacency_list.keys() \
                and second_word in self.adjacency_list[one_word].keys():
            return 1.0 / self.adjacency_list[one_word][second_word]
        else:
            return 0

    def get_contextual_distance(self):
        return 1


# TESTING COMPLEX NETWORK class -------
t1 = 'Lorem ipsum dolor Lorem Lorem sit amet Nullam metus.'
t2 = 'Lorem ipsum sit Consectetur sit adipiscing sit elit.'
textual = [t1, t2]
cn = ComplexNetwork()
# print(len(cn_al))

# textual = ["bla ble bli blo bu", "la le li lo lu"]
# cn_al = cn.train_network(textual_train_base=textual)
# print len(cn_al)

# print cn.get_contextual_distance(one_word='dolor', second_word='Lorem')

# cn.save_complex_network()
# print cn.adjacency_list
cn.load_complex_network()
cn_al = cn.train_network(textual_train_base=textual)
# print(cn.adjacency_list)
