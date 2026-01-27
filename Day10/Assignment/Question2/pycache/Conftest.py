
import pytest


@pytest.fixture(scope="function")
def sample_numbers():
    return (3,2)

@pytest.fixture(scope="module")
def calculator_resource():
    print("\n Connecting to calculator resource")
    yield "calculator ready"
    print("\n Disconnecting calculator resource")
