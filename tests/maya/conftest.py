"""Pytest configuration for Maya tests."""

import pytest

@pytest.fixture(scope='session', autouse=True)
def initialize():
    """Initialize Maya standalone session before running tests."""
    import maya.standalone
    try:
        maya.standalone.initialize()
    except RuntimeError:
        # Maya is already initialized
        pass
    yield
    maya.standalone.uninitialize()

# Override the default tik_manager4 initialization for Maya
@pytest.fixture(scope='function')
def tik():
    """Initialize tik_manager4 for testing."""
    print("\n")
    print("----------------------------")
    print("Tik Manager 4 is initializing...")
    print("----------------------------")
    from importlib import reload
    import tik_manager4 # importing main checks the common folder definition, thats why its here
    reload(tik_manager4)
    return tik_manager4.initialize("Maya")