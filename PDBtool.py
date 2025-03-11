#!/usr/bin/env python3

import sys  # Allows us to access command-line arguments and exit the program if needed.
import os   # Provides functions to check file existence.
import math  # Will need this for math functions


# This function is called when the program is not used correctly.
# It prints out a message showing the correct usage format.
def usage_and_exit():
    print("Usage: {} <pdb_file_path".format(sys.argv[0]))
    sys.exit(1) # terminates the program with a non-zero status to indicate an error.

def parse_pdb_file(filepath):
    # Store information in list
    atoms = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                # process only lines that start with "ATOM " exactly.
                if not line.startswith("ATOM  "):
                    continue
                # If the alternate location indicator (column 17, index 16) is non-blank, skip record.
                if len(line) >= 17 and line[16] != ' ':
                    continue

                # Store individual atom information in a dictionary
                atom = {
                        'serial': int(line[6:11].strip()),
                        'atom_name': line[12:16].strip(),
                        'alt_loc': line[16].strip(),
                        'res_name': line[17:20].strip().upper(),
                        'chain_id': line[21].strip().upper(),
                        'res_seq': int(line[22:26].strip()),
                        'x': float(line[30:38].strip()),
                        'y': float(line[38:46].strip()),
                        'z': float(line[46:54].strip()),
                        'occupancy': float(line[54:60].strip()),
                        'temp_factor': float(line[60:66].strip()),
                        'element': line[76:78].strip().capitalize()
                    }
                atoms.append(atom) # Each atom’s data is stored as a dictionary in the list atoms

    except Exception as e:
        print("Error: could not open file '{}': {}".format(filepath, e))
        usage_and_exit()
    return atoms

# Insert each other functions here such as:
def print_help():
    print("help")
    
def atom_frequencies():
    print("atom frequencies")

def residue_frequencies():
    print("residue frequencies")
          
def residuelength_command():
    print("residue length")

def temp_check_command():
    print("temp check")

def occupancy_command():
    print("occupancy")

# Main function, I'll update periodically when functions are updated
def main():
    if len(sys.argv) != 2:
       usage_and_exit()
      
    # Assigning the pdb file to the variable pdb_file, this is the  second
    # argument when the user types ./PDBtool.py file.pdb
    pdb_file = sys.argv[1]

    # Splits the text of the file from argument two when the user
    # types ./PDBtool.py file.pdb, here file and .pdb is
    # seperated
    file_extension = os.path.splitext(pdb_file)
    # If the file dosen't exist exit
    if not os.path.exists(pdb_file):
        print("Error: '{}' does not exists".format(pdb_file))
        usage_and_exit()
      
    # Just for testing file extensions
    # print("File extension:'{}'".format(file_extension[1]))

    # Checks if the file is a pdb file
    if file_extension[1] != '.pdb':
        print("Wrong file type")
        usage_and_exit()
    # Just for testing 
    # print("Successfully opened file")
  
    # reads the file and builds a list of atom dictionaries.
    atoms = parse_pdb_file(pdb_file) 
    print("Welcome to the pdb program.\n")
    print("To begin, try typing 'help' for the list of valid commands.\n")
    print("{} atoms recorded.\n".format(len(atoms)))

# The program enters a while Trun loop, prompting the user with "Enter command: "
    while True:
        try:
            # The input is stripped of extra whitespace and spit into parts
            # The first part is the command and the remaining is taken as arguments
            user_input = input("Enter a command: ").strip()
        except EOFError:  # If the user presses Ctrl D or Ctrl Z it signals an end-of-file\
                          # and input() raises this exception
            break # End of file, exit interactive loop
        if not user_input:  # checks if the input string is empty; the user just presses enter
            continue # prompts the user again

        parts = user_input.split()
        command = parts[0].lower()
        args = parts[1:]
        if command == 'help':
            print_help()
        elif command == 'atomfreq':
            atom_frequencies(atoms)
        elif command == 'resfreq':
            residue_frequencies(atoms)
        elif command == 'reslength':
            residue_length_command(atoms, args)
        elif command == 'tempcheck':
            temp_check_command(atoms, args)
        elif command == 'occupancy':
            occupancy_command(atoms, args)
        elif command == 'quit':
            print("Exiting program, Goodbye!")
            break
        else:
            print("Invalid command. Type 'help' for the list of valid commands.")



if __name__ == "__main__":
    main()
