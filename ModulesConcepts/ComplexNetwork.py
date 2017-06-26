class ComplexNetwork(object):
    """A words ComplexNetwork build by sites text about computer science and programming.
        This will be used to measure words contextual distance.
    Static Attribute:
        complex_network_file
    Attributes:
        textual_train_base: A array of strings to train complex network based on co-occurrence
    """
    complex_network_file = "adjacency_list_complex_network.npy"
    adjacency_list = dict([])

    def __init__(self, textual_train_base):
        # TODO if textual_train_base is empty : load save complex network by file *adjacency_list_complex_network.npy*
        if textual_train_base:
            self.textual_train_base = textual_train_base
            self.train_network()
            self.__save_complex_network()
        else:
            self.__load_complex_network()

    def __load_complex_network(self):
        """Returns the ComplexNetwork data loaded by a file"""
        return self.complex_network_file

    def __save_complex_network(self):
        """Save ComplexNetwork data into a file and returns the data"""
        return self.complex_network_file

    def train_network(self):
        """Create structure and train ComplexNetwork based on textual_train_base
        Returns trained """

        for doc in self.textual_train_base:
            print doc
            words = doc.split()
            for idx, word in enumerate(words):
                if idx+1 == len(words):
                    break
                next_word = words[idx + 1]
                self.adjacency_list[word, next_word] = self.adjacency_list[word, next_word]+1\
                    if (word, next_word) in self.adjacency_list.keys()\
                    else 1

        print self.adjacency_list
        return self.adjacency_list

    def get_contextual_distance(self, one_word, second_word):
        """Create structure and train ComplexNetwork based on textual_train_base"""
        print(self.adjacency_list)
        print(one_word)
        print(second_word)
        return 0.3

t1 = 'Lorem ipsum dolor sit amet Nullam metus.'
t2 = 'Lorem ipsum Consectetur adipiscing elit.'
textual = [t1, t2]
ComplexNetwork(textual_train_base=textual)
