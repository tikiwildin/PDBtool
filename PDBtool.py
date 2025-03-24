#!/usr/bin/env python3

import sys  # Allows us to access command-line arguments and exit the program if needed.
import os   # Provides functions to check file existence.
import math  # Will need this for math functions

#
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
    
def atom_frequencies(atoms):
    #python PDBtool.py ./tests/6lu7.pdb

    #key = atomName, value = number of atoms for that element
    distinct_atom = {}

    #looping through the atoms list and getting the indv dictionary
    for atom in atoms:
        #getting the atom's name, if it's not in the dictionary, add it and set the value to 0 else add 1
        currentAtomName = atom['element']
        if currentAtomName in distinct_atom:
            distinct_atom[currentAtomName] +=1
        else:
            distinct_atom[currentAtomName] = 1

    #python sort function, sorts the keys in alphabetical order and returns the new dictionary
    sorted_atoms = dict(sorted(distinct_atom.items()))

    #loop through the new dictionary and format it to "atom: #"
    for atom in sorted_atoms:
        print(atom + ":" + str(sorted_atoms.get(atom)))

def residue_frequencies(atoms):
    #key = residueName, value = number of occurrences of that residue
    distinct_res = {}

    #looping through the atoms list and getting the indv dictionary
    for atom in atoms:
        #getting the residue's name, if it's not in the dictionary, add it and set the value to 0 else add 1
        currentResidueName = atom['res_name']
        if currentResidueName in distinct_res:
            distinct_res[currentResidueName] +=1
        else:
            distinct_res[currentResidueName] = 1
        
        #python sort function, sorts the keys in alphabetical order and returns the new dictionary
        sorted_residue = dict(sorted(distinct_res.items()))

        #loop through the new dictionary and format it to "residue: #"
        for residue in sorted_residue:
            print(residue + ":" + str(sorted_residue.get(residue)))
          
def residuelength_command(atoms, args):
    print("residue length")

def temp_check_command(atoms, args):
    print("temp check")

def occupancy_command(atoms, args):
    #python PDBtool.py ./tests/6lu7.pdb
    print(args)
    number = None
    try:
        number = float(args[0])
        if(number < 0.0 or number > 1.0):
            raise ValueError
    except ValueError:
        newRange = input("The input is invalid! Please enter a value between 0.0 - 1.0 : ")
        occupancy_command(atoms, newRange)
    
    tempAbove = 0
    tempAt = 0
    tempBelow = 0
    
    # print("num: " + str(number) + " args: " + str(args))


    # if ( < 0.0) or (float(args) > 1.0):
    #     newRange = input("The number is invalid. Please enter a value between 0.0 - 1.0")
    #     occupancy_command(atoms, newRange)


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
            residuelength_command(atoms, args)
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
