"""
Practice with the dictionary built-in data type.

File: programming_languages.py
Initial developers: COMP 801 instructors
Developer: Nalin
Collaborator(s): Olivia
Date:
"""


class ProgrammingLanguages:
    """
    Represents a mapping of programmers and the languages
    in which they are proficient.
    """

    def __init__(self, programmers, languages):
        """
        Create ProgrammingLanguages object.

        Attribute: self.languages: dictionary
            keys: strings, represent programming languages.
            values: list of strings programmers proficient in the
            language.

            e.g.: { "C++" : ["Bill", "Joan"], "Python" : ...}

        Attribute: self.programmers: dictionary
            keys: strings, represent programmer names.
            values: list of strings representing languages
            in which the programmer is proficient.

            e.g.: { "Bill" : ["C++", "Python"], "Joan" : ...}

        :param programmers: list of strings representating programmer names,
            e.g., ['Bill', 'Joan'].
            This list is parallel with `languages`: has the same size and its
            items correspond to `languages` items by position.
        :param languages: list of sublists, where a sublist is a list of
            strings representing course programming languages
                [['C++', 'Python'], ['C++']]
        Implemenation requirement: We consider ONLY "happy path" cases.
        Parameters `programmers` and `languages` receive non-empty arguments
        that have types and values as specified in the docstring, and meet the
        "parallelism" requirement.
        """

        self.languages = {}
        self.programmers = {}
        index = 0
        for programmer in programmers:
            self.programmers[programmer] = languages[index]
            for language in languages[index]:
                if language not in self.languages:
                    self.languages[language] = []
                self.languages[language] = self.languages[language]+[programmer]
            index = index + 1

    def find_programmers(self, language):
        """
        :param language: a programming language in the form of a string.
        :return: a list of programmers proficient in the input language
        """
        list_of_programmers = self.languages[language]
        return [list_of_programmers]  # stub

    def find_languages(self, programmer):
        """
        :param programmer: a programmer's name in the form of a string.
        :return: a list languages in which the programmer is proficient.
        """
        list_of_languages = self.programmers[programmer]
        return [list_of_languages]  # stub
