# Algorithm Document

(delete this after code is finished)
functions we need to make:

1. storing conversion info from morse code into a dictionary
2. read the morse code text from a file
3. convert morse code text into english (maybe could be same function as #3)
4. main


Name: morse_dictionary
Purpose: create a dictionary containing morse code characters and what character they represent
Parameters: none
Return: morse_dict
Algorithm:
1. create a dictionary "morse_dict"
2. read text from morsecode.txt
3. for every line in morsecode.txt:
   1. strip and split every line
   2. the key will equal the second element in the line
   3. the value with equal the first element in the line
   4. add key and corresponding value to dictionary
4. return morse_dict


Name: morse_translator
Purpose: translates the morse code into a readable text
Parameters: none
Return: none
Algorithm:
1. ask user to input the name of file to read from
2. try:
   1. open the file user inputted if it exists
   2. for every line in the file:
      1. strip and split morse_words, (morse_words is the name of elements in each line)
      2. create an empty list called translated_text (this is to store the whole translated text)
      3. for every morse_word in morse_words:
         1. split the morse_word into individual letters
         2. create an empty list called translated_letters (this is to store each translated letter)
            1. for every morse_letter in morse_letters:
            2. translate the letter by searching for the key & value in morse_dict
            3. append the translated letter to the translated_letter list
         3. combine the translated letters into a word
         4. append the translated word to the translated_text list
3. except: 
   1. output error to user that file does not exist


(this one might need a bit of tweaking(delete this after code is finished))
Name: main
Purpose: main function
Parameters: none
Return: none 
Algorithm:
1. output program explanation to user
2. call morse_dictionary
3. create a while loop for translating more than one list
   1. call morse_translator 
   2. output the translated_text list
   3. ask user if they wish to translate another file
4. output goodbye message to user 