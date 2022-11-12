import pytest


@pytest.fixture(scope="module")
def module_fixture():
    return "Author : Nandhini"


def test_import():
    import vocably
    assert vocably.__version__ == "0.0.8"
