import unittest

from translator import english_to_french, french_to_english

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertRaises(ValueError,french_to_english,None) 
    def test2(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  

class englishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertRaises(ValueError,english_to_french,None) 
    def test2(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 

unittest.main()