import os
from math import *
from Part_I import *
# -*- coding: utf-8 -*-

#Part II.1

print("Part II")

def words_in_question(phrase : str) -> list:
  """
  IN : str, the input phrase
  OUT : list, the list of words in the question
  Description : Function that takes a phrase as input and returns a list of words in the question
  """
  acc = {'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a', 'ù': 'u', 'û': 'u', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'œ': 'oe', 'ç': 'c', 'É': 'E', 'È': 'E', 'Ê': 'E', 'À': 'A', 'Â': 'A', 'Ù': 'U', 'Û': 'U', 'Î': 'I', 'Ï': 'I', 'Ô': 'O', 'Ö': 'O', 'Œ': 'OE'}
  cleaned_character = ""
  list_of_words_in_question =[]

  for word in phrase :
    formatted_word = word.lower()                                        # Lower the character A -> a
    
    for character in formatted_word:
      if character in ("'", "-","\n"):                                   # If the character is a special character or a new line
        character = " "                                                  # Replace it by a space

      elif character in (".", ",", " :", " ;", "!", "?"):                # If the character is a ne or a special character
        character = ""                                                   # Delete it            

      for key, value in acc.items():                                     # For each key and value in the acc dictionary
        character = character.replace(key, value)

    cleaned_character += character

    list_of_words_in_question = cleaned_character.split(" ")                  # Split the text into individual words and put it in a list


  for item in range(len(list_of_words_in_question)):                        # Iterate over each item in the list_of_words_in_question

        if list_of_words_in_question[item] == "" or list_of_words_in_question[item] == " ":
            list_of_words_in_question.remove(list_of_words_in_question[item])     # Remove the empty strings in the list generate by the absence of special characters

        #BONUS
        
        elif list_of_words_in_question[item] == 'l':                              # Check if the current item is 'l'
            list_of_words_in_question[item] = 'la'                                # Replace 'l' with 'la'

        elif list_of_words_in_question[item] == 'qu':                             # Check if the current item is 'qu'
            list_of_words_in_question[item] = 'que'                               # Replace 'qu' with 'que'

        elif list_of_words_in_question[item] == 'j':
           list_of_words_in_question[item] = 'je'
        
        elif list_of_words_in_question[item] == 'm':
           list_of_words_in_question[item] = 'me'
        
        elif list_of_words_in_question[item] == 't':
           list_of_words_in_question[item] = 'te'

        else:
            continue

  return list_of_words_in_question
 





def question_word_in_corpus():
  tf()
  idf()

