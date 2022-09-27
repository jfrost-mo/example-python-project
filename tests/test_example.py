# Import your code the same as any other package.
import Example.example as exmpl


# Tests are functions starting in test_*
def test_is_even():
    assert exmpl.is_even(10)
    # Assert condition must end up True
    assert not exmpl.is_even(5)


def test_add_one():
    assert exmpl.add_one(7) == 8
    # Can test function multiple times with different values
    assert exmpl.add_one(-1) == 0


def test_truthyness():
    # Test functions don't need to be inside classes
    truthy_var = 1
    assert truthy_var == True


def test_failing():
    # Assert that evaluates to false counts as a test failure
    assert 3 == 3
