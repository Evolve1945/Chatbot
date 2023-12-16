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

    elif character in (".", ",", ":", ";", "!", "?", '"'):          # If the character is a ne or a special character
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
    print(i+1,".", files[i]) 
  chosen_speech = int(input("Enter the number of the speech to search for the questions words in it : "))

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
  
  print(common_words)
  return dico                                    

#print(question_word_in_corpus(directory))


def tf_question(file_path, folder, list_of_words_in_question):
  """
  1655 mots, 8 docs
  """
  assert type(file_path) == str and file_path != "" and type(folder) == str and folder != "", "Insert a valid str file path and folder" #Checks if the file path and the folder are str
 
  frequency = {}                                                                        # Create an empty dictionary to store the word frequencies
  
  with open(os.path.join(folder, file_path), 'r', encoding = 'utf-8') as file:          # Open the file in read mode with UTF-8 encoding
    text = file.read()                                                                  # Read the contents of the file
    words = text.split()                                                                # Split the text into individual words
    for word in words: 
      
      if word not in list_of_words_in_question:                                                                 # Iterate over each word in the text
        frequency[word] = 0

      else:

        if word not in frequency:                                                         # Check if the word is not already in the frequency dictionary
          frequency[word] = 1                                                             # If not, initialize the frequency of the word to 1
        
        else:                                                                             # If the word is already in the frequency dictionary
          frequency[word] += 1                                                            # Increment its frequency by 1
    frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True)) # Sort the frequency dictionary by value in descending order
    return frequency
 


  



def calculate_tdidf_vector(list_of_words_in_question):
  
  idf_values = idf(new_directory)
  tfidf_matrix = []                                                                 # Create an empty list to store the TF-IDF values of the words in the folder

  for filename in os.listdir(new_directory):                                                   # Iterate over each file in the folder
    tf_values = tf_question(filename, new_directory, list_of_words_in_question)                                                    # Get the TF values of the words in the file

    for key in idf_values.keys():                                                       # Iterate over each word in the IDF dictionary
      found = False                                                                     # Initialize a boolean variable to keep track of whether the word is in the TF-IDF matrix or not

      for i in range(len(tfidf_matrix)):                                                # Iterate over each word in the TF-IDF matrix
        
        if tfidf_matrix[i][0] == key:                                                   # Check if the word is already in the TF-IDF matrix
          
          if key in tf_values :                                                         # If yes, check if the word is in the TF dictionary
            tfidf_matrix[i][1].append(idf_values[key] * tf_values[key])                 # If yes, append the TF-IDF value of the word to the list of TF-IDF values of the word
          
          else:                                                                         # If not
            tfidf_matrix[i][1].append(0)                                                # Append 0 to the list of TF-IDF values of the word
          found = True                                                                  # Set the boolean variable to True
      
      if found == False:                                                                # If the word is not in the TF-IDF matrix
        
        if key in tf_values:                                                            # Check if the word is in the TF dictionary
          tfidf_matrix.append([key.lower(), [idf_values[key] * tf_values[key]]])                # If yes, append the word and its TF-IDF value to the TF-IDF matrix
        

        else:                                                                           # If not
          tfidf_matrix.append([key.lower(), [0]])                                               # Append the word and 0 to the TF-IDF matrix
  
  return tfidf_matrix                                                                  # Return the TF-IDF matrix

def display_tfidf_matrix (tfidf_matrix) :
  for lign in tfidf_matrix :
      print (lign)

#list_of_words_in_question = words_in_question(input("Enter a question (*): "))
#display_tfidf_matrix(calculate_tdidf_vector(list_of_words_in_question))


#Part II.2

def scalar_product(a, b):
  return sqrt(a * b)


def norm_vector(a):
  return sqrt(sum([x**2 for x in a]))


def cosine_similarity(a, b):
  return scalar_product(a, b) / (norm_vector(a) * norm_vector(b))


def matrix_cosine_similarity(tfidf_question_matrix, tfidf_corpus_matrix):
  for row in range(len(tfidf_question_matrix)):
    for column in range (len(tfidf_corpus_matrix[row][1])):
      cosine_similarity(tfidf_question_matrix[row][1][column], tfidf_corpus_matrix[row][1][column])
      

def document_name_similarity(folder):
  list_of_folder = list_of_files(folder, ".txt")
  title_of_text = []
  word_in_title_text = []
  dico_title_text = {}

  for text in list_of_folder:
    title_of_text.append(text)

  for i in range(len(title_of_text)):
    for k in "1234567890":
        if k in title_of_text[i]:
          title_of_text[i] = title_of_text[i].replace(k, "_" + k)

    word_in_title_text.append(title_of_text[i].split("_"))
    for j in range(len(word_in_title_text[i])):
      if word_in_title_text[i][j].endswith(".txt"):
        word_in_title_text[i][j] = word_in_title_text[i][j][:-4]
      
  for i in range(len(title_of_text)):
    for j in range(len(word_in_title_text[i])):
      if title_of_text[i] not in dico_title_text:
        dico_title_text[title_of_text[i]] = word_in_title_text[i]


    """
      if title_of_text[i] not in dico_title_text:
        dico_title_text[title_of_text[i]] = 
    """

    """
    word = text.split("_")
    for i in range(len(word)):
      word_in_title_text.append(word[i])
      for j in range(len(word_in_title_text)):
        if word_in_title_text[j].endswith(".txt"):
          word_in_title_text[j] = word_in_title_text[j][:-4]
        else:
          for k in "0123456789":
            if k in word_in_title_text[j]:
              word_in_title_text[j] = word_in_title_text[j].replace(k, "")
    """

  return dico_title_text


print(document_name_similarity(new_directory))




















