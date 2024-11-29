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

#name: morse_dictionary
#parameters:
#returns: morse_dict







def morse_dictionary():
    filename = input("Enter a file name: ")
    morse_dict = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                text = line.strip().split()
                if len(text) == 2:
                    morse = text[1]
                    letter = text[0]
                    morse_dict[morse] = letter
    except FileNotFoundError:
        print("File not found")
    return morse_dict

morse_dictionary()
