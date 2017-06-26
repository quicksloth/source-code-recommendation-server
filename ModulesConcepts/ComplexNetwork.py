class ComplexNetwork(object):
    """A words ComplexNetwork build by sites text about computer science and programming.
        This will be used to measure words contextual distance.
    Static Attribute:
        complex_network_file
    Attributes:
        textual_train_base: A array of strings to train complex network based on co-occurrence
    """
    complex_network_file = "data_complex_network.npy"
    adjacency_list = dict([])

    def __init__(self, textual_train_base):
        # TODO if textual_train_base is empty : load save complex network by file *data_complex_network.npy*
        self.textual_train_base = textual_train_base

    def __load_complex_network(self):
        """Returns the ComplexNetwork data loaded by a file"""
        return self.complex_network_file

    def __save_complex_network(self):
        """Save ComplexNetwork data into a file and returns the data"""
        return self.complex_network_file

    def train_network(self):
        """Create structure and train ComplexNetwork based on textual_train_base"""
        return self.textual_train_base

    def get_contextual_distance(self, one_word, second_word):
        """Create structure and train ComplexNetwork based on textual_train_base"""
        print(self.adjacency_list)
        print(one_word)
        print(second_word)
        return 0.3
