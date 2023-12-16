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
  assert phrase != "", "The phrase is empty"                        # If the phrase is empty, raise an error

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

  file_path = os.path.join("Speeches",files[chosen_speech])         # Get the path of the file
  file_content = open(file_path, "r", encoding="utf-8").read()      # Open the file and read it
  file_content = words_in_question(file_content)                    # Get the list of words in the file
  for word in file_content:                                         # For each word in the file content
    if word in user_question and word not in common_words :         # If the word is in the user question
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
 
  frequency = {}                                                                          # Create an empty dictionary to store the word frequencies
  
  with open(os.path.join(folder, file_path), 'r', encoding = 'utf-8') as file:            # Open the file in read mode with UTF-8 encoding
    text = file.read()                                                                    # Read the contents of the file
    words = text.split()                                                                  # Split the text into individual words
    for word in words: 
      
      if word not in list_of_words_in_question:                                           # Iterate over each word in the text
        frequency[word] = 0

      else:

        if word not in frequency:                                                         # Check if the word is not already in the frequency dictionary
          frequency[word] = 1                                                             # If not, initialize the frequency of the word to 1
        
        else:                                                                             # If the word is already in the frequency dictionary
          frequency[word] += 1                                                            # Increment its frequency by 1
    frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))   # Sort the frequency dictionary by value in descending order
    
    return frequency
 



def calculate_tdidf_question(list_of_words_in_question):
  
  idf_values = idf(new_directory)
  tfidf_matrix = []                                                                     # Create an empty list to store the TF-IDF values of the words in the folder

  for filename in os.listdir(new_directory):                                            # Iterate over each file in the folder
    tf_values = tf_question(filename, new_directory, list_of_words_in_question)         # Get the TF values of the words in the file

    for key in idf_values.keys():                                                       # Iterate over each word in the IDF dictionary
      if key in list_of_words_in_question:                                               # Check if the word is in the list of words in the question
        tfidf_value = idf_values[key] * tf_values.get(key, 0)                            # Calculate the TF-IDF value if the word is in the TF dictionary, otherwise set it to 0
        tfidf_matrix.append([key.lower(), [tfidf_value]])                                 # Append the word and its TF-IDF value to the TF-IDF matrix
      else:
        tfidf_matrix.append([key, [0]])                                           # Append the word and 0 as its TF-IDF value to the TF-IDF matrix
  
  return tfidf_matrix                                                                   # Return the TF-IDF matrix

def display_tfidf_matrix (tfidf_matrix) :
  for lign in tfidf_matrix :
      print (lign)

#list_of_words_in_question = words_in_question(input("Enter a question (*): "))
#display_tfidf_matrix(calculate_tdidf_question(list_of_words_in_question))


#Part II.2

def scalar_product(list_a, list_b):
  return sqrt(sum([list_a[i] * list_b[i] for i in range(len(list_a))]))


def norm_vector(list_a): 
  #Sqrt(sum of Ai²) = sqrt(A1² + A2² + ... + An²)
  return sqrt(sum(x**2 for x in list_a))


def cosine_similarity(list_a, list_b):
  if norm_vector(list_a) * norm_vector(list_b) == 0:
    return 0.0
  else:
    return scalar_product(list_a, list_b) / (norm_vector(list_a) * norm_vector(list_b))


def matrix_cosine_similarity(tfidf_question_matrix, tfidf_corpus_matrix):
  list_of_cosine_similarity = []
  for row in range(len(tfidf_question_matrix)):
    word_and_value = [tfidf_corpus_matrix[row][0],cosine_similarity(tfidf_question_matrix[row][0], tfidf_corpus_matrix[row][1])]
    list_of_cosine_similarity.append(word_and_value)
  return list_of_cosine_similarity




tfidf_corpus_matrix = calculate_tfidf(new_directory)

list_of_words_in_question = words_in_question(input("Enter a question (*): "))
tfidf_question_matrix = calculate_tdidf_question(list_of_words_in_question)

#print(tfidf_corpus_matrix)
#print("\n\n\n",tfidf_question_matrix)


print("\n\n\n",matrix_cosine_similarity(tfidf_question_matrix, tfidf_corpus_matrix))
"""
def document_cleaned_title(folder):

  list_of_folder = list_of_files(folder, ".txt")
  title_of_text = []
  word_in_title_text = []
  list_word_in_title_text = []

  #All titles in title_of_text
  for text in list_of_folder:
    title_of_text.append(text)


  #Separate the text and the numbers of the title in title_of_text
  for i in range(len(title_of_text)):
    for k in "1234567890":
        if k in title_of_text[i]:
          title_of_text[i] = title_of_text[i].replace(k, "_" + k)

    #Words in title goes in word_in_title_text after being split at the "_" 
    word_in_title_text.append(title_of_text[i].split("_"))

    #Cleaned the ".txt" of the title
    for j in range(len(word_in_title_text[i])):
      if word_in_title_text[i][j].endswith(".txt"):
        word_in_title_text[i][j] = word_in_title_text[i][j][:-4]
  
  for i in range(len(title_of_text)):
    
    list_word_in_title_text.append([title_of_text[i], word_in_title_text[i]])
  
  for i in list_word_in_title_text :
    nbr = ""
    cpt = -1
    for j in i[1] :
      if j in "1234567890" :
        cpt +=1
        nbr += j
    i[1] = i[1][0:len(i)-cpt]
    if nbr != "" :
      i[1].append(nbr)
    
    

  return list_word_in_title_text

print(document_cleaned_title(new_directory), '\n')

"""

def most_relevant_document(tf_idf_matrix, tf_idf_vector_question, list_name_corpus):

  pass
















