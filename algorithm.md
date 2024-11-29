# Algorithm Document

functions we need to make:

1. storing conversion info from morse code into a dictionary
2. read the morse code text from a file
3. convert morse code text into english (maybe could be same function as #3)
4. main



Name: file_input_error
Purpose: check if the file inputted by user exists
Parameters: none
Return: none
Algorithm:
1. ask user to input the name of file to read from
2. create a try:
   1. if the file exists:
      1. open the file for reading
3. except: 
   1. output error to user that file does not exist


Name: morse_dictionary
Purpose: create a dictionary containing morse code characters and what character they represent
Parameters: 
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


Name:
Purpose:
Parameters:
Return:
Algorithm:

