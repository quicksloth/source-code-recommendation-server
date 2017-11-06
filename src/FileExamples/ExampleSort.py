import os
import pickle
import numpy

dirname = os.path.dirname(os.path.abspath(__file__))


class MyProjectObjectList(object):
    """
       MyProjectObject is a class that groups all data needed:
       it's possible to get:
        - sort object by id
        - get all data from file
    """

    file = os.path.join(dirname, "project_object.pickle")

    def __init__(self, list=None):
        if list is None:
            list = []

        self.list = list

    def __load_file(self, filename=None):
        """Load file"""
        pfile = open((filename or self.file), 'rb+')

    def __save_file(self, filename=None):
        """Save file"""
        pfile = open((filename or self.file), 'wb+')
        pickle.dump(self.list, pfile)

    def __reading_file(self):
        # Return a file with list of lines
























