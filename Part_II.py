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
  Description : Function that takes a sentence as an input and returns a list of words in the question
  """
  global list_of_words_in_question
  assert phrase != "", "The phrase is empty"                        # If the phrase is empty, raise an error

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
  return list_of_words_in_question                                                                                      # return the list of words in the question



def question_word_in_corpus(directory : str) -> list:
  """
  IN : str, the directory of the corpus
  OUT : list, the list of words in the question that are in the corpus
  Description : Function that takes a directory as an input and returns a list of words in the question that are in the corpus
  """
  common_words = []                                                       #list of words in the question that are in the corpus
  files = os.listdir("Speeches")                                          #list of files in the corpus
  user_question = special_words_in_question()                             #list of words in the question

  for i in range(len(files)) :                                            #print the list of files in the corpus
    print(i,".", files[i])                                                #print the list of files in the corpus
  chosen_speech = int(input("Enter the number of the speech to search for the questions words in it : ")) #ask the user to choose a speech

  file_path = os.path.join("Speeches",files[chosen_speech])               #path of the chosen speech
  file_content = open(file_path, "r", encoding="utf-8").read()            #content of the chosen speech
  file_content = words_in_question(file_content)                          #list of words in the chosen speech
  for word in file_content:                                               #for each word in the chosen speech
    if word in user_question and word not in common_words :               #if the word is in the question and not in the list of common words
      common_words.append(word)                                           #add the word to the list of common words
  return common_words                                                     #return the list of common words
  

#print(question_word_in_corpus(directory))


 

