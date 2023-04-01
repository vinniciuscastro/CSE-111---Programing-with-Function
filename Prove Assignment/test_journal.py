# Vinnicius Castro
# March 29th 2023
import pytest
from journal import  welcome, questions


def test_welcome():
    # Test if the function returns a string
    assert welcome() == "Welcome to your Journal"


def test_questions():
    # Test if the function returns a list
    assert isinstance(questions(), list)

pytest.main(["-v", "--tb=line", "-rN", __file__])