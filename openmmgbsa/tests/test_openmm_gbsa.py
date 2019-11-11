"""
Unit and regression test for the openmmgbsa package.
"""

# Import package, test suite, and other packages as needed
import openmmgbsa
import pytest
import sys

def test_openmmgbsa_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "openmmgbsa" in sys.modules
