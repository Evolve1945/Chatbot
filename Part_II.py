import os
from math import *
from Part_I import *
import os
# -*- coding: utf-8 -*-

#Part II.1

print("PART II")

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
    
    if character in ("'", "-","\n", "_"):                                # If the character is a special character or a new line
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
 



def calculate_tfidf_question(list_of_words_in_question):
  
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
  
  return tfidf_matrix                                                                 # Return the TF-IDF matrix

#print(calculate_tfidf_question(words_in_question(input("Enter a question : "))))

def display_tfidf_matrix (tfidf_matrix):
  
  for lign in tfidf_matrix :
    print(lign)

# list_of_words_in_question = words_in_question(input("Enter a question (*): "))
# display_tfidf_matrix(calculate_tfidf_question(list_of_words_in_question))


#Part II.2

def scalar_product(tfidf_question_list_of_values, tfidf_corpus_list_of_values):
  """
  Input : two list of values [x, y, z, ...] and [A,B,C,...]
  Output : a list of values [xA, xB, xC, ...]
  """
  list_value = []

  for i in range(len(tfidf_corpus_list_of_values)):
    tot = tfidf_corpus_list_of_values[i] * tfidf_question_list_of_values[i]
    list_value.append(tot)

  return list_value



def norm_vector(tfidf_list_of_values): 
  """
  Input : a list of values [A,B,C,...]
  """
  #print(tfidf_list_of_values)
  b = []

  #Sqrt(sum of Ai²) = sqrt(A1² + A2² + ... + An²)

  for i in range(len(tfidf_list_of_values)):
    b.append(tfidf_list_of_values[i] ** 2)

  c = sqrt(sum(b))

  return c





def cosine_similarity(tfidf_question_list_of_values, tfidf_corpus_list_of_values):
  """
  Input : two list of values [x, y, z,...] and [A,B,C,...]
  """
  final_tab = []

  for i in range(len(tfidf_corpus_list_of_values)):
    if norm_vector(tfidf_question_list_of_values) * norm_vector(tfidf_corpus_list_of_values) == 0:
      final_tab.append(0.0)

    else:
      scalar_product_ = scalar_product(tfidf_question_list_of_values, tfidf_corpus_list_of_values)[i]
      norm_vector_ = norm_vector(tfidf_question_list_of_values) * norm_vector (tfidf_corpus_list_of_values)
      tot = scalar_product_ / norm_vector_
      #print(tot)
      final_tab.append(tot)
  return final_tab


def matrix_cosine_similarity(tfidf_question_matrix, tfidf_corpus_matrix):
  """
  Input : two matrix : [word[x]]   [[word1, [v_text1,v_text2,v_text3,...]]
                                    [word2, [v_text1,v_text2,v_text3,...]]
  """

  list_of_cosine_similarity = []

  for row in range(len(tfidf_corpus_matrix)):                                                         #len(fidf_corpus_matrix) = len(tfidf_question_matrix)
  
    test1 = tfidf_corpus_matrix[row][0]                                                               #Word              
    test2 = cosine_similarity(tfidf_question_matrix[row][1], tfidf_corpus_matrix[row][1])             #Return 
    
    word_and_value = [test1, test2]                                                                   # Word, [Value1, Value2, ...]
    list_of_cosine_similarity.append(word_and_value)

  return list_of_cosine_similarity

# tfidf_corpus_matrix = calculate_tfidf(new_directory)

# list_of_words_in_question = words_in_question(input("Enter a question (**): "))
# tfidf_question_matrix = calculate_tfidf_question(list_of_words_in_question)

# # print(tfidf_question_matrix)
# # print(tfidf_corpus_matrix)
# print(matrix_cosine_similarity(tfidf_question_matrix, tfidf_corpus_matrix))

 

def calculate_relevance(matrix_cosine_similarity, doc_number):
  tot = 0
  for i in range (len(matrix_cosine_similarity)) :
    tot += matrix_cosine_similarity[i][1][doc_number]
  return tot

#print(calculate_relevance(matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus), 4))

