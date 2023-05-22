def convert_word(word):
   
  VOWELS = ('a', 'e', 'i', 'o', 'u')
  vowelpos=0
  cons = ''
  brokenword = [*word]
  
  for letter in brokenword:
    if letter not in VOWELS:
        vowelpos += 1
        cons += letter
        

    if letter in VOWELS:
        if cons == '':
            finalWord = word + "way"
            print(finalWord)
            return(finalWord)
        else:
            finalWord = (word[vowelpos:] + cons + "ay")
            print(finalWord)
            return(finalWord)
        

import unittest
#Click to add an import
class UnitTests(unittest.TestCase):

  def test_vowel_start(self):
# Failure message: 
# "always" = "alwaysway" 
# "ends" = "endsway" 
# "honest" = "honestway"
    self.assertEqual(convert_word('always'), 'alwaysway')
    self.assertEqual(convert_word('ends'), 'endsway')
    self.assertEqual(convert_word('i'), 'iway')
  def test_consonant_first(self):
# Failure message: 
# Fails for bagel, trash or store
# agelbay, ashtray, orestay
    self.assertEqual(convert_word('bagel'), 'agelbay')
    self.assertEqual(convert_word('trash'), 'ashtray')
    self.assertEqual(convert_word('store'), 'orestay')

if __name__ == '__main__':
    unittest.main()
