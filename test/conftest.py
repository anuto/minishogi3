import pytest
from Utils import *

@pytest.fixture
def utils():
    return Utils

pytest_plugins = [
    "Utils"
]