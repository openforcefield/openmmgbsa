"""
Unit and regression test for the openmm_gbsa package.
"""

# Import package, test suite, and other packages as needed
import openmm_gbsa
import pytest
import sys

def test_openmm_gbsa_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "openmm_gbsa" in sys.modules
