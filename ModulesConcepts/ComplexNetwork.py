class ComplexNetwork(object):
    """A ComplexNetwork of Words build by sites text about computer science and programming.
        This will be used to measure words contextual distance.
    Static Attribute:
        complex_network_file
    Attributes:
        textual_train_base: A array of strings to train complex network based on co-occurrence
    """
    complex_network_file = "adjacency_list_complex_network.npy"
    default_weight = 1

    def __init__(self):
        # TODO fix this logic => continous training
        self.adjacency_list = dict([])

    def __load_complex_network(self):
        """Returns the ComplexNetwork data loaded by a file"""
        return self.complex_network_file

    def __save_complex_network(self):
        """Save ComplexNetwork data into a file and returns the data"""
        return self.complex_network_file

    def train_network(self, textual_train_base):
        """Create structure and train ComplexNetwork based on textual_train_base
        Returns trained """

        for doc in textual_train_base:
            words = doc.split()
            for idx, word in enumerate(words):
                # TODO parametrize co-occurrence (numbers)
                if idx + 1 == len(words):
                    break
                next_word = words[idx + 1].lower()
                current_word = word.lower()

                if current_word in self.adjacency_list.keys():
                    if next_word in self.adjacency_list[current_word].keys():
                        self.adjacency_list[current_word][next_word] += self.default_weight
                    else:
                        self.adjacency_list[current_word][next_word] = self.default_weight
                else:
                    self.adjacency_list[current_word] = {next_word: self.default_weight}

        print self.adjacency_list
        return self.adjacency_list

    def get_contextual_distance(self, one_word, second_word):
        """Create structure and train ComplexNetwork based on textual_train_base"""
        # print len(self.adjacency_list['lorem'])
        print(self.adjacency_list)
        print(one_word)
        print(second_word)
        return 0.3


t1 = 'Lorem ipsum dolor Lorem Lorem sit amet Nullam metus.'
t2 = 'Lorem ipsum sit Consectetur sit adipiscing sit elit.'
textual = [t1, t2]
cn = ComplexNetwork()
cn_al = cn.train_network(textual_train_base=textual)
print len(cn_al)

textual = ["bla ble bli blo bu", "la le li lo lu"]
cn_al = cn.train_network(textual_train_base=textual)
print  len(cn_al)
