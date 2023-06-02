import unittest
import translator

class TestStringMethods(unittest.TestCase):
    """Tests the functions for translator.py."""
    def test_english_to_french(self):
        """Test 1."""
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour", "Not correct!")
    def test_french_to_english(self):
        """Test 2."""
        self.assertEqual(translator.french_to_english("Bonjour"), "Good morning", "Not correct!")

if __name__ == '__main__':
    unittest.main()
