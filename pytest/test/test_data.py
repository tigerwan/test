import pytest

@pytest.fixture
def data1():
    return {'a':'a'}
    
@pytest.fixture
def data2():
    return {'b':'b'}