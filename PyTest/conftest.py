# This is a global file which contains fixtures and should be in path where TC's are present
# This reduces no of fixtures to written in python file -> Globalised

import pytest


@pytest.fixture(scope="module")     # @pytest.fixture(scope="module")  -> This will only run once for entire test file
def beforeMethod1():
    print("This is pre defined module step which runs before any other method")

@pytest.fixture(scope="function")     # @pytest.fixture(scope="module")  -> This will only run once for entire test file
def beforeMethod2():
    print("This is pre defined function step which runs before any other method")

@pytest.fixture(scope="session")     # @pytest.fixture(scope="module")  -> This will only run once for all execution or once for a session
def beforeMethod3():
    print("This is pre defined session step which runs before any other method")
