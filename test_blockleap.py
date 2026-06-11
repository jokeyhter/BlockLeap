# test_blockleap.py
"""
Tests for BlockLeap module.
"""

import unittest
from blockleap import BlockLeap

class TestBlockLeap(unittest.TestCase):
    """Test cases for BlockLeap class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockLeap()
        self.assertIsInstance(instance, BlockLeap)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockLeap()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
