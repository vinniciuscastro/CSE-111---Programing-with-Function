# Vinnicius Castro
# Jan 30th 2023 

from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Vinnicius", "Castro") == "Castro; Vinnicius"
    assert make_full_name("Marie", "Toussaint") == "Toussaint; Marie"
    assert make_full_name("Oliver", "Toussaint") == "Toussaint; Oliver"

def test_extract_family_name():
    assert extract_family_name("Castro; Vinnicius") == "Castro"
    assert extract_family_name("Toussaint; Marie") == "Toussaint"
    assert extract_family_name("Toussaint; Oliver") == "Toussaint"
def test_extract_given_name():
    assert extract_given_name("Castro; Vinnicius") == "Vinnicius"
    assert extract_given_name("Toussaint; Marie") == "Toussaint"
    assert extract_given_name("Toussaint; Oliver") == "Toussaint"






# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])