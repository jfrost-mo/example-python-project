# Import your code the same as any other package.
import Example.example as exmpl


# Tests are functions starting in test_*
def test_simple():
    seven = 7
    assert seven == 7


def test_is_even():
    assert exmpl.is_even(10)
    # Assert condition must end up True
    assert not exmpl.is_even(5)


def test_add_one():
    assert exmpl.add_one(7) == 8
    # Can test function multiple times with different values
    assert exmpl.add_one(-1) == 0
