from Part_I import *
from Part_II import *

directory = "Speeches"
new_directory = "Cleaned"
"""
MAIN MENU
"""

def main_menu():
  print("-----------------------------------------------------------------------------------------------")
  print("------------------------------------------- CHATBOT -------------------------------------------")
  print("-----------------------------------------------------------------------------------------------")

  print("--- Part I ---")
  print("1. List Presidents' Full Names")
  print("2. Reformat the text and put them in the 'Cleaned' folder")
  print("3. Analyze text and display results")
  print()

  print("--- Part II ---")
  print("-------------------------------------- IMPORTANT MESSAGE --------------------------------------")
  print("!!! This section doesn't answer your question, it is just to show you how the chatbot works !!!")
  print("-----------------------------------------------------------------------------------------------")
  print()
  print("----------------------------------------- HOW IT WORKS ----------------------------------------")
  print("4. Rewrite a phrase or a question in a more 'readable' way")
  print("5. Give the list of words in the question and in the text")
  print("6. Give the list of words in the question and in the text with the TF-IDF score")
  print("7. Give the TF-IDF matrix of the question")
  print("8. Give the matrix of similarities between the question and the speeches")
  print("9. Give the most revelant document to answer the question")
  print("10. Take the most revelant file in the folder 'Cleaned' and give that same file from the folder 'Speeches'")
  print("11. Give the most relevant word in your question")
  print("12. Give you the most relevant answer")
  print()
  print("--------------------------------------------CHATBOT--------------------------------------------")
  print("13. Ask a question to the chatbot, get an answer")
  print()
  print("0. Exit")

def choice_menu(choice, tf_idf_dict):
  if choice == 1:
    display_president_full_name = president_full_names(get_names(directory))
    print("Presidents' Full Names : ", display_president_full_name)

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
    print()
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
    phrase = input("Enter your question, to have your question cleaned (you will not get an answer here) : ")
    print(words_in_question(phrase))

  elif choice == 5:
    print(question_word_in_corpus(new_directory))

  elif choice == 6:
    files = os.listdir(new_directory)
    for i in range(len(files)) :
      print(i + 1,".", files[i]) 
    file_path = int(input("Enter the number of the speech to search for the questions words in it : "))
    tf_of_question = tf_question(files[file_path], new_directory, list_of_words_in_question)
    print("Here the TF matrix of the question : ", tf_of_question)

  elif choice == 7:
    word_in_question = words_in_question(input("Enter a question : "))                                                     
    tfidf_matrix_question = calculate_tfidf_question(word_in_question) 
    print("Here the TD-IDF matrix of the question : ", tfidf_matrix_question)

  elif choice == 8:
    word_in_question = words_in_question(input("Enter a question : "))                                                     
    tfidf_matrix_question = calculate_tfidf_question(word_in_question)                                                        
    tfidf_matrix_corpus = calculate_tfidf(new_directory)
    matrix_similarity = matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus)
    print( "Here the matrix of similarities for each word in the question and text : ", matrix_similarity)

  elif choice == 9:
    word_in_question = words_in_question(input("Enter a question : "))                                       
    tfidf_matrix_question = calculate_tfidf_question(word_in_question)                                                        
    tfidf_matrix_corpus = calculate_tfidf(new_directory)
    list_names_files_corpus = list_of_files(new_directory, ".txt")
    matrix_similarity = matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus)
    most_relevant_document_index = most_relevant_document(matrix_similarity, list_names_files_corpus)  
    print("The most relevant document is : ", most_relevant_document_index)

  elif choice == 10:
    word_in_question = words_in_question(input("Enter a question : "))                                                  
    tfidf_matrix_question = calculate_tfidf_question(word_in_question)                                                        
    tfidf_matrix_corpus = calculate_tfidf(new_directory)
    list_names_files_corpus = list_of_files(new_directory, ".txt")
    matrix_similarity = matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus)
    most_relevant_document_index = most_relevant_document(matrix_similarity, list_names_files_corpus)  
    equivalent_file_path = equivalent_text(most_relevant_document_index, list_of_files(directory, ".txt"))
    print("The equivalent file is the n°", equivalent_file_path, "in the folder 'Speeches'")

  elif choice == 11:
    word_in_question = words_in_question(input("Enter a question : "))                                                      
    tfidf_matrix_question = calculate_tfidf_question(word_in_question)                                                        
    tfidf_matrix_corpus = calculate_tfidf(new_directory)
    list_names_files_corpus = list_of_files(new_directory, ".txt")
    matrix_similarity = matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus)
    most_relevant_document_index = most_relevant_document(matrix_similarity, list_names_files_corpus)  
    equivalent_file_path = equivalent_text(most_relevant_document_index, list_of_files(directory, ".txt"))
    most_revelant_word = highest_tfidf_score(equivalent_file_path, tfidf_matrix_question,word_in_question)                                                                #Get the word with the highest tfidf score of the most relevant document
    print("The most revelant word is : ", most_revelant_word)

  elif choice == 12:
    word_in_question = words_in_question(input("Enter a question : "))                                                      
    tfidf_matrix_question = calculate_tfidf_question(word_in_question)                                                        
    tfidf_matrix_corpus = calculate_tfidf(new_directory)
    list_names_files_corpus = list_of_files(new_directory, ".txt")
    matrix_similarity = matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus)
    most_relevant_document_index = most_relevant_document(matrix_similarity, list_names_files_corpus)  
    equivalent_file_path = equivalent_text(most_relevant_document_index, list_of_files(directory, ".txt"))
    most_revelant_word = highest_tfidf_score(equivalent_file_path, tfidf_matrix_question,word_in_question)                                                                #Get the word with the highest tfidf score of the most relevant document
    un_cleaned_phrase = first_occurrence_in_text(most_revelant_word, most_relevant_document_index)
    print("The most revelant answer is : ", un_cleaned_phrase)
   
  elif choice == 13:
    word_in_question = words_in_question(input("Enter a question : "))                                                    
    tfidf_matrix_question = calculate_tfidf_question(word_in_question)                                                        
    tfidf_matrix_corpus = calculate_tfidf(new_directory)
    list_names_files_corpus = list_of_files(new_directory, ".txt")
    matrix_similarity = matrix_cosine_similarity(tfidf_matrix_question, tfidf_matrix_corpus)
    most_relevant_document_index = most_relevant_document(matrix_similarity, list_names_files_corpus)  
    equivalent_file_path = equivalent_text(most_relevant_document_index, list_of_files(directory, ".txt"))
    most_revelant_word = highest_tfidf_score(equivalent_file_path, tfidf_matrix_question,word_in_question)                                                            
    un_cleaned_phrase = first_occurrence_in_text(most_revelant_word, most_relevant_document_index)
    print(cleaned_response(word_in_question, un_cleaned_phrase))


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