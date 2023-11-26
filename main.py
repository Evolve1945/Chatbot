import os
import math



#PART I
print("PART I\n")



#VARIABLES
dict_president_full_name = {"Chirac" : "Jacques", "Giscard dEstaing" : "Gilles", "Hollande" : "François", "Macron" : "Emmanuel", "Sarkozy" : "Nicolas", "Mitterrand" : "François"}

directory = "Speeches"


#FUNCTIONS

def list_of_files(directory, extension):
  files_names = []
  for filename in os.listdir(directory):
    if filename.endswith(extension):
      files_names.append(filename)
  return files_names

directory = "./speeches"
files_names = list_of_files(directory, "txt")

#print(files_names)




def president_last_name(file : str) -> str:
  """
  IN : str, the full name of the .txt file, with the extension
  OUT : the name of the president's name giving the speech
  Description : print the president's name present in the title of the file (without the number and the extention file)
  """
  L = os.path.basename(file).split("_") 

  #Split the name of the last file/folder of the
  #path into a list of strs, where we can find the 
  #first element, supposed to be the word "Nomination" 
  #and the second element, the name of the president 
  #with or without a number, following with the extension 
  # of the file, here ".txt"

  cpt = 0
  for i in range (len(L[1].split(".")[0])-1,1,-1) :   #for loop to prevent from the name being followed by a number having more than 1 digit
    if L[1].split(".")[0][i] in "abcdefghijklmnopqrstuvwxyz" and cpt == 0: 
      name = L[1].split(".")[0][:i+1]
      cpt += 1
  return name

#print(president_last_name("Speeches/Nomination_Giscard dEstaing23574657642746246247642464564754.txt"))


def get_names (directory :str) -> list :
  list_of_speeches = []
  for namefile in os.listdir(directory) :
    if namefile.endswith(".txt") :
      speech = president_last_name(os.path.join(namefile))
      if speech not in list_of_speeches :
        list_of_speeches.append(speech)
  return list_of_speeches

#print(get_names(directory))



def president_full_names (list_of_files : list) -> None:
  """Function that takes a list of name files as input and prints a string of with all president full names
  IN :
  OUT : 
  """
  global dict_president_full_name                     # Declare a global variable
  names = []                                          # Declare an empty list to store the names
  for text in list_of_files :                         
    name = dict_president_full_name[text]+ " " + text # Concatenate the president's first name and last name
    names.append(name)                                # Append the name to the list of names
  print("|", " | ".join(names), "|")                  # Print the list of names in a formatted way




#Cleaned text in "Cleaned" folder

def folder_cleaned() -> bool:
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
    
    
    with open(path_file_orgl, 'r', encoding='utf-8') as file_orgl, open(path_file_prime, 'w', encoding='utf-8') as file_prime :
      lines = file_orgl.readlines()                           # "Read" each line of the orginal and return them as a list of str (a line = an element)
      
      for line in lines:  
        cleaned_line = ""  
        
        for character in line:                                # For each character in each line
          formatted_character = character.lower()             # Lower the character A -> a
      
          if formatted_character in ("'", "-",):               # if f_chr = ! . ? , ; :
              formatted_character = " "
          elif formatted_character in (".", ",", ":", ";", "!", "?"):       
              formatted_character = ""
          
          for key, value in acc.items():
            formatted_character = formatted_character.replace(key, value) # Replace a special character by a "normal" one
          
          cleaned_line += formatted_character
          

        file_prime.write(cleaned_line)                 # Re-write the lowered character in the new file

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

def tf(text : str) -> dict:
  """
  Calculate how many times a word appears in a text
  """
  frequency = {}

  for word in range(len(text)):
    if text[word] not in frequency:
      frequency[word] = 0

    else:
      frequency[word] += 1

  frequency = dict(sorted(frequency.items(), key = lambda item : item[0]))
  return frequency





def idf(directory : str) -> dict:

  idf_dict = {}
  nb = 0

  for files in os.listdir(directory):
      
      with open(os.path.join(directory, files), 'r', encoding = 'utf-8') as file:
        nb += 1
        words = file.read().split
        frequency = tf(words)

        for word in frequency:
          idf_dict[word] = math.log(nb / frequency[word])


  return idf_dict

"""
def calculate_tfidf(text, folder):
  tfidf = {}
  tf = tf(text)
  idf = idf(folder)

  for word in tf.keys():
    pass
"""

def tf_idf_matrix( directory : str) -> dict:
  """
  Takes the files' directory and return a matrix
  """

  tf_idf_matrix = []

  for file in os.listdir(directory):

    with open(os.path.join(directory, file), 'r', encoding = 'utf_8') as files:

      tf_freq = tf(file.read().split())
      idf_freq = idf(directory)
      tf_idf_freq = []
      tf_idf_dict = {}

      for word in tf_freq:

        if word in idf_freq:
          tf_idf_freq = tf_freq[word] * idf_freq[word]
          tf_idf_freq.append(tf_idf_freq)
          tf_idf_freq_dict = tf_idf_freq

      tf_idf_matrix.append(tf_idf_freq)
      tf_idf_dict[file] = tf_idf_dict

  for file, tf_idf_freq_dict in tf_idf_dict.items():
    tf_idf_freq_dict['tf_idf_matrix'] = tf_idf_matrix

  return tf_idf_dict

#1
def least_imp_words(tf_idf_dict):
  """
  Get all words the find those which have a tf-idf == 0 in all files
  """
  words = []
  liw = []

  for document in tf_idf_dict :
    liw.update(tf_idf_dict[words])

  for word in words:
    unimportant = True

    for document in tf_idf_dict:

      if tf_idf_dict[document] and tf_idf_dict[document][word] != 0:
        unimportant = False

    if unimportant:
      least_imp_words.append(word)

  return word


"""
def important_words():
  most_important_words = []
  for word in text:
    if calculate_tfidf(word) == max(calculate_tfidf(text)):
      most_important_words.add(word)
  return most_important_words


  
# CALL
president_full_names(get_names(directory))

folder_cleaned()
file_cleaned()
"""

