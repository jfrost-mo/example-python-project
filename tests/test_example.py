import Example.example as exmpl


def test_add_one():
    assert exmpl.add_one(7) == 8
    assert exmpl.add_one(-1) == 0


def test_is_even():
    assert exmpl.is_even(10)
    assert not exmpl.is_even(5)


def test_failing():
    assert 3 == 3
