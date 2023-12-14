import os
from math import *
from Part_I import *
# -*- coding: utf-8 -*-

#Part II.1

print("Part II")

directory = "Speeches"
new_directory = "Cleaned"

def words_in_question(phrase : str) -> list:
  """
  IN : str, the input phrase
  OUT : list, the list of words in the question
  Description : Function that takes a sentence as an input and returns a list of words in the question
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

def special_words_in_question() -> set:
  """
  IN : None
  OUT : set, the set of words in the question without the special words
  Description : Function that takes a sentence as an input and returns a set of words in the question without the special words
  """
  clean_words = {"l": "la", "qu": "que", "n": "ne", "j": "je", "m": "me", "t": "te"}                                    # dictionary of words to replace
  words_in_question(input("Enter a question : "))                                                                       # ask the user to enter a question
  for item in range(len(list_of_words_in_question)):                                                                    # for each item in the list of words in the question
    list_of_words_in_question[item] = clean_words.get(list_of_words_in_question[item], list_of_words_in_question[item]) # replace the item by the value of the key in the clean_words dictionary if the key is in the list of words in the question
  return list_of_words_in_question



def question_word_in_corpus(directory : str):

  dico = {}
  common_words = []
  files = os.listdir(directory)
  user_question = special_words_in_question()
  for i in range(len(files)) :
    print(i,".", files[i]) 
  chosen_speech = int(input("Enter the number of the speech to search for the questions words in it : "))


  # Idée : Utiliser intersection pour trouver les mots en commun entre la question et les discours
  file_path = os.path.join("Speeches",files[chosen_speech])                      # Get the path of the file
  file_content = open(file_path, "r", encoding="utf-8").read()     # Open the file and read it
  file_content = words_in_question(file_content)                   # Get the list of words in the file
  for word in file_content:                                         # For each word in the file content
    if word in user_question and word not in common_words :                                       # If the word is in the user question
      common_words.append(word)                                     # Add the word to the list of common words
  
    for word in common_words:
      if word in dico:
        dico[word] += 1
      else:
        dico[word] = 1
  
  #print(common_words)
  return dico                                    

print(question_word_in_corpus(directory))


def TF_IDF_vector():
  calculate_tfidf("Cleaned")



  """
  files = os.listdir("Cleaned")

  tab = [0] * m
  matrix = [tab] * n
  
  for i in range(len(files)):
    for j in range(len(files)):
      pass
    
  """



print(TF_IDF_vector())

 

