# Chatbot
Chatbot Python Project
KRYLOV Rudolf, POUILLAUDE Agathe

--------------------------------------------------
|               SETUP INSTRUCTION                |
--------------------------------------------------

Download the release as a zip file containing all the code, and extract it to the desired folder. Do NOT tamper with the structure of folders and files once extracted or their names, which would break the program. Tampering with the speeches .txt file with non-unicode characters may also hinder the bot's capacities.

Once done, launch the program by running main.py in any python console interpreter. You may now interact with the program

--------------------------------------------------
|                APP DESCRIPTION                 |
--------------------------------------------------

This ChatBot consists of two separate parts. It bases any of its answers on the investiture speeches of the last 6 French presidents.

****** FIRST PART ******

First, it will be able to review the given corpus and give 6 different results :

    Least important words;
    Words with the highest TF-IDF score (the rarest);
    The most repeated words by president Chirac;
    Names of president who mentions the word nation, and the president who mentions it the most;
    The first president talking about climate in his speech;
    Words which all president mentioned in their speeches.

****** SECOND PART ******

Secondly, it will be able to take into input any user question (NB: In French) and generate an appropriate answer based on the given corpus.

There is a 5s to 10s cooldown before each answer.



Github link : https://github.com/Evolve1945/Chatbot