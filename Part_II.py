import os
from math import *
from Part_I import *
import os
# -*- coding: utf-8 -*-

#Part II

#print("PART II")

directory = "Speeches"
new_directory = "Cleaned"

def words_in_question(phrase : str) -> list:
  """
  IN : str, the input phrase
  OUT : list, the list of words in the question
  Description : Function that takes a sentence as an input and returns a list of words in the question
  """
  global list_of_words_in_question                                  # Make the list of words in the question a global variable
  assert phrase != "", "The phrase is empty"                        # Check if the phrase is not empty

  acc = {'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a', 'ù': 'u', 'û': 'u', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'œ': 'oe', 'ç': 'c', 'É': 'E', 'È': 'E', 'Ê': 'E', 'À': 'A', 'Â': 'A', 'Ù': 'U', 'Û': 'U', 'Î': 'I', 'Ï': 'I', 'Ô': 'O', 'Ö': 'O', 'Œ': 'OE'}          # Dictionary of accents to replace
  cleaned_character = ""                                            # Initialize an empty string to store the cleaned characters
  list_of_words_in_question =[]                                     # Initialize an empty list to store the words in the question

  for char in phrase :                                              # For each character in the phrase
    character = char.lower()                                        # Convert the character to lowercase
    
    if character in ("'", "-","\n", "_"):                           # If the character is a space, a dash or a newline      
      character = " "                                               # Replace the character by a space

    elif character in (".", ",", ":", ";", "!", "?", '"'):          # If the character is a punctuation mark
      character = ""                                                # Replace the character by an empty string          

    for key, value in acc.items():                                  # For each key and value in the acc dictionary
      character = character.replace(key, value)                     # Replace the key by the value in the character

    cleaned_character += character                                  # Add the cleaned character to the cleaned character string
   
  list_of_words_in_question = cleaned_character.split()             # Split the cleaned character string into individual words
  
  return list_of_words_in_question                                  # Return the list of words in the question

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
  
  return list_of_words_in_question                                                                                      # return the list of words in the question without the special words


def question_word_in_corpus(directory : str):                     
  """
  IN : str, the directory of the corpus
  OUT : dict, the dictionary of the common words between the question and the corpus
  Description : Function that takes the directory of the corpus as an input and returns a dictionary of the common words between the question and the corpus"""
  dico = {}                                                         # Create an empty dictionary to store the common words between the question and the corpus
  common_words = []                                                 # Create an empty list to store the common words between the question and the corpus
  files = os.listdir(directory)                                     # Get the list of files in the directory
  user_question = special_words_in_question()                       # Get the list of words in the question without the special words
  for i in range(len(files)) :                                      # For each file in the directory
    print(i+1,".", files[i])                                        # Print the number of the file and its name
  chosen_speech = int(input("Enter the number of the speech to search for the questions words in it : "))   # Ask the user to enter the number of the speech to search for the questions words in it

  file_path = os.path.join("Speeches",files[chosen_speech])         # Get the path of the file
  file_content = open(file_path, "r", encoding="utf-8").read()      # Open the file and read it
  file_content = words_in_question(file_content)                    # Get the list of words in the file
  for word in file_content:                                         # For each word in the file content
    if word in user_question and word not in common_words :         # If the word is in the user question
      common_words.append(word)                                     # Add the word to the list of common words
  
    for word in common_words:                                       # For each word in the list of common words
      if word in dico:                                              # If the word is in the dictionary
        dico[word] += 1                                             # Increment its frequency by 1
      else:                                                         # If not
        dico[word] = 1                                              # If not, initialize its frequency to 1
  
  #print(common_words)
  return dico                                    


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
 

def calculate_tfidf_question(list_of_words_in_question):
  
  idf_values = idf(new_directory)
  tfidf_matrix = []                                                                     # Create an empty list to store the TF-IDF values of the words in the folder

  for filename in os.listdir(new_directory):                                            # Iterate over each file in the folder
    tf_values = tf_question(filename, new_directory, list_of_words_in_question)         # Get the TF values of the words in the file

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
          tfidf_matrix.append([key.lower(), [idf_values[key] * tf_values[key]]])        # If yes, append the word and its TF-IDF value to the TF-IDF matrix
        

        else:                                                                           # If not
          tfidf_matrix.append([key.lower(), [0]])                                       # Append the word and 0 to the TF-IDF matrix
  
  return tfidf_matrix                                                                   # Return the TF-IDF matrix


