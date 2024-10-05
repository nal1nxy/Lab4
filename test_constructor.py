"""
Practice with the dictionary built-in data type.

File: test_constructor.py
Initial developers: COMP 801 instructors
Developer: Nalin
Collaborator(s): Olivia
Date:
"""
from programming_languages import ProgrammingLanguages
import pytest

def test_constructor_2_2_1():
    """
    Test constructor with two programmers, 1st with 2 programming langauges,
    2nd programmer with 1 programming langauge
    """
    programmers = ['Bill', 'Joan']
    languages = [['C++', 'Python'], ['C++']]

    pl_obj = ProgrammingLanguages(programmers, languages)

    actual_p = pl_obj.programmers
    expected_p = {"Bill": ["C++", "Python"], "Joan": ["C++"]}
    actual_l = pl_obj.languages
    expected_l = {"C++": ["Bill", "Joan"], "Python": ["Bill"]}
    actual = (actual_p, actual_l)
    expected = (expected_p, expected_l)
    assert actual == expected


def test_constructor_2_2_2():
    """
    Test constructor with two programmers, 1st with 2 programming langauges,
    2nd programmer with 1 programming langauge
    """
    programmers = ['Nalin', 'Kumar', 'Yetukuri']
    languages = [['C#', 'Python'], ['C++'], ['C']]

    pl_obj = ProgrammingLanguages(programmers, languages)

    actual_p = pl_obj.programmers
    expected_p = {"Nalin": ["C#", "Python"], "Kumar": ["C++"], "Yetukuri": ["C"]}
    actual_l = pl_obj.languages
    expected_l = {"C++": ["Kumar"], "Python": ["Nalin"], "C#": ["Nalin"], "C": ["Yetukuri"]}
    actual = (actual_p, actual_l)
    expected = (expected_p, expected_l)
    assert actual == expected


pytest.main()