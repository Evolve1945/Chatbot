import os
from math import log
# -*- coding: utf-8 -*-


#PART I
print("PART I\n")

#Variables
dict_president_full_name = {"Chirac" : "Jacques", "Giscard dEstaing" : "Gilles", "Hollande" : "François", "Macron" : "Emmanuel", "Sarkozy" : "Nicolas", "Mitterrand" : "François"}
dict_year_president = {1995 : "Chirac", 2007 : "Sarkozy", 2012 : "Hollande", 2017 : "Macron", 1981 : "Mitterrand", 1974 : "Giscard dEstaing"}
directory = "Speeches"

#Functions

def list_of_files(directory : str, extension : str) -> list:  # Defines a function named "list_of_files" that takes two parameters: "directory" and "extension"
  """
  IN : str, the path of the directory & str, the extension of the files we want to get
  OUT : list of strs, the names of the files with the extension we want
  Description : Function that takes a directory and an extension as input and returns a list of the names of the files in the directory with the specified extension
  """
  assert directory != "" and extension != "" and type(directory) == str and type(extension) == str, "Insert a valid str directory and extension"# Checks if the directory and the extension are not empty
  files_names = []                                            # Creates an empty list named "files_names"
  for filename in os.listdir(directory):                      # Iterates over the files in the specified directory
    if filename.endswith(extension):                          # Checks if the file has the specified extension
      files_names.append(filename)                            # Adds the file name to the "files_names" list
  return files_names                                          # Returns the list of file names
  
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)



def president_last_name(file : str) -> str:                                 # Defines a function named "president_last_name" that takes one parameter: "file"
  """
  IN : str, the full name of the .txt file, with the extension
  OUT : the name of the president's name giving the speech
  Description : print the president's name present in the title of the file (without the number and the extention file)
  """
  assert type(file) == str and file != "", "Insert a valid str file"        #Checks if the file is a str
  L = os.path.basename(file).split("_")                                     #Split the name of the last file/folder of the path into a list of strs, where we can find the first element, supposed   to be the word "Nomination" and the second element, the name of the president with or without a number, following with the extension of the file, here ".txt"
  cpt = 0                                                                   #Counter to prevent from the name being followed by a number having more than 1 digit
  for i in range (len(L[1].split(".")[0])-1,1,-1) :                         #for loop to prevent from the name being followed by a number having more than 1 digit
    if L[1].split(".")[0][i] in "abcdefghijklmnopqrstuvwxyz" and cpt == 0:  #if the last character of the name is a letter and the counter is equal to 0, we have the last character of the name
      name = L[1].split(".")[0][:i+1]                                       #We have the name of the president
      cpt += 1                                                              #Increment the counter to prevent from the name being followed by a number having more than 1 digit
  return name                                                               #Return the name of the president




def get_names (directory :str) -> list :                                    # Defines a function named "get_names" that takes one parameter: "directory"
  """  
  IN : str corresponding to the location of the directory
  OUT : list of strs, all last names which made the speech, without duplicates
  Description : Function to get all the last names of the presidents which speeches are in the folder folder in parameters
  """
  assert type(directory) == str and directory != "", "Insert a valid str directory" #Checks if the directory is a str
  list_of_speeches = []                                                     #Create an empty list to store the names of the presidents
  for namefile in os.listdir(directory) :                                   #Loop through the list of files in the directory            
    if namefile.endswith(".txt") :                                          #Check if the file is a .txt file                     
      speech = president_last_name(os.path.join(namefile))                  #Get the name of the president giving the speech
      if speech not in list_of_speeches :                                   #Check if the name of the president is not already in the list of names
        list_of_speeches.append(speech)                                     #If not, add the name of the president to the list of names
  return list_of_speeches                                                   #Return the list of names





