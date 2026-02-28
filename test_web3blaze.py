# test_web3blaze.py
"""
Tests for Web3Blaze module.
"""

import unittest
from web3blaze import Web3Blaze

class TestWeb3Blaze(unittest.TestCase):
    """Test cases for Web3Blaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Blaze()
        self.assertIsInstance(instance, Web3Blaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Web3Blaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
