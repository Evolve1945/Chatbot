import os

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
  file_name = os.path.basename(file).split("_") 
  #Split the name of the last file/folder of the
  #path into a list of strs, where we can find the first element, supposed   to be the
  #word "Nomination" and the second element, the name of the president with or without
  #a number, following with the extension of the file, here ".txt"
  cpt = 0
  for i in range (len(file_name[1].split(".")[0])-1,1,-1) :#for loop to prevent from the name
  #being followed by a number having more than 1 digit
    if file_name[1].split(".")[0][i] in "abcdefghijklmnopqrstuvwxyz" and cpt == 0: 
      name = file_name[1].split(".")[0][:i+1]
      cpt += 1
  return name

#print(president_last_name("Speeches/Nomination_Giscard dEstaing23574657642746246247642464564754.txt"))


def get_names (directory :str) -> list :
  """  
  IN : str corresponding to the location of the directory
  OUT : list of strs, all last names which made the speech, without duplicates
  Description : Function to get all the last names of the presidents which speeches are in the folder folder in parameters
  """
  list_of_speeches = []
  for namefile in os.listdir(directory) :
    if namefile.endswith(".txt") :
      speech = president_last_name(os.path.join(namefile))
      if speech not in list_of_speeches :
        list_of_speeches.append(speech)
  return list_of_speeches

#print(get_names(directory))



def president_full_names (list_of_files : list) -> None:
  """
  IN : list of strs, corresponding to files names
  OUT : None no return
  Description : Function that takes a list of name files as input and prints a string of with all president full names
  """
  global dict_president_full_name # Declare a global variable
  names = [] # Declare an empty list to store the names
  for text in list_of_files : # Loop through the list of files we gave as paramaters
    name = dict_president_full_name[text]+ " " + text # Concatenate the president's first name and last name
    names.append(name) # Append the name to the list of names
  print("|", " | ".join(names), "|") # Print the list of names in a formatted way


president_full_names(get_names(directory))


def folder_cleaned():
  """
  Check if it exists a folder "Cleaned" 
    if no : create it
    if yes : verify if it's empty
      if no : delete the files inside of it
      return True

  """
  #rmv = os.rmdir
  dirname = os.path.dirname                 #Give the name of the folder
  path_dir = 'Chatbot/Cleaned'

  if dirname == "Cleaned" in "./Chatbot":   #Verify if the folder already exists
    for files in os.listdir(path_dir):      #Yes : Remove the files
      os.remove(os.path.join(path_dir, files))
  else:                                     #Create a new folder
    os.mkdir("Cleaned")

  return True
    


def cleaned_pt1():
  """
  folder_cleaned True
    Ask if the file prime already exists
      if yes : delete it then create a new one
      if no : create one
      ...
  """
  path_file_orgl = "/Chatbot/Speeches"
  path_file_prime = "/Chatbot/Cleaned"

  if "/Cleaned" in directory:
    for file in "/Speeches" :
      if file in "/Cleaned" and file in "/Speeches":
        os.remove(os.path.join(path_file_orgl, file))
      else:
        os.open(path_file_prime, 'w')



def cleaned_pt2():
  """
  ...
  Then verify that each chr in txt is well formated
        If no : reformate it
        Then put the chr in the file
  """
  pass