def president_full_names (list_of_files : list) -> None:              # Defines a function named "president_full_names" that takes one parameter: "list_of_files"
  """
  IN : list of strs, corresponding to files names
  OUT : None no return
  Description : Function that takes a list of name files as input and prints a string of with all president full names
  """
  assert type(list_of_files) == list and list_of_files != [], "Insert a valid list of files" #Checks if the list of files is a list
  global dict_president_full_name                                     # Declare a global variable
  names = []                                                          # Declare an empty list to store the names
  for text in list_of_files :                                         # Loop through the list of files we gave as paramaters
    name = dict_president_full_name[text]+ " " + text                 # Concatenate the president's first name and last name
    names.append(name)                                                # Append the name to the list of names
  print("|", " | ".join(names), "|")                                  # Print the list of names in a formatted way






#Cleaned text in "Cleaned" folder

def folder_cleaned() -> bool:                       # Defines a function named "folder_cleaned" that takes no parameter
  """
  IN : None
  Out : bool, True to confirm the folder has been created or formated
  Description : Create a folder named "Cleaned" if it doesn't exist, and delete all the files in it if it does already exist
  """
  path_dir = 'Cleaned'                              # Path of the folder we want to create or format 
  if os.path.exists(path_dir):                      # If the folder already exists

    list_of_files_name = os.listdir(path_dir)       # List of the files in the folder
    for file in list_of_files_name:                 # For each file in the folder
      file_path = os.path.join(path_dir, file)      # Path of the file
      os.remove(file_path)                          # Delete the file
                                                   
  else:                                             # If the folder doesn't exist
    os.mkdir(path_dir)                              # Create the folder

  return True                                       # Return True to confirm the folder has been created or formated




def file_cleaned()-> bool:                          # Defines a function named "file_cleaned" that takes no parameter
  """
  IN : None
  OUT : bool, True to confirm the files have been cleaned
  Description : Clean the files in the "Speeches" folder and write the cleaned files in the "Cleaned" folder
  """
  acc = {'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a', 'ù': 'u', 'û': 'u', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'œ': 'oe', 'ç': 'c', 'É': 'E', 'È': 'E', 'Ê': 'E', 'À': 'A', 'Â': 'A', 'Ù': 'U', 'Û': 'U', 'Î': 'I', 'Ï': 'I', 'Ô': 'O', 'Ö': 'O', 'Œ': 'OE'}

  path_file_orgl = "Speeches"                                                          # Original path
  path_file_prime = "Cleaned"                                                          # New path

  for file_name in os.listdir(path_file_orgl):                                         # For the file in the original folder do :
    path_file_orgl = "Speeches"                                                        # Original path
    path_file_prime = "Cleaned"  
    path_file_orgl = os.path.join(path_file_orgl, file_name)                           # path_file_orgl\file_name
    path_file_prime = os.path.join(path_file_prime,file_name)                          # path_file_prime\file_name
    #print(path_file_orgl)
    #print(path_file_prime)

    with open(path_file_orgl, 'r', encoding='utf-8') as file_orgl, open(path_file_prime, 'w', encoding='utf-8') as file_prime:
      lines = file_orgl.readlines()                                                    # "Read" each line of the orginal and return them as a list of str (a line = an element)

      for line in lines:                                                               # For each line in the list of lines
        cleaned_line = ""                                                              # Create an empty str to store the cleaned line

        for character in line:                                                         # For each character in each line
          formatted_character = character.lower()                                      # Lower the character A -> a

          if formatted_character in ("'", "-","\n"):                                   # If the character is a special character
            formatted_character = " "                                                  # Replace it by a space

          elif formatted_character in (".", ",", ":", ";", "!", "?"):                  # If the character is a new line
            formatted_character = ""                                                   # Delete it            

          for key, value in acc.items():                                               # For each key and value in the acc dictionary
            formatted_character = formatted_character.replace(key, value)              # Replace a special character by a "normal" one

          cleaned_line += formatted_character                                          # Add the cleaned character to the cleaned line

        file_prime.write(cleaned_line)                                                 # Re-write the lowered character in the new file

  return True



