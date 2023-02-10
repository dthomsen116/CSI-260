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
        
        
        
          
        


convert_word("always")
