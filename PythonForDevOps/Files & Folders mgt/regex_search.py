"""Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen."""

import os
import re


def find_files_in_folder(folder_path, regex_pattern):
    """Search for lines matching a user-supplied regular expression in all .txt files in a folder.
    folder_path = The path to folder containing .txt files
    regex_pattern = The regular expression pattern to search for"""

    # Ensure the folder_path end with '/'
    if not folder_path.endswith("/"):
        folder_path += "/"

    # Get list of all the .txt files in the folder
    file_list = os.listdir(folder_path)
    file_list_txt = []  # to get a list of the .txt files from the folder
    for f in file_list:
        if f.endswith(".txt"):
            file_list_txt.append(f)

    # to loop through the .txt files
    for f_txt in file_list_txt:
        file_path = folder_path + f_txt
        print(f'Searching in {f_txt} now....')

        # Open the files and search for line matching the regular expression
        with open(file_path, 'r', encoding="utf-8") as file:
            lines_number = 0
            for line in file:
                lines_number += 1
                if re.search(regex_pattern, line):
                    print(f'Match found in {f_txt}, line {lines_number}: {line.strip()}')


# Example usage
folder_path = "/path/to/your/folder"  # Replace with the actual path to your folder
regex_pattern = input("Enter the regular expression pattern: ")
find_files_in_folder(folder_path, regex_pattern)
