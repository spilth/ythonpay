import unittest

from translator import Translator

class TestTranslator(unittest.TestCase):

  def test_translate(self):
    translator = Translator()
    result = translator.translate("python")
    self.assertEqual("ythonpay", result)

if __name__ == '__main__':
  unittest.main()

