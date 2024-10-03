"""
[enter well-formed module docstring]
"""

from programming_languages import ProgrammingLanguages


def test_find_langauges_2_2_1():
    """
    Test constructor with two programmers, 1st with 2 programming langauges,
    2nd programmer with 1 programmin glangauge
    """
    programmers = ["Bill", "Joan"]
    languages = [["C++", "Python"], ["C++"]]

    language_obj = ProgrammingLanguages(programmers, languages)

    expected = ["C++", "Python"]
    actual = language_obj.find_languages("Bill")

    assert expected == actual
