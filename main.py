from Functions import *

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
      print("Least important words : ", least_imp_words("Cleaned"))

    elif second_choice == 2:
      print("Most important words : ", most_imp_words("Cleaned"))

    elif second_choice == 3:
      president = "Chirac"
      print(f"Most repeated wordss by president {president} : {most_repeated_words_by(president, 'Cleaned')}")

    elif second_choice == 4:
      print("President(s) mentioning the Nation : ", mentioned_nation('Cleaned'))
    
    elif second_choice == 5:
      print("1st president to mention climate : ", mentioned_climate('Cleaned'))

    
    elif second_choice == 6:
      print("Words mentionned by every president : ", words_mentioned_by_all_presidents(tf_idf_dict))

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
    choice_menu(choice, "Speeches")



  
# CALL
president_full_names(get_names("Speeches"))

#print(files_names)
#print(get_names(directory))
#print(most_imp_words(calculate_tfidf("Cleaned")))
#print(words_mentioned_by_all_presidents("Cleaned"))
#print(mentioned_climate("Cleaned"))
#print(least_imp_words(calculate_tfidf("Cleaned")))

# CALL
#president_full_names(get_names(directory))

#folder_cleaned()
#file_cleaned()

#print(tf("Nomination_Chirac1.txt","Cleaned"))
#print(idf("Cleaned"))

#print(calculate_tfidf("Cleaned"))
#president_full_names(get_names(directory))

#print(president_last_name("Speeches/Nomination_Giscard dEstaing23574657642746246247642464564754.txt"))

#folder_cleaned()
#file_cleaned()
#run_chatbot()



