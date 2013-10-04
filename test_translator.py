import unittest

from translator import Translator

class TestTranslator(unittest.TestCase):

  def test_translate_lowercase_word(self):
    translator = Translator()
    result = translator.translate("python")
    self.assertEqual("ythonpay", result)

    result = translator.translate("ruby")
    self.assertEqual("ubyray", result)

  def test_translate_capitalized_word(self):
    translator = Translator()
    result = translator.translate("Python")
    self.assertEqual("Ythonpay", result)

if __name__ == '__main__':
  unittest.main()

