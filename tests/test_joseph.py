from josephtest import hello
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ('A', 'hello A'),
    ('B', 'hello B'),
    ('Joseph', 'hello Joseph'),
])
def test_hello(test_input, expected):
    assert hello(test_input) == expected
# @pytest.mark.skip(reason="Something not support for this test?")

# @pytest.mark.xfail #(Expected fail)
# def test_devided_by_zero()
#    assert 1/0 == 1

# @pytest.fixture(scope="session")  #Conf for testing database connection
# def db_conn():
#   db=....
#   url = ...
#   with db.connection(url) as conn:
#       yield conn

# def test_db_hello(db_conn):
#     db_conn.read_func()
#     assert ...