def display_tfidf_matrix (tfidf_matrix):
  
  for lign in tfidf_matrix :
    print(lign)


def scalar_product(tfidf_question_list_of_values, tfidf_corpus_list_of_values):
  """
  Input : two list of values [x, y, z, ...] and [A,B,C,...]
  Output : a list of values [xA, xB, xC, ...]
  """
  list_value = []

  for i in range(len(tfidf_corpus_list_of_values)):                                     #len(tfidf_corpus_list_of_values) = len(tfidf_question_list_of_values)
    tot = tfidf_corpus_list_of_values[i] * tfidf_question_list_of_values[i]             #xA, xB, xC, ...
    list_value.append(tot)                                                              #[xA, xB, xC, ...]

  return list_value



def norm_vector(tfidf_list_of_values): 
  """
  Input : a list of values [A,B,C,...]
  """
  #Sqrt(sum of Ai²) = sqrt(A1² + A2² + ... + An²)
  
  list_of_values = []

  for i in range(len(tfidf_list_of_values)):                                            #len(tfidf_list_of_values) = len(tfidf_list_of_values)
    list_of_values.append(tfidf_list_of_values[i] ** 2)                                 #A1², A2², ... , An²
  final_result = sqrt(sum(list_of_values))                                              #sqrt(A1² + A2² + ... + An²)

  return final_result


def cosine_similarity(tfidf_question_list_of_values, tfidf_corpus_list_of_values):
  """
  IN : list, the list of tfidf values of the question, list, the list of tfidf values of the corpus
  OUT : list, the list of cosine similarity
  """
  final_tab = []

  for i in range(len(tfidf_corpus_list_of_values)):                                                                     #len(tfidf_corpus_list_of_values) = len(tfidf_question_list_of_values)
    if norm_vector(tfidf_question_list_of_values) * norm_vector(tfidf_corpus_list_of_values) == 0:                      #If the norm of the vector is 0
      final_tab.append(0.0)                                                                                             #Append 0.0 to the final_tab because we can't divide by 0

    else:
      scalar_product_ = scalar_product(tfidf_question_list_of_values, tfidf_corpus_list_of_values)[i]                   #scalar_product_ = [xA, xB, xC, ...]
      norm_vector_ = norm_vector(tfidf_question_list_of_values) * norm_vector (tfidf_corpus_list_of_values)             #norm_vector_ = sqrt(A1² + A2² + ... + An²) * sqrt(x1² + x2² + ... + xn²)
      tot = scalar_product_ / norm_vector_                                                                              #tot = [xA, xB, xC, ...] / sqrt(A1² + A2² + ... + An²) * sqrt(x1² + x2² + ... + xn²)
      final_tab.append(tot)                                                                                             #Append tot to the final_tab
  return final_tab


def matrix_cosine_similarity(tfidf_question_matrix, tfidf_corpus_matrix):
  """
  IN : list, the matrix of tfidf values of the question, list, the matrix of tfidf values of the corpus
  OUT : list, the matrix of cosine similarity
  """

  list_of_cosine_similarity = []

  for row in range(len(tfidf_corpus_matrix)):                                                         #len(fidf_corpus_matrix) = len(tfidf_question_matrix)
  
    test1 = tfidf_corpus_matrix[row][0]                                                               #Word              
    test2 = cosine_similarity(tfidf_question_matrix[row][1], tfidf_corpus_matrix[row][1])             #[Value1, Value2, ...]
    
    word_and_value = [test1, test2]                                                                   # Word, [Value1, Value2, ...]
    list_of_cosine_similarity.append(word_and_value)                                                  #[[Word, [Value1, Value2, ...]], [[Word, [Value1, Value2, ...]], ...]

  return list_of_cosine_similarity



