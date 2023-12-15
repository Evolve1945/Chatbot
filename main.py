from Part_I import *
from Part_II import *

directory = "Speeches"
new_directory = "Cleaned"
"""
MAIN MENU
"""

def main_menu():
  print("--- CHATBOT ---")
  print("--- Part I ---")
  print("1. List Presidents' Full Names")
  print("2. Reformat the text and put them in the 'Cleaned' folder")
  print("3. Analyze text and display results")
  print()
  print("--- Part II ---")
  print("4. Rewrite a phrase or a question in a more 'readable' way")
  print("5. Give the list of words in the question and in the text")
  print("0. Exit")

def choice_menu(choice, tf_idf_dict):
  if choice == 1:
    president_full_names(get_names(directory))

  elif choice == 2:
    folder_cleaned()
    file_cleaned()

    print("Texts cleaned and moved to the 'Cleaned' folder")

  elif choice == 3:
    print("--- CHATBOT ---")
    print("--- Part I ---")
    print("1. Display the list of least important words")
    print("2. Display words with the highest TF-IDF score")
    print("3. Display the most used words by president Chirac")
    print("4. Display the name(s) of the president(s) who used the word 'Nation'")
    print("5. Identify the first president to talk about climate")
    print("6. Display the most common word used by all the presidents")
    print("0. Exit")

    second_choice = int(input("Enter the number : "))

    if second_choice == 1:
      print("Least important words : ", least_imp_words(calculate_tfidf(new_directory)))

    elif second_choice == 2:
      print("Most important words : ", most_imp_words(calculate_tfidf(new_directory)))

    elif second_choice == 3:
      president = "Chirac"
      print(f"Most repeated wordss by president {president} : {most_repeated_words_by(president, new_directory)}")

    elif second_choice == 4:
      print("President(s) mentioning the Nation : ", mentioned_nation(new_directory))
    
    elif second_choice == 5:
      print("1st president to mention climate : ", mentioned_climate(new_directory))

    
    elif second_choice == 6:
      print("Words mentionned by every president : ", words_mentioned_by_all_presidents(tf_idf_dict))

    elif second_choice == 0:
      main_menu()

    else :
      print("Invalid")

  elif choice == 4:
    phrase = input("Phrase : ")
    print(words_in_question(phrase))

  elif choice == 5:
    print(question_word_in_corpus(new_directory))

  elif choice == 0:
    print("End.")
    exit()

  else:
    print("Invalid")

def run_chatbot():
  while True:
    main_menu()
    choice = int(input("Enter a number :"))
    choice_menu(choice, directory)



  

#print(files_names)

def president_last_name(file : str) -> str:
  """
  IN : str, the full name of the .txt file, with the extension
  OUT : the name of the president's name giving the speech
  Description : print the president's name present in the title of the file (without the number and the extention file)
  """
  L = os.path.basename(file).split("_") 
  """
  Split the name of the last file/folder of the path into a list of strs, where we can 
  find the first element, supposed   to be the word "Nomination" and the second element, 
  the name of the president with or without a number, following with the extension of 
  the file, here ".txt"
  """
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


president_full_names(get_names(directory))
run_chatbot()



