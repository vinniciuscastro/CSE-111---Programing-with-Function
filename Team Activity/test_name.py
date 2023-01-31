# Vinnicius Castro
# Jan 30th 2023 

from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    pass

def test_extract_family_name():
    pass
def test_extract_given_name():
    pass





# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])