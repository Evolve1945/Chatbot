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
  global list_of_words_in_question

  acc = {'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a', 'ù': 'u', 'û': 'u', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'œ': 'oe', 'ç': 'c', 'É': 'E', 'È': 'E', 'Ê': 'E', 'À': 'A', 'Â': 'A', 'Ù': 'U', 'Û': 'U', 'Î': 'I', 'Ï': 'I', 'Ô': 'O', 'Ö': 'O', 'Œ': 'OE'}
  cleaned_character = ""
  list_of_words_in_question =[]

  for char in phrase :
    character = char.lower()                                        # Lower the character A -> a
    
    if character in ("'", "-","\n"):                                # If the character is a special character or a new line
      character = " "                                               # Replace it by a space

    elif character in (".", ",", ":", ";", "!", "?"):               # If the character is a ne or a special character
      character = ""                                                # Delete it            

    for key, value in acc.items():                                  # For each key and value in the acc dictionary
      character = character.replace(key, value)

    cleaned_character += character
   
  list_of_words_in_question = cleaned_character.split()             # Split the text into individual words and put it in a list
  return list_of_words_in_question

    #BONUS

def special_words_in_question() -> list:

  words_in_question(input("Enter a question : ")) 
  
  for item in range(len(list_of_words_in_question)):                        # For each item in the list of words in the question
    if list_of_words_in_question[item] == 'l':                              # Check if the current item is 'l'
      list_of_words_in_question[item] = 'la'                                # Replace 'l' with 'la'
      #print(list_of_words_in_question[item])

    elif list_of_words_in_question[item] == 'qu':                           # Check if the current item is 'qu'
      list_of_words_in_question[item] = 'que'                               # Replace 'qu' with 'que'
      #print(list_of_words_in_question[item])

    elif list_of_words_in_question[item] == 'n':                            # Check if the current item is 'n'
      list_of_words_in_question[item] = 'ne'                                # Replace 'n' with 'ne'
      #print(list_of_words_in_question[item])

    elif list_of_words_in_question[item] == 'j':                            # Check if the current item is 'j'
      list_of_words_in_question[item] = 'je'                                # Replace 'j' with 'je'
      #print(list_of_words_in_question[item])
          
    elif list_of_words_in_question[item] == 'm':                            # Check if the current item is 'm' 
      list_of_words_in_question[item] = 'me'                                # Replace 'm' with 'me'
      #print(list_of_words_in_question[item])
          
    elif list_of_words_in_question[item] == 't':                            # Check if the current item is 't'  
      list_of_words_in_question[item] = 'te'                                # Replace 't' with 'te'
      #print(list_of_words_in_question[item])

    else:
      continue

  return set(list_of_words_in_question)                                        # Return the list of words in the question
 
#special_words_in_question()



def question_word_in_corpus():

  common_words = []

  user_question = special_words_in_question()
  print(user_question)


  # Utiliser intersection pour trouver les mots en commun entre la question et les discours
  
  for file in os.listdir("Speeches"):                                  # For each file in the Speeches folder
      file_path = os.path.join("Speeches", file)                       # Get the path of the file
      file_content = open(file_path, "r", encoding="utf-8").read()     # Open the file and read it
      file_content = words_in_question(file_content)                   # Get the list of words in the file       
      #print(file_content) 
      print("")

      for word in file_content:                                         # For each word in the file content
        if word in user_question:                                       # If the word is in the user question
          
          print(word)                                                   # Print the word
          common_words.append(word)                                     # Add the word to the list of common words
  print(common_words)                                    
  

#print(question_word_in_corpus())


 