def most_relevant_document(matrix_cosine_similarity, list_names_files_corpus):
  total_relevance = []
  for i in range (len(list_names_files_corpus)) :
    total_relevance.append(calculate_relevance(matrix_cosine_similarity, i))
    name_file = list_names_files_corpus[total_relevance.index(max(total_relevance))]
  return name_file



#print(most_relevant_document(matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus), list_of_files(new_directory, ".txt")))


# word_in_question = words_in_question(input("Enter a question : "))                                                      #Clean the word in the question then put it into a list
# tfidf_matrix_question = calculate_tfidf_question(word_in_question)                                                      #Calculate the tfidf of the question              

# tfidf_matrix_corpus = calculate_tfidf(new_directory)

# list_names_files_corpus = list_of_files(new_directory, ".txt")  
# print(list_names_files_corpus)
# print(most_relevant_document(matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus), list_names_files_corpus))


def equivalent_text(file_name, list_of_files):
  cleaned_folder = "Cleaned"
  speeches_folder = "Speeches"

  cleaned_file_path = os.path.join(cleaned_folder, file_name)
  speeches_file_path = os.path.join(speeches_folder, file_name)

  if os.path.exists(speeches_file_path):
    print(cleaned_file_path + " -> " + speeches_file_path)
    print(file_name)
    
    for i in range(len(list_of_files)):
      if file_name == list_of_files[i]:
        print(i)
        return i
  


# file_name = "Nomination_Chirac1.txt" #Remplacer par la fonction most_relevant_document(tf_idf_matrix, tf_idf_vector_question, list_name_corpus)
# equivalent_file_path = equivalent_text(file_name)
# print(equivalent_file_path)


def highest_tfidf_score(most_relevant_document_index, tfidf_question_matrix, words_in_question):
  """
  IN : int, index of the most relevant document, list, matrix of tfidf values of the question
  OUT : str, the word with the highest tfidf score, float, the tfidf score of the word, list, the list of words with the same tfidf score
  """
  
  unimportant_words_mentionned = ['c', 's', 'qu', 'suis', 'es', 'est', 'sommes', 'etes', 'sont', 'me', 'n', 'elle', 'il', 'elles', 'ils', 'soit', 'j', 'je', 'ses', 'se', 'sa', 'ca', 'l', 'le', 'les', 'la', 'un', 'une', 'd', 'de', 'du', 'des', 'et', 'ou', 'où', 'a', 'à', 'au', 'aux', 'en', 'par', 'pour', 'avec', 'dans', 'sur', 'sous', 'entre', 'vers', 'mais', 'donc', 'or', 'ni', 'car', 'que', 'qui', 'quoi', 'quand', 'comment', 'pourquoi', 'quel', 'quelle', 'quelles', 'quels', 'ce', 'cet', 'cette', 'ces', 'mon', 'ton', 'son', 'notre', 'votre', 'leur', 'ceci', 'cela', 'celui', 'celle', 'ceux', 'celles', 'ici', 'là', 'lui', 'eux', 'elles', 'si', 'tout', 'tous', 'toute', 'toutes', 'rien', 'aucun', 'aucune', 'autre', 'autres', 'même', 'mêmes', 'tel', 'telle', 'tels', 'telles', 'quelque', 'quelques', 'plusieurs', 'plus', 'autant', 'tant', 'trop', 'peu', 'beaucoup', 'moins', 'autrefois', 'aujourd', 'hui', 'demain', 'hier', 'maintenant', 'alors', 'après', 'avant', 'bientôt', 'déjà', 'ensuite', 'jamais', 'parfois', 'souvent', 'toujours', 'tard', 'tôt', 'aussi', 'donc', 'ensuite', 'puis', 'quand', 'que', 'comment', 'où', 'pourquoi', 'qui', 'quoi', 'si', 'comme', 'ainsi']
  final_question_matrix = []

  for row in range(len(tfidf_question_matrix)):
    if tfidf_question_matrix[row][0] in words_in_question:
      word = tfidf_question_matrix[row][0]
      if tfidf_question_matrix[row][0] in unimportant_words_mentionned:
        value = 0

      else:
        value = tfidf_question_matrix[row][1][most_relevant_document_index]

      word_and_value = [word, value]
      final_question_matrix.append(word_and_value)

  final_question_matrix = sorted(final_question_matrix, key=lambda x: x[1], reverse=True)

  return final_question_matrix[0]


