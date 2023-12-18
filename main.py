from Part_I import *
from Part_II import *

directory = "Speeches"
new_directory = "Cleaned"
"""
MAIN MENU
"""

def main_menu():
  print("----------------------------------------")
  print("--------------- CHATBOT ----------------")
  print("----------------------------------------")
  print("--- Part I ---")
  print("1. List Presidents' Full Names")
  print("2. Reformat the text and put them in the 'Cleaned' folder")
  print("3. Analyze text and display results")
  print()

  print("--- Part II ---")
  print("4. Rewrite a phrase or a question in a more 'readable' way")
  print("5. Give the list of words in the question and in the text")
  print("6. Give the list of words in the question and in the text with the TF-IDF score")
  print("7. Give the TF-IDF matrix of the question")
  print("8. Give the matrix of similarities between the question and the speeches")
  print("9.Give the most revelant document to answer the question")
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

  elif choice == 6:
    files = os.listdir(new_directory)
    for i in range(len(files)) :
      print(i + 1,".", files[i]) 
    file_path = int(input("Enter the number of the speech to search for the questions words in it : "))
    print(tf_question(files[file_path], new_directory, list_of_words_in_question))

  elif choice == 7:
    word_in_question = words_in_question(input("Enter a question : "))                                                      #Clean the word in the question then put it into a list
    tfidf_matrix_question = calculate_tfidf_question(word_in_question) 
    print(tfidf_matrix_question)

  elif choice == 8:
    word_in_question = words_in_question(input("Enter a question : "))                                                      #Clean the word in the question then put it into a list
    tfidf_matrix_question = calculate_tfidf_question(word_in_question)                                                        
    tfidf_matrix_corpus = calculate_tfidf(new_directory)
    matrix_similarity = matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus)
    print(matrix_similarity)

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



  

run_chatbot()



