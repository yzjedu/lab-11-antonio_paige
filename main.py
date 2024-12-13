# Programmers:  Antonio, Paige
# Course:  CS151, Professor Zelalem Yalew
# Due Date: November 28
# Lab Assignment:  Lab 11
# Problem Statement:  In this lab assignment we will create a dictionary using text from a file, then translate other files
#                       from morse code into english using the dictionary
# Data In: user inputs the name of file for creating dictionary, then the name of file they wish to translate
# Data Out: translation of file user inputted
# Credits: class discussion
# Input Files: morsecode.txt, morse1.txt, morse2.txt, morse3.txt

import os

# Purpose: put morse code into a dictionary
# Parameters: filename
# Returns: morse_dict
def morse_dictionary(filename):
    morse_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split('  ')
            morse = line[1]
            letter = line[0]
            morse_dict[morse] = letter
    print(morse_dict)
    return morse_dict

# Purpose: Read the Morse code text file to decode
# Parameters: filename
# Returns: table
def morse_file(filename):
    table = []
    with open(filename, 'r') as file:
        for line in file:
            table.append(line.strip().split())
        return table

# Purpose: Decode a line of Morse code using the dictionary.
# Parameters: row, morse_dict
# Returns: decoded_line
def decode_morse_row(row, morse_dict):
    #words = line.split(' ')  # Split the line into Morse code letters
    decoded_line = ''
    for word in row:
        decoded_line += morse_dict[word]
    return decoded_line

# Purpose: Decode the entire Morse code text and write to an output file.
# Parameters: table, morse_dict, output_file
# Returns: None
def decode_morse_to_file(table, morse_dict, output_file):
    with open(output_file, 'w') as file:
        for row in table:
            decoded_line = decode_morse_row(row, morse_dict)
            file.write(decoded_line + '\n')

# Purpose: Main function to drive the Morse code decoder program.
# Parameters: None
# Returns: None
def main():
    print("This program decodes morse code")
    input_morse = input("Enter the name of the morse code dictionary file: ")
    while not os.path.isfile(input_morse):
        print("File not found")
        input_morse = input("Enter a file name: ")

    morse_dict = morse_dictionary(input_morse)
    input_file = input("Enter the name of the file to decode: ")
    table = morse_file(input_file)
    output_file = input("Enter the name of the output file: ")
    decode_morse_to_file(table, morse_dict, output_file)
    print(f"Decoding complete! The decoded text has been saved to '{output_file}'.")

main()