import pytest
@pytest.yield_fixture()
def setup():
    print('BEFORE EACH the methods....')
    yield
    print('after EACH test!')

def test1(setup):
    print('test1...')

def test2(setup):
    print('Test2....')

