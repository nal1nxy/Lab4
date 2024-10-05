"""
Practice with the dictionary built-in data type.

File: test_find_programmers.py
Initial developers: COMP 801 instructors
Developer: Nalin
Collaborator(s): Olivia
Date:
"""
from programming_languages import ProgrammingLanguages


def test_find_programmers_2_3_1():
    """
    Test the method find_programmer with a language as input.
    """
    language = "C#"
    programmers = ['Nalin', 'Kumar', 'Yetukuri']
    languages = [['C#', 'Python'], ['C++'], ['C']]
    pl = ProgrammingLanguages(programmers, languages)
    actual = pl.find_programmers(language)
    expected = ['Nalin']
    assert actual == expected


def test_find_programmers_2_3_2():
    """
    Test the method find_programmer with a language as input.
    """
    language = "C"
    programmers = ['Nalin', 'Kumar', 'Yetukuri']
    languages = [['C#', 'Python'], ['C++', 'C#'], ['C']]
    pl = ProgrammingLanguages(programmers, languages)
    actual = pl.find_programmers(language)
    expected = ['Yetukuri']
    assert actual == expected
