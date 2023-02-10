def has_vowels(word):
   
    VOWELS = ('a', 'e', 'i', 'o', 'u')
    count = 0 
    
    for letter in word:
        if letter in VOWELS: 
            count += 1

            
    if count >= 2:
        return True
    else:
        return False
        
print(has_vowels("David"))