def calculate_relevance(matrix_cosine_similarity, doc_number):
  """
  IN : list, the matrix of cosine similarity, int, the number of the document
  OUT : float, the relevance of the document
  """
  tot = 0
  for i in range (len(matrix_cosine_similarity)) :                                                    #len(matrix_cosine_similarity) = len(tfidf_question_matrix)
    tot += matrix_cosine_similarity[i][1][doc_number]                                                 #tot = Value1 + Value2 + ... + ValueN
  return tot


def most_relevant_document(matrix_cosine_similarity, list_names_files_corpus):
  """
  IN : list, the matrix of cosine similarity, list, the list of names of the files in the corpus
  OUT : str, the name of the most relevant document
  """
  total_relevance = []
  for i in range (len(list_names_files_corpus)) :                                                     #len(list_names_files_corpus) = len(matrix_cosine_similarity)
    total_relevance.append(calculate_relevance(matrix_cosine_similarity, i))                          #total_relevance = [Value1, Value2, ...]
    name_file = list_names_files_corpus[total_relevance.index(max(total_relevance))]                  #name_file = name of the file with the highest relevance
  return name_file




def equivalent_text(file_name, list_of_files):
  """
  IN : str, the name of the file, list, the list of files in the folder
  OUT : str, the equivalent file path
  """
  cleaned_folder = "Cleaned"
  speeches_folder = "Speeches"

  cleaned_file_path = os.path.join(cleaned_folder, file_name)                                         #cleaned_file_path = Cleaned/file_name
  speeches_file_path = os.path.join(speeches_folder, file_name)                                       #speeches_file_path = Speeches/file_name

  if os.path.exists(speeches_file_path):                                                              #If the file exists in the Speeches folder
    #print(cleaned_file_path + " -> " + speeches_file_path)
    
    for i in range(len(list_of_files)):                                                               #For each file in the list of files
      if file_name == list_of_files[i]:                                                               #If the file name is in the list of files
        return i                                                                                      #Return the index of the file


def highest_tfidf_score(most_relevant_document_index, tfidf_question_matrix, words_in_question):
  """
  IN : int, index of the most relevant document, list, matrix of tfidf values of the question
  OUT : str, the word with the highest tfidf score, float, the tfidf score of the word, list, the list of words with the same tfidf score
  """
  
  unimportant_words_mentionned = ['c', 's', 'qu', 'suis', 'es', 'est', 'sommes', 'etes', 'sont', 'me', 'n', 'elle', 'il', 'elles', 'ils', 'soit', 'j', 'je', 'ses', 'se', 'sa', 'ca', 'l', 'le', 'les', 'la', 'un', 'une', 'd', 'de', 'du', 'des', 'et', 'ou', 'où', 'a', 'à', 'au', 'aux', 'en', 'par', 'pour', 'avec', 'dans', 'sur', 'sous', 'entre', 'vers', 'mais', 'donc', 'or', 'ni', 'car', 'que', 'qui', 'quoi', 'quand', 'comment', 'pourquoi', 'quel', 'quelle', 'quelles', 'quels', 'ce', 'cet', 'cette', 'ces', 'mon', 'ton', 'son', 'notre', 'votre', 'leur', 'ceci', 'cela', 'celui', 'celle', 'ceux', 'celles', 'ici', 'là', 'lui', 'eux', 'elles', 'si', 'tout', 'tous', 'toute', 'toutes', 'rien', 'aucun', 'aucune', 'autre', 'autres', 'même', 'mêmes', 'tel', 'telle', 'tels', 'telles', 'quelque', 'quelques', 'plusieurs', 'plus', 'autant', 'tant', 'trop', 'peu', 'beaucoup', 'moins', 'autrefois', 'aujourd', 'hui', 'demain', 'hier', 'maintenant', 'alors', 'après', 'avant', 'bientôt', 'déjà', 'ensuite', 'jamais', 'parfois', 'souvent', 'toujours', 'tard', 'tôt', 'aussi', 'donc', 'ensuite', 'puis', 'quand', 'que', 'comment', 'où', 'pourquoi', 'qui', 'quoi', 'si', 'comme', 'ainsi']
  final_question_matrix = []

  for row in range(len(tfidf_question_matrix)):                                                     #len(tfidf_question_matrix) = len(tfidf_corpus_matrix)
    if tfidf_question_matrix[row][0] in words_in_question:                                          #If the word is in the question
      word = tfidf_question_matrix[row][0]                                                          #word = word
      if tfidf_question_matrix[row][0] in unimportant_words_mentionned:                             #If the word is in the list of unimportant words
        value = 0                                                                                   #value = 0

      else:
        value = tfidf_question_matrix[row][1][most_relevant_document_index]                         #value = tfidf value of the word in the most relevant document

      word_and_value = [word, value]                                                                #word_and_value = [word, value]
      final_question_matrix.append(word_and_value)                                                  #final_question_matrix = [[word, value], [word, value], ...]

  final_question_matrix = sorted(final_question_matrix, key = lambda x : x[1], reverse = True)           #Sort the final_question_matrix by value in descending order

  if final_question_matrix:
    return final_question_matrix[0]
  else:
    return "No word found"



