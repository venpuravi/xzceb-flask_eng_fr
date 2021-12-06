import unittest
import machinetranslation.translator
#from machinetranslation import translator
#from machinetranslation import translator
from machinetranslation.translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french(""), "Error : empty string")
        
        

class TestF2E(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(""), "Error : empty string")


unittest.main()