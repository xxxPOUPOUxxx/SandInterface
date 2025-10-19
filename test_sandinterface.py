# test_sandinterface.py
"""
Tests for SandInterface module.
"""

import unittest
from sandinterface import SandInterface

class TestSandInterface(unittest.TestCase):
    """Test cases for SandInterface class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SandInterface()
        self.assertIsInstance(instance, SandInterface)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SandInterface()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
