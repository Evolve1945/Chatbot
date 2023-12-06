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
          idf_dict[word] = math.log(nb / frequency[word] + 1)


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

#1
def least_imp_words(tf_idf_dict):
  """
  Get all words the find those which have a tf-idf == 0 in all files
  """
  words = []
  least_important_words = []

  for document in tf_idf_dict :
    least_important_words.update(tf_idf_dict[words])

  for word in words:
    unimportant = True

    for document in tf_idf_dict:

      if tf_idf_dict[document] and tf_idf_dict[document][word] != 0:
        unimportant = False

    if unimportant:
      least_important_words.append(word)

  return word


#2
def most_imp_words(tf_idf_dict) -> str:
  most_important_worlds = {}
  for document, tf_idf_freq_dict in tf_idf_dict.items():
    max_freq = max(tf_idf_freq_dict, key = tf_idf_freq_dict.get)
    most_important_worlds[document] == (max_freq, tf_idf_freq_dict[max_freq])

  for word, tfidf in most_important_worlds.items():
    print(f"Word with the highest TF_IDF score : {word} ({tfidf})")


#3
def most_repeated_words_by(president : str, tf_idf_dict):
  
  president_speeches = []
  most_repeated_words = []

  for document in tf_idf_dict:
    if president in document:
      president_speeches.append(document)

  for document in president_speeches:
    max_words = max(tf_idf_dict[document], key = tf_idf_dict[document].get)
    max_words.append(most_repeated_words)

  return most_repeated_words

#4
def mentioned_nation(tf_idf_dict):
  presidents_mentioning_nation = []

  for document in tf_idf_dict:
    if 'Nation' in tf_idf_dict[document]:
      president_name = get_names(document)
      presidents_mentioning_nation.append(president_name)
  return presidents_mentioning_nation

#5
def mentioned_climate(tf_idf_dict):
  for document in tf_idf_dict:
    if 'climat' in tf_idf_dict[document] or 'ecologie' in tf_idf_dict[document]:
      return get_names(document)
    
  return None

#6
def unimportant_words_mentioned(tf_idf_dict):

  common_words = []

  for document in tf_idf_dict:
    first_document = document
  
  for word in tf_idf_dict[first_document]:
    common = True

    for document in tf_idf_dict:
      if word not in tf_idf_dict[document] or tf_idf_dict[document][word] == 0:
        common = False

    if common:
      common_words.append(word)


  return common_words


"""
MAIN MENU
"""

def main_menu():
  print("--- CHATBOT ---")
  print("1. List Presidents' Full Names")
  print("2. Reformat the text and put them in the 'Cleaned' folder")
  print("3. Analyze text and display results")
  print("4. Exit")

def choice_menu(choice, tf_idf_dict):
  if choice == "1":
    president_full_names(get_names(directory))
  elif choice == "2":
    folder_cleaned()
    file_cleaned()

    print("Texts cleaned and moved to the 'Cleaned' folder")

  elif choice == "3":
    print("--- CHATBOT ---")
    print("1. Display the list of least important words")
    print("2. Display words with the highest TF-IDF score")
    print("3. Display the most used words by president Chirac")
    print("4. Display the name(s) of the president(s) who used the word 'Nation'")
    print("5. Identify the first president to talk about climate")
    print("6. Display the most common word used by all the presidents")
    print("7. Exit")

    second_choice = int(input("Enter the number : "))

    if second_choice == 1:
      print("Least important words : ", least_imp_words(tf_idf_dict))

    elif second_choice == 2:
      print("Most important words : ", most_imp_words(tf_idf_dict))

    elif second_choice == 3:
      president = "Chirac"
      print(f"Most repeated wordss by president {president} : {most_repeated_words_by(president, tf_idf_dict)}")

    elif second_choice == 4:
      print("President(s) mentioning the Nation : ", mentioned_nation(tf_idf_dict))
    
    elif second_choice == 5:
      print("1st president to mention climate : ", mentioned_climate(tf_idf_dict))

    
    elif second_choice == 6:
      print("Words mentionned by every president : ", unimportant_words_mentioned(tf_idf_dict))

    elif second_choice == 7:
      main_menu()

    else :
      print("Invalid")


  elif choice == "4":
    print("End.")
    exit()

  else:
    print("Invalid")

def run_chatbot():
  while True:
    main_menu()
    choice = int(input("Enter a number :"))
    choice_menu(choice, tf_idf_dict)



  
# CALL
president_full_names(get_names(directory))

folder_cleaned()
file_cleaned()

td_idf_dict(tf_idf_matrix("./Cleaned"))

run_chatbot()