def tf(file_path : str, folder : str) -> dict:                                          # Defines a function named "tf" that takes two parameters: "file_path" and "folder"
  """
  IN : str, the file path & str, the path of the folder
  OUT : dict, the frequency of each word in the text file
  Description : Calculate how many times a word appears in a text file
  """
  assert type(file_path) == str and file_path != "" and type(folder) == str and folder != "", "Insert a valid str file path and folder" #Checks if the file path and the folder are str
  frequency = {}                                                                        # Create an empty dictionary to store the word frequencies
  with open(os.path.join(folder, file_path), 'r', encoding = 'utf-8') as file:          # Open the file in read mode with UTF-8 encoding
    text = file.read()                                                                  # Read the contents of the file
    words = text.split()                                                                # Split the text into individual words
    for word in words:                                                                  # Iterate over each word in the text
      
      if word not in frequency:                                                         # Check if the word is not already in the frequency dictionary
        frequency[word] = 1                                                             # If not, initialize the frequency of the word to 1
      
      else:                                                                             # If the word is already in the frequency dictionary
        frequency[word] += 1                                                            # Increment its frequency by 1
    frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True)) # Sort the frequency dictionary by value in descending order
    return frequency                                                                    # Return the dictionary of word frequencies






def idf(folder : str) -> dict:                                                                  # Defines a function named "idf" that takes one parameter: "folder"
  """
  IN : str, the path of the folder
  OUT : dict, the idf of each word in the folder
  Description : Function that takes a folder as input and returns a dictionary of the idf of each word in the folder
  """
  assert type(folder) == str and folder != "", "Insert a valid str folder"                     #Checks if the folder is a str
  idf_dict = {}                                                                                 # Create an empty dictionary to store the IDF values
  nb = len(os.listdir(folder))                                                                  # Initialize a counter variable to keep track of the number of files
  word_in_docs = {}                                                                             # Create an empty dictionary to store the number of documents containing each word

  for files in os.listdir(folder):                                                              # Iterate over each file in the specified folder
    with open(os.path.join(folder, files), 'r', encoding = 'utf-8') as file:                    # Open the file in read mode with UTF-8 encoding
      words = set(file.read().split())                                                          # Use a set to get unique words in the document
      
      for word in words:                                                                        # Iterate over each word in the document
        if word in word_in_docs:                                                                # Check if the word is already in the word_in_docs dictionary
          word_in_docs[word] += 1                                                               # If yes, increment the number of documents containing the word by 1
        else:                                                                                   # If not
          word_in_docs[word] = 1                                                                # If not, initialize the number of documents containing the word to 1

  for word, count in word_in_docs.items():                                                      # Iterate over each word in the word_in_docs dictionary
    idf_dict[word] = log(nb / count)                                                            # Calculate the IDF of the word and store it in the IDF dictionary
  
  idf_dict = dict(sorted(idf_dict.items(), key=lambda item: item[1], reverse=True))             # Sort the idf_dict by value in descending order
  return idf_dict                                                                           # Return the IDF dictionary


def calculate_tfidf(folder):
  assert type(folder) == str and folder != "", "Insert a valid str folder"              #Checks if the folder is a str
  idf_values = idf(folder)                                                              # Get the IDF values of the words in the folder
  tfidf_matrix = []                                                                     # Create an empty list to store the TF-IDF values of the words in the folder

  for filename in os.listdir(folder):                                                   # Iterate over each file in the folder
    tf_values = tf(filename, folder)                                                    # Get the TF values of the words in the file

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
          tfidf_matrix.append([key, [idf_values[key] * tf_values[key]]])                # If yes, append the word and its TF-IDF value to the TF-IDF matrix
        
        else:                                                                           # If not
          tfidf_matrix.append([key, [0]])                                               # Append the word and 0 to the TF-IDF matrix
  
  return tfidf_matrix                                                                   # Return the TF-IDF matrix


  