#CALL
# word_in_question = words_in_question(input("Enter a question : "))                                                      #Clean the word in the question then put it into a list
# tfidf_matrix_question = calculate_tfidf_question(word_in_question)    
                                                         

# tfidf_matrix_corpus = calculate_tfidf(new_directory)

# list_names_files_corpus = list_of_files(new_directory, ".txt")
# most_relevant_document_index = most_relevant_document(matrix_cosine_similarity(tfidf_question_matrix, tfidf_corpus_matrix), list_names_files_corpus)  


# print(highest_tfidf_score(most_relevant_document_index, tfidf_matrix_question,word_in_question))                                                                   #Get the word with the highest tfidf score of the most relevant document
  

def first_occurrence_in_text(word_to_find, equivalent_text):

  word_to_find = word_to_find[0]
  equivalent_path = os.path.join("Speeches", equivalent_text)
  read_text = open(equivalent_path, "r", encoding="utf-8").read()           #Open the file and read it
  # print(read_text) #fonctionne
  phrase = read_text.split(".")                                             #Split the text into phrases
  # print(phrase) #fonctionne


  cleaned_phrase = []                                                     
  filtered_phrase = []

  un_cleaned_dico = {}

  for p in phrase:
    un_cleaned_dico[p] = words_in_question(p)                                #Cleaned the phrase and put it as value of p
    cleaned_p = words_in_question(p)                                         
    cleaned_phrase.append(cleaned_p)
  #print("\n", cleaned_phrase)                                               #[[word1, word2, ...], [word1, word2, ...], ...]
  print('\n', un_cleaned_dico)                                              #{phrase1 : [word1, word2, ...], phrase2 : [word1, word2, ...], ...}


  for phrase in cleaned_phrase:                                              #[word1, word2, ...]
    if word_to_find in phrase:                                               #[word1, word2, word_to_find, ...]
      for i in range(len(phrase)):                                           #[word1, word2, word_to_find, ...]
        filtered_phrase.append(phrase[i])
  
  print('\n',filtered_phrase)

  L = []

  if 0 < len(filtered_phrase):
    for key, value in un_cleaned_dico.items():
      if filtered_phrase == value :
        L.append(key)
  return L


         
          
word_in_question = words_in_question(input("Enter a question : "))                                                      #Clean the word in the question then put it into a list
tfidf_matrix_question = calculate_tfidf_question(word_in_question)                                                        

tfidf_matrix_corpus = calculate_tfidf(new_directory)

list_names_files_corpus = list_of_files(new_directory, ".txt")

matrix_similarity = matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus)

most_relevant_document_index = most_relevant_document(matrix_similarity, list_names_files_corpus)  
print(most_relevant_document_index)

equivalent_file_path = equivalent_text(most_relevant_document_index, list_of_files(directory, ".txt"))

most_revelant_word = highest_tfidf_score(equivalent_file_path, tfidf_matrix_question,word_in_question)                                                                #Get the word with the highest tfidf score of the most relevant document
  

      
print(first_occurrence_in_text(most_revelant_word, most_relevant_document_index))


































#???

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

"""
def equivalent_text(file_name):
  cleaned_folder = "Cleaned"
  speeches_folder = "Speeches"

  cleaned_file_path = os.path.join(cleaned_folder, file_name)
  speeches_file_path = os.path.join(speeches_folder, file_name)

  if os.path.exists(speeches_file_path):
    return speeches_file_path
  else:
    print("No such file in the folder")
    return None

file_name = "Nomination_Chirac1.txt"
equivalent_file_path = equivalent_text(file_name)
print(equivalent_file_path)
"""