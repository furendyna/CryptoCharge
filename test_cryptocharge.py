# test_cryptocharge.py
"""
Tests for CryptoCharge module.
"""

import unittest
from cryptocharge import CryptoCharge

class TestCryptoCharge(unittest.TestCase):
    """Test cases for CryptoCharge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoCharge()
        self.assertIsInstance(instance, CryptoCharge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoCharge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
