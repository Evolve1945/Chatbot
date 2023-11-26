import os
from math import log
# -*- coding: utf-8 -*-

#PART I
print("PART I\n")

#Variables
dict_president_full_name = {"Chirac" : "Jacques", "Giscard dEstaing" : "Gilles", "Hollande" : "François", "Macron" : "Emmanuel", "Sarkozy" : "Nicolas", "Mitterrand" : "François"}
directory = "Speeches"

#Functions

def list_of_files(directory, extension):                      # Defines a function named "list_of_files" that takes two parameters: "directory" and "extension"
  """
  IN : str, the path of the directory & str, the extension of the files we want to get
  OUT : list of strs, the names of the files with the extension we want
  Description : Function that takes a directory and an extension as input and returns a list of the names of the files in the directory with the specified extension
  """
  files_names = []                                            # Creates an empty list named "files_names"
  for filename in os.listdir(directory):                      # Iterates over the files in the specified directory
    if filename.endswith(extension):                          # Checks if the file has the specified extension
      files_names.append(filename)                            # Adds the file name to the "files_names" list
  return files_names                                          # Returns the list of file names
  
directory = "./speeches"
files_names = list_of_files(directory, "txt")

#print(files_names)

def president_last_name(file : str) -> str:                                 # Defines a function named "president_last_name" that takes one parameter: "file"
  """
  IN : str, the full name of the .txt file, with the extension
  OUT : the name of the president's name giving the speech
  Description : print the president's name present in the title of the file (without the number and the extention file)
  """
  L = os.path.basename(file).split("_")                                     #Split the name of the last file/folder of the path into a list of strs, where we can find the first element, supposed   to be the word "Nomination" and the second element, the name of the president with or without a number, following with the extension of the file, here ".txt"
  cpt = 0                                                                   #Counter to prevent from the name being followed by a number having more than 1 digit
  for i in range (len(L[1].split(".")[0])-1,1,-1) :                         #for loop to prevent from the name being followed by a number having more than 1 digit
    if L[1].split(".")[0][i] in "abcdefghijklmnopqrstuvwxyz" and cpt == 0:  #if the last character of the name is a letter and the counter is equal to 0, we have the last character of the name
      name = L[1].split(".")[0][:i+1]                                       #We have the name of the president
      cpt += 1                                                              #Increment the counter to prevent from the name being followed by a number having more than 1 digit
  return name                                                               #Return the name of the president

#print(president_last_name("Speeches/Nomination_Giscard dEstaing23574657642746246247642464564754.txt"))


def get_names (directory :str) -> list :                                    # Defines a function named "get_names" that takes one parameter: "directory"
  """  
  IN : str corresponding to the location of the directory
  OUT : list of strs, all last names which made the speech, without duplicates
  Description : Function to get all the last names of the presidents which speeches are in the folder folder in parameters
  """
  list_of_speeches = []                                                     #Create an empty list to store the names of the presidents
  for namefile in os.listdir(directory) :                                   #Loop through the list of files in the directory            
    if namefile.endswith(".txt") :                                          #Check if the file is a .txt file                     
      speech = president_last_name(os.path.join(namefile))                  #Get the name of the president giving the speech
      if speech not in list_of_speeches :                                   #Check if the name of the president is not already in the list of names
        list_of_speeches.append(speech)                                     #If not, add the name of the president to the list of names
  return list_of_speeches                                                   #Return the list of names

#print(get_names(directory))



def president_full_names (list_of_files : list) -> None:              # Defines a function named "president_full_names" that takes one parameter: "list_of_files"
  """
  IN : list of strs, corresponding to files names
  OUT : None no return
  Description : Function that takes a list of name files as input and prints a string of with all president full names
  """
  global dict_president_full_name                                     # Declare a global variable
  names = []                                                          # Declare an empty list to store the names
  for text in list_of_files :                                         # Loop through the list of files we gave as paramaters
    name = dict_president_full_name[text]+ " " + text                 # Concatenate the president's first name and last name
    names.append(name)                                                # Append the name to the list of names
  print("|", " | ".join(names), "|")                                  # Print the list of names in a formatted way


president_full_names(get_names(directory))



#Cleaned text in "Cleaned" folder

def folder_cleaned() -> bool:                       # Defines a function named "folder_cleaned" that takes no parameter
  """
  IN : None
  Out : bool, True
  Description : Create a folder named "Cleaned" if it doesn't exist, and delete all the files in it if it does already exist
  """
  path_dir = 'Cleaned'                              # Set the path of the folder to be checked/created
  if os.path.exists(path_dir):                      # Check if the folder already exists
    
                                                    # If not empty, delete the files but keep the folder
    list_of_files_name = os.listdir(path_dir)       # Get the list of file names in the folder
    for file in list_of_files_name:                 
      file_path = os.path.join(path_dir, file)      # Get the full path of the file
      os.remove(file_path)                          # Remove the file
                                                   
  else:                                             # If the folder doesn't exist
    os.mkdir(path_dir)                              # Create the folder

  return True




