import os
import shutil

#PART I
print("PART I\n")

#Variables
dict_president_full_name = {"Chirac" : "Jacques", "Giscard dEstaing" : "Gilles", "Hollande" : "François", "Macron" : "Emmanuel", "Sarkozy" : "Nicolas", "Mitterrand" : "François"}
directory = "Speeches"

#Functions

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
  for i in range (len(L[1].split(".")[0])-1,1,-1) :#for loop to prevent from the name
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
  global dict_president_full_name # Declare a global variable
  names = [] # Declare an empty list to store the names
  for text in list_of_files : # Loop through the list of files we gave as paramaters
    name = dict_president_full_name[text]+ " " + text # Concatenate the president's first name and last name
    names.append(name) # Append the name to the list of names
  print("|", " | ".join(names), "|") # Print the list of names in a formatted way




def folder_cleaned() -> bool:
  """
  IN : None
  Out : bool, True
  Description : Create a folder named "Cleaned" if it doesn't exist, and delete all the files in it if it does already exist
  """
  # Defined the path
  dirname = os.path.dirname  # Get the directory name from the path
  path_dir = 'Cleaned'  # Set the path of the folder to be checked/created
  
  # Check if the folder exists
  if os.path.exists(path_dir):  # Check if the folder already exists
    
    # If not empty, delete the files
    list_of_files_name = os.listdir(path_dir)  # Get the list of file names in the folder
    for file in list_of_files_name:  # Iterate through the file names
      file_path = os.path.join(path_dir, file)  # Get the full path of the file
      os.remove(file_path)  # Remove the file
    
  # If doesn't exist, create it
  else:  # If the folder doesn't exist
    os.mkdir(path_dir)  # Create the folder

  return True


def cleaned_pt2():
  """
  ...
  Then verify that each chr in txt is well formated
        If no : reformate it
        Then put the chr in the file
  """
  path_file_orgl = "Speeches"
  path_file_prime = "Cleaned"

  for file_name in os.listdir(path_file_orgl):
    path_file_orgl = os.path.join(path_file_orgl, file_name)
    path_file_prime = os.path.join(path_file_prime,file_name)
    
    with open(path_file_orgl, 'r', encoding='utf-8') as file_orgl, open(path_file_prime, 'r', encoding='utf-8') as file_prime :
      lines = file_orgl.readlines()                           # "Read" each line of the orginal
      
      for line in lines:
        formatted_line = line.lower()
        file_prime.write(formatted_line)

  return True






# CALL
president_full_names(get_names(directory))

folder_cleaned()
#cleaned_pt1()
cleaned_pt2()


