import os

#PART I
print("PART I\n")

#Variables

dict_president_full_name = {"Chirac" : "Jacques", "Giscard dEstaing" : "Gilles", "Holland" : "François", "Macron" : "Emmanuel", "Sarkozy" : "Nicolas", "Mitterrand" : "François",1 : "donut"}


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

print(president_last_name("Speeches/Nomination_Giscard dEstaing23574657642746246247642464564754.txt"))


def president_all_names(file : str) -> str:
  name = president_last_name(file)
  return dict_president_full_name[name] + " " + name

print(president_all_names("Speeches/Nomination_Giscard dEstaing90868433593.txt"))


#print(dict_president_full_name[1])

for i







