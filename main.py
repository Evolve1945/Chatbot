import os

directory = "Speeches"
#PART I
print("PART I\n")

#Variables
dict_president_full_name = {"Chirac" : "Jacques", "Giscard dEstaing" : "Gilles", "Hollande" : "François", "Macron" : "Emmanuel", "Sarkozy" : "Nicolas", "Mitterrand" : "François",1 : "donut"}


#Functions

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

#Test bonjour
print(president_last_name("Speeches/Nomination_Giscard dEstaing23574657642746246247642464564754.txt"))



def get_names (directory :str) -> list :
  list_of_speeches = []
  for namefile in os.listdir(directory) :
    if namefile.endswith(".txt") :
      speech = president_last_name(os.path.join(namefile))
      if speech not in list_of_speeches :
        list_of_speeches.append(speech)
  return list_of_speeches

print(get_names(directory))

def president_full_names (list_of_files : list) -> str:
  global dict_president_full_name
  for text in list_of_files :
    name = dict_president_full_name[text]+ " " + name
    print(name)


print(president_full_names(get_names(directory)))
