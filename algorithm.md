# Algorithm Document

(delete this after code is finished)
functions we need to make:

1. storing conversion info from morse code into a dictionary
2. read the morse code text from a file
3. convert morse code text into english (maybe could be same function as #3)
4. main


Name: morse_dictionary  
Purpose: create a dictionary containing morse code characters and what character they represent  
Parameters: filename  
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

Purpose: Read the Morse code text file to decode    
Parameters: filename    
Returns: table    
Name: morse_file    
1. create a table
2. open and read filename using with keyword
   1. for line in file
      1. add the split and striped line to table
   2. return table

Purpose: Decode a line of Morse code using the dictionary
Parameters: row, morse_dict  
Returns: decoded_line  
Name: decode_morse_row  
Algorithm:  
1. create a variable decoded_line to store an empty string
2. for word in row
   3. add morse_dict to decoded_line
3. return decoded_line

Purpose: Decode the entire Morse code text and write to an output file.  
Parameters: table, morse_dict, output_file  
Returns: None  
Name: decode_morse_to_file  
Algorithm:  
1. open output_file for writing 
2. for row in table
   3. call function decoded_morse_code with the arguments row and morse_dict in a variable called decoded_line
   4. write decoded_line to file

   
Name: main  
Purpose: main function  
Parameters: none  
Return: none   
Algorithm:  
1. output program explanation to user
2. ask user to input the dictionary file
3. error check to make sure input is a real file 
4. call function morse_dictionary in variable morse_dict 
5. ask user for the file they want to decode in variable input_file
6. call function morse_file with argument input_file in variable table
7. ask user for the name of the output file in variable output_file
8. call function decode_morse_to_file using arguments table, morse_dict, and output_file
9. output that the decoding is complete and the name of the file where the translation is stored