
import logging

# Cryptographically secure random ... just because :)
from random import SystemRandom


logging.basicConfig(level=logging.INFO)


class Engine(object):

    """
    Takes a path to a file that has a list of names (one name per line) and splits the names into groups with the
    specified size. It does this randomly.
    """

    def __init__(self, file_path, group_size=4):

        if not file_path:
            raise AttributeError("A file path is required.")

        self.file_path = file_path
        self.group_size = group_size

        self.names = self.load_names(self.file_path)

    def load_names(self, file_path):
        """
        Loads the data from a filepath -- does not parse them.
        :param file_path: string
        :return: file data: string
        """
        if not file_path:
            raise AttributeError("A file path is required.")

        with open(file_path, 'r') as f:
            name_data = f.read()

        names_list = self.parse_names(name_data)

        logging.info('{} names loaded'.format(len(names_list)))
        return names_list

    def parse_names(self, name_data):
        """
        Parses the name data string and returns a list of names
        :param name_data: string
        :return: list of names: list
        """
        if not name_data:
            raise AttributeError("No name data specified, or empty list.")

        name_data = str(name_data)
        name_list = name_data.split("\n")

        return name_list

    def generate_groups(self):
        """
        Generates the groups based on a randomization algorithm.
        :return: the generated groups: a list of lists (names)
        """

        if not self.names:
            raise AttributeError("Could not find names list. Try re-initializing Engine with valid filepath.")

        groups = []

        cryptogen = SystemRandom()
        cryptogen.shuffle(self.names)

        current_group = []
        for name in self.names:

            current_group.append(name)

            is_last_name = self.names.index(name) == len(self.names) - 1
            is_group_full = len(current_group) == self.group_size

            if is_group_full or is_last_name:
                groups.append(current_group)
                current_group = []

        logging.info("Created {} groups with max size {}.".format(len(groups), self.group_size))

        return groups

    def nice_print_groups(self, groups):
        """
        Print the groups nicely
        :param groups: list of lists
        :return:
        """

        print "-" * 20
        for group in groups:
            for name in group:
                print name
            print "-" * 20