def first_occurrence_in_text(word_to_find, equivalent_text):
  """
  IN : str, the word with the highest tfidf score, int, the index of the most relevant document
  OUT : str, the first occurrence of the word in the text
  """

  word_to_find = word_to_find[0]

  equivalent_path = os.path.join("Speeches", equivalent_text)               #equivalent_path = Speeches/equivalent_text
  read_text = open(equivalent_path, "r", encoding="utf-8").read()           #Open the file and read it
 
  phrase = read_text.split(".")                                             #Split the text into phrases
                                                    
  filtered_phrase = []
  cleaned_matrix = []
  cleaned_p = []
  sentence = []

  for p in phrase:
    cleaned_p = words_in_question(p)                                         #Clean the phrase with the previous function made for the questions
    sentence = [p, cleaned_p]                                                #[phrase, [word1, word2, ...]]
    cleaned_matrix.append(sentence)                                          #[[word1, word2, ...], [word1, word2, ...], ...]

  for phrase in cleaned_matrix:                                              #[word1, word2, ...]
    if word_to_find in phrase[1] and len(phrase[0]) > 0 :                                            #[word1, word2, word_to_find, ...]
      filtered_phrase.append(phrase[0])                                      #[word1, word2, word_to_find, ...]
  
  return filtered_phrase                                                     #Return the first occurrence of the word in the text


def cleaned_response(question, phrase):
  """
  IN : str, the question, str, the first occurrence of the word in the text
  OUT : str, the cleaned response
  """
  answer = {"comment": "Après analyse ; ", "pourquoi": "Car ; ", "peux tu": "Oui, bien sûr! Dans les faits ; ", "quoi": "En ce qui concerne cela ; ", "qui": "En termes de personnes ; ", "quel": "Concernant ce choix ; ", "est ce que": "Bien entendu ; ", "penses tu que": "De mon point de vue ; ", "explique": "Pour mieux comprendre ; ", "decris": "En détail ; ", "imagine": "En imaginant ; ", "en quoi consiste": "En ce qui concerne cela ; "}

  for key, value in answer.items():                                           #For each key and value in the answer dictionary
    if key in question:                                                       #If the key is in the question
      phrase = value + phrase + "."                                                #phrase = value + phrase
  return phrase                                                               #Return the phrase
         
          
#word_in_question = words_in_question(input("Enter a question : "))                                                    
#tfidf_matrix_question = calculate_tfidf_question(word_in_question)                                                        

#tfidf_matrix_corpus = calculate_tfidf(new_directory)

#list_names_files_corpus = list_of_files(new_directory, ".txt")

# matrix_similarity = matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus)

# most_relevant_document_index = most_relevant_document(matrix_similarity, list_names_files_corpus)  

# equivalent_file_path = equivalent_text(most_relevant_document_index, list_of_files(directory, ".txt"))

# most_revelant_word = highest_tfidf_score(equivalent_file_path, tfidf_matrix_question,word_in_question)                                                            
  
# un_cleaned_phrase = first_occurrence_in_text(most_revelant_word, most_relevant_document_index)

# cleaned_response(word_in_question, un_cleaned_phrase)

