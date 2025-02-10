import pytest
from sqlalchemy.testing import fixture


@pytest.fixture  # @pytest.fixture -> This runs before methods if the method name under this tag is assigned as parameter to other method name
def beforeMethod():
    print("This is pre defined step which runs before any other method")

@pytest.fixture(scope="module")     # @pytest.fixture(scope="module")  -> This will only run once for entire test file
def beforeMethod1():
    print("This is pre defined module step which runs before any other method")
    return "true"

@pytest.fixture(scope="function")     # @pytest.fixture(scope="module")  -> This will only run for each test file
def beforeMethod2():
    print("This is pre defined function step which runs before any other method")
    yield                             # Yield statement will not allow to execute statement mentioned below it, implemented in line 37
    print("This YIELD statement is skipped")

@pytest.fixture(scope="class")     # @pytest.fixture(scope="module")  -> This will only run once for entire test file
def beforeMethod3():
    print("This is pre defined class step which runs before any other method")

def test_initialCheck(beforeMethod):  # When we start method name as test -> then it understands the method as Pytest
    print("This is first test")

def test_initialCheck1(beforeMethod):
    print("This is second test")

def test_initialCheck2(beforeMethod1):
    print("This is third test")
    assert beforeMethod1 == "true"

def test_initialCheck3(beforeMethod1):
    print("This is fourth test")

def test_initialCheck4(beforeMethod1, beforeMethod2):
    print("This is fifth test")
    assert beforeMethod1 == "true"

def test_initialCheck5(beforeMethod2):
    print("This is sixth test")

def test_initialCheck6(beforeMethod3):
    print("This is seventh test")

def test_initialCheck7(beforeMethod3):
    print("This is eightth test")

