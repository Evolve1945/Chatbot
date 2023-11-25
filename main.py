import os
import math



#PART I
print("PART I\n")



#VARIABLES
dict_president_full_name = {"Chirac" : "Jacques", "Giscard dEstaing" : "Gilles", "Hollande" : "François", "Macron" : "Emmanuel", "Sarkozy" : "Nicolas", "Mitterrand" : "François"}
directory = "Speeches"
punct_chr ="?.!,;:"
spe_punct_chr = "-'"
acc = {'a' : "àâä", 'e' : "éèêë", 'i' : "îï", 'o' : "ôö", 'u' : "ûü", 'c' : "ç"}


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
  #path into a list of strs, where we can find the first element, supposed   to be the
  #word "Nomination" and the second element, the name of the president with or without
  #a number, following with the extension of the file, here ".txt"
  cpt = 0
  for i in range (len(L[1].split(".")[0])-1,1,-1) :   #for loop to prevent from the name
                                                      #being followed by a number having more than 1 digit
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
  for text in list_of_files :                         # Loop through the list of files we gave as paramaters
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
  # Defined the path
  
  #dirname = os.path.dirname 
  path_dir = 'Cleaned'                              # Set the path of the folder to be checked/created
  
  if os.path.exists(path_dir):                      # Check if the folder already exists
    
    # If not empty, delete the files but keep the folder
    list_of_files_name = os.listdir(path_dir)       # Get the list of file names in the folder
    for file in list_of_files_name:                 # Iterate through the file names
      file_path = os.path.join(path_dir, file)      # Get the full path of the file
      os.remove(file_path)                          # Remove the file
    
  # If doesn't exist, create it
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
  path_file_orgl = "Speeches"                                 # Original path
  path_file_prime = "Cleaned"                                 # New path

  for file_name in os.listdir(path_file_orgl):                # For the file in the original folder do :
    path_file_orgl = "Speeches"                                 # Original path
    path_file_prime = "Cleaned"  
    path_file_orgl = os.path.join(path_file_orgl, file_name)  # 
    path_file_prime = os.path.join(path_file_prime,file_name) #
    print(path_file_orgl)
    print(path_file_prime)
    
    
    with open(path_file_orgl, 'r', encoding='utf-8') as file_orgl, open(path_file_prime, 'w', encoding='utf-8') as file_prime :
      lines = file_orgl.readlines()                           # "Read" each line of the orginal
      
      for line in lines:  
        cleaned_line = ""  
        
        for character in line:                            # For each character in each line
          formatted_character = character.lower()               # Lower the character A -> a
      
          if formatted_character in punct_chr:
            
            if formatted_character == "'" and cleaned_line and cleaned_line[-1] != ' ':
              cleaned_line += ' ' + formatted_character 
            elif formatted_character == '-':
              cleaned_line += ' '
              
          else:
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

def calculate_tf(text : str) -> dict:
  """
  Calculate how many times a word appears in a text
  """
  occurrence_word = {}
  for word in text:
    if word in occurrence_word:
      occurrence_word[word] += 1
    else:
      occurrence_word = 0
  return occurrence_word


"""
# Besoin idée
def calculate_idf(folder) -> dict:

  cpt_in_text = 0

  for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    with open(file, 'r', encoding = 'utf-8') as file:
      cpt_in_text += 1

      # Faut checker si le mot est présent dans le doc
      #Puis trouver un moyen de calculer idf
      return math.log(cpt / "x fois l occurence du mot" )

def calculate_tfidf(text, folder):
  tfidf = {}
  tf = calculate_tf(text)
  idf = calculate_idf(folder)

  for word in tf.keys():

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


