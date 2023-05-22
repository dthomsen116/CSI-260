Complete the function convert_word(word) so it returns the piglatin version of the word that is given as an argument.

We will be following a simplified set of piglatin rules:

1. For words that begin with [consonants](https://en.wikipedia.org/wiki/Consonant), all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added, as in the following examples:

- "pig" = "igpay"
- "latin" = "atinlay"
- "banana" = "ananabay"
- "smile" = "ilesmay"
- "string" = "ingstray"
- "stupid" = "upidstay"

2. For words that begin with vowel, one just adds "way". Examples are:

- "eat" = "eatway" 
- "omelet" = "omeletway" 