#1. Display the list of least important words in the document corpus. 
#A word is said to be unimportant if its TD-IDF = 0 in all files.
#2. Display the word(s) with the highest TD-IDF score
#3. Indicate the most repeated word(s) by President Chirac
#4. Indicate the name(s) of the president(s) who spoke of the "Nation" and the one who repeated it the most
#times.
#5. Identify the first president to talk about climate (“climat”) and/or ecology (“écologie”)
#6. Excepti the so-called "unimportant" words, which word(s) did all the president mention?

def least_imp_words(tfidf_matrix : list) -> list:                                       # Defines a function named "least_imp_words" that takes one parameter: "tfidf_matrix"
  """
  IN : list of lists, the tfidf matrix
  OUT : list of lists, the least important words
  Description : Function that takes a tfidf matrix as input and returns a list of the least important words
  """
  assert type(tfidf_matrix) == list and tfidf_matrix != [], "Insert a valid list tf-idf matrix" #Checks if the tfidf matrix is a list
  nbr_words_display = int(input("How many words do you want to display ?"))             # Ask the user how many words he wants to display
  liw_list = []                                                                         # Create an empty list to store the least important words
  tfidf_matrixpop = tfidf_matrix                                                        # Create a copy of the TF-IDF matrix to avoid modifying the original matrix

  for word in tfidf_matrix:                                                             # Iterate over each word in the TF-IDF matrix
    min_tfidf = min(tfidf_matrix, key=lambda x: min(x[1]))                              # Get the word with the minimum TF-IDF value
    del tfidf_matrixpop[tfidf_matrix.index(min_tfidf)]                                  # Delete the word from the TF-IDF matrix
    liw_list.append(min_tfidf)                                                          # Append the word to the list of least important words
  
  return liw_list[:nbr_words_display]                                                   # Return the list of least important words


def most_imp_words(tfidf_matrix : list) -> list:                                        # Defines a function named "most_imp_words" that takes one parameter: "tfidf_matrix"
  """
  IN : list of lists, the tfidf matrix
  OUT : list of lists, the most important words
  Description : Function that takes a tfidf matrix as input and returns a list of the most important words
  """
  assert type(tfidf_matrix) == list and tfidf_matrix != [], "Insert a valid list tf-idf matrix" #Checks if the tfidf matrix is a list
  nbr_words_display = int(input("How many words do you want to display ?"))             # Ask the user how many words he wants to display
  miw_list = []                                                                         # Create an empty list to store the most important words
  tfidf_matrixpop = tfidf_matrix                                                        # Create a copy of the TF-IDF matrix to avoid modifying the original matrix
  
  for word in tfidf_matrix:                                                             # Iterate over each word in the TF-IDF matrix
    max_tfidf = max(tfidf_matrix, key=lambda x: max(x[1]))                              # Get the word with the maximum TF-IDF value
    del tfidf_matrixpop[tfidf_matrix.index(max_tfidf)]                                  # Delete the word from the TF-IDF matrix
    miw_list.append(max_tfidf)                                                          # Append the word to the list of most important words

  return miw_list[:nbr_words_display]                                                   # Return the list of most important words






def most_repeated_words_by(president: str, folder: str) -> str :
  """
  IN : str, the name of the president & str, the path of the folder
  OUT : str, the most repeated words by the president
  Description : Function that takes a president and a folder as input and returns a string of the most repeated words by the president
  """
  assert type(president) == str and president != "" and type(folder) == str and folder != "", "Insert a valid str president and folder" #Checks if the president and the folder are str
  president_speeches = [i for i in os.listdir(folder) if president in i]            # Get the list of the president's speeches
  most_repeated_words = []                                                          # Create an empty list to store the most repeated words
  nbr_words_display = int(input("How many words do you want to display ?"))         # Ask the user how many words he wants to display

  for text in president_speeches:                                                   # Iterate over each speech of the president
    tf_values = tf(text, folder)                                                    # Get the TF values of the words in the speech

    for _ in range(len(tf_values)):                                                 # Iterate over each word in the TF dictionary
      max_word = max(tf_values, key=tf_values.get)                                  # Get the word with the maximum TF value
      most_repeated_words.append(max_word)                                          # Append the word to the list of most repeated words
      del tf_values[max_word]                                                       # Delete the word from the TF dictionary

  return f"The most repeated words by {president} are {', '.join(most_repeated_words[:nbr_words_display])}" # Return the string of the most repeated words by the president


