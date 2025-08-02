# test_futurelingua.py
"""
Tests for FutureLingua module.
"""

import unittest
from futurelingua import FutureLingua

class TestFutureLingua(unittest.TestCase):
    """Test cases for FutureLingua class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FutureLingua()
        self.assertIsInstance(instance, FutureLingua)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FutureLingua()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