def file_cleaned():
  """
  For folder_cleaned == True :
  ...
  Then verify that each chr in txt is well formated
    If no : reformate it
    Then put the chr in the file
  """
  acc = {'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a', 'ù': 'u', 'û': 'u', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'œ': 'oe', 'ç': 'c', 'É': 'E', 'È': 'E', 'Ê': 'E', 'À': 'A', 'Â': 'A', 'Ù': 'U', 'Û': 'U', 'Î': 'I', 'Ï': 'I', 'Ô': 'O', 'Ö': 'O', 'Œ': 'OE'}

  path_file_orgl = "Speeches"                                 # Original path
  path_file_prime = "Cleaned"                                 # New path

  for file_name in os.listdir(path_file_orgl):                # For the file in the original folder do :
    path_file_orgl = "Speeches"                               # Original path
    path_file_prime = "Cleaned"  
    path_file_orgl = os.path.join(path_file_orgl, file_name)  # path_file_orgl\file_name
    path_file_prime = os.path.join(path_file_prime,file_name) # path_file_prime\file_name
    #print(path_file_orgl)
    #print(path_file_prime)

    with open(path_file_orgl, 'r', encoding='utf-8') as file_orgl, open(path_file_prime, 'w', encoding='utf-8') as file_prime:
      lines = file_orgl.readlines()                           # "Read" each line of the orginal and return them as a list of str (a line = an element)

      for line in lines:  
        cleaned_line = ""  

        for character in line:                                # For each character in each line
          formatted_character = character.lower()             # Lower the character A -> a

          if formatted_character in ("'", "-",):              # if f_chr = ! . ? , ; :
            formatted_character = " "
          elif formatted_character in (".", ",", ":", ";", "!", "?"):       
            formatted_character = ""
          elif formatted_character == "\n":                    # If the character is a new line
            formatted_character = ""                           # Delete it

          for key, value in acc.items():
            formatted_character = formatted_character.replace(key, value) # Replace a special character by a "normal" one

          cleaned_line += formatted_character

        file_prime.write(cleaned_line)                        # Re-write the lowered character in the new file

  return True


"""
1. Display the list of least important words in the document corpus. 
A word is said to be unimportant if its TD-IDF = 0 in all files.
2. Display the word(s) with the highest TD-IDF score
3. Indicate the most repeated word(s) by President Chirac
4. Indicate the name(s) of the president(s) who spoke of the "Nation" and the one who repeated it the most
times.
5. Identify the first president to talk about climate (“climat”) and/or ecology (“écologie”)
6. Excepti the so-called "unimportant" words, which word(s) did all the president mention?
"""

def tf(text : str) -> dict:                                                             # Defines a function named "tf" that takes one parameter: "text"
  """IN : str, the text
  OUT : dict, the frequency of each word in the text
  Description : Calculate how many times a word appears in a text
  """
  frequency = {}                                                                        # Create an empty dictionary to store the word frequencies
  text = text.split(" ")                                                                # Split the text into individual words
  for word in text:                                                                     # Iterate over each word in the text
    if word not in frequency:                                                           # Check if the word is not already in the frequency dictionary
      frequency[word] = 1                                                               # If not, initialize the frequency of the word to 1
    else:
      frequency[word] += 1                                                              # If the word is already in the frequency dictionary, increment its frequency by 1
  frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))   # Sort the frequency dictionary by word in descending order
  return frequency                                                                      # Return the dictionary of word frequencies






def idf(folder : str) -> dict:                                                                  # Defines a function named "idf" that takes one parameter: "folder"
  """
  IN : str, the path of the folder
  OUT : dict, the idf of each word in the folder
  Description : Function that takes a folder as input and returns a dictionary of the idf of each word in the folder
  """
  
  idf_dict = {}                                                                                 # Create an empty dictionary to store the IDF values
  nb = 0                                                                                        # Initialize a counter variable to keep track of the number of files
  
  for files in os.listdir(folder):                                                              # Iterate over each file in the specified folder
    with open(os.path.join(folder, files), 'r', encoding = 'utf-8') as file:                    # Open the file in read mode with UTF-8 encoding
      nb += 1                                                                                   # Increment the counter variable
      words = file.read()                                                                       # Read the contents of the file
      frequency = tf(words)                                                                     # Calculate the term frequency (TF) for each word in the file
      for word in frequency:                                                                    # Iterate over each word in the frequency dictionary
        idf_dict[word] = log(nb / frequency[word])                                              # Calculate the IDF value for the word and store it in the IDF dictionary
  return idf_dict                                                                               # Return the IDF dictionary


def calculate_tfidf(text, folder):
  tfidf = {}
  tf = tf(text)
  idf = idf(folder)

  for word in tf.keys():
    tfidf[word] = tf[word] * idf[word]

  total_idf = sum(idf.values())  # Calculate the total final idf

  return tfidf, total_idf
"""
def unimportant_words():
  least_important_words = []
  for word in text:
    if calculate_tfidf(word) == 0:
      least_important_words.add(word)
  return least_important_words
    
    
def important_words():
  most_important_words = []
  for word in text:
    if calculate_tfidf(word) == max(calculate_tfidf(text)):
      most_important_words.add(word)
  return most_important_words

"""
  
# CALL
president_full_names(get_names(directory))

folder_cleaned()
file_cleaned()

print(tf("Speeches mommy car car car bobby vive la france la France est un beau pays il faut se réveiller et aller travailler pour la france".lower()))
print(idf("Cleaned"))