def mentioned_nation(folder : str) -> str:
  """
  IN : str, the path of the folder
  OUT : str, the president(s) who mentioned the word "Nation"
  Description : Function that takes a folder as input and returns a string of the president(s) who mentioned the word "Nation"
  """
  assert type(folder) == str and folder != "", "Insert a valid str folder" #Checks if the folder is a str
  presidents_mentioning_nation = []                                                                 # Create an empty list to store the presidents who mentioned the word "Nation"
  
  for text in os.listdir(folder):                                                                   # Iterate over each file in the folder
    with open(os.path.join(folder, text), 'r', encoding='utf-8') as file:                           # Open the file in read mode with UTF-8 encoding
      doc = file.read()                                                                             # Read the contents of the file
      
      if 'nation' in doc and president_last_name(text) not in presidents_mentioning_nation:         # Check if the word "Nation" is in the file and if the president is not already in the list of presidents who mentioned the word "Nation"
        presidents_mentioning_nation.append(president_last_name(text))                              # If yes, append the president to the list of presidents who mentioned the word "Nation"

  return f"The word nation was mentioned by {', '.join(presidents_mentioning_nation)}."             # Return the string of the president(s) who mentioned the word "Nation"


def mentioned_climate(folder : str)-> str :
  """
  IN : str, the path of the folder
  OUT : str, the first president to mention the word "Climate"
  Description : Function that takes a folder as input and returns a string of the first president to mention the word "Climate"
  """
  assert type(folder) == str and folder != "", "Insert a valid str folder"                                              #Checks if the folder is a str
  presidents_mentioning_climate = []                                                                                    # Create an empty list to store the presidents who mentioned the word "Climate"
  
  for text in os.listdir(folder):                                                                                       # Iterate over each file in the folder
    with open(os.path.join(folder, text), 'r', encoding='utf-8') as file:                                               # Open the file in read mode with UTF-8 encoding
      doc = file.read()                                                                                                 # Read the contents of the file

      if ('ecologie' in doc or 'climat' in doc) and president_last_name(text) not in presidents_mentioning_climate:     # Check if the word "Ecologie" or "Climat" is in the file and if the president is not already in the list of presidents who mentioned the word "Climate"
        presidents_mentioning_climate.append(president_last_name(text))                                                 # If yes, append the president to the list of presidents who mentioned the word "Climate"

  return f"The word ecologie/climat was mentioned by {', '.join(presidents_mentioning_climate)}."                       # Return the string of the first president to mention the word "Climate"



#6
def words_mentioned_by_all_presidents(folder : str)-> str :                         # Defines a function named "words_mentioned_by_all_presidents" that takes one parameter: "folder"
  """
  IN : str, the path of the folder
  OUT : str, the words mentioned by all presidents
  Description : Function that takes a folder as input and returns a string of the words mentioned by all presidents
  """
  assert type(folder) == str and folder != "", "Insert a valid str folder"          #Checks if the folder is a str
  matrix = calculate_tfidf(folder)                                                  # Get the TF-IDF matrix of the folder
  words = []                                                                        # Create an empty list to store the words mentioned by all presidents
  
  for word in matrix:                                                               # Iterate over each word in the TF-IDF matrix
    
    if word[1] == [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0] :                               # Check if the word is mentioned by all presidents
      words.append(word[0])                                                         # If yes, append the word to the list of words mentioned by all presidents
  
  return f"The words mentioned by all presidents are {', '.join(words)}."           # Return the string of the words mentioned by all presidents