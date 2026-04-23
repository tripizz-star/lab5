import unittest

def reverse_string(text):
    """Функция переворота строки (вынесли логику отдельно)"""
    return text[::-1]

class TestReverseString(unittest.TestCase):
    
    def test_hello(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")
    
    def test_single_char(self):
        self.assertEqual(reverse_string("a"), "a")
    
    def test_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
    
    def test_numbers_as_string(self):
        self.assertEqual(reverse_string("12345"), "54321")
    
    def test_russian_letters(self):
        self.assertEqual(reverse_string("привет"), "тевирп")
    
    def test_palindrome(self):
        self.assertEqual(reverse_string("madam"), "madam")

if __name__ == "__main__":
    unittest.main()
