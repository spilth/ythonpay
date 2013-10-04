class Translator(object):

  def translate(self, word):
    translation = word[1::] + word[0] + "ay"
    if word[0].isupper():
      return translation.title()
    else:
      return translation

