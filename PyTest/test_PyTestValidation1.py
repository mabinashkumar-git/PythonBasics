import pytest
from sqlalchemy.testing import fixture


def test_initialCheck(beforeMethod1):  # When we start method name as test -> then it understands the method as Pytest
    print("This is first test")

def test_initialCheck1(beforeMethod1):
    print("This is second test")

def test_initialCheck4(beforeMethod2):
    print("This is fifth test")

def test_initialCheck5(beforeMethod2):
    print("This is sixth test")

def test_initialCheck6(beforeMethod3):
    print("This is seventh test")

def test_initialCheck7(beforeMethod3):
    print("This is eight test")
