import pytest
from calculator import add,subtract,divide
from check_palindrome import check_palindrome
def test_add():
    assert add(2,3)==5
def test_subtract():
    assert subtract(10,4)==6
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)
@pytest.mark.parametrize(
    "strs,expected",[
        ("amit",False),
        ("nitin",True)
    ]
)
def test_palindrome(strs,expected):
    assert check_palindrome(strs)==expected
