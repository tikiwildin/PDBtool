#!/usr/bin/env python3

# Authors: Fenley, Atiq, Carey, Nawel
# Date: 04/30/2025

import sys  # Allows us to access command-line arguments and exit the program if needed.
import os   # Provides functions to check file existence.
import math  # Will need this for math functions
import string # Will need this for checking strings

# This function is called when the program is not used correctly.
# It prints out a message showing the correct usage format.
def usage_and_exit():
    print("Usage: {} <pdb_file_path".format(sys.argv[0]))
    sys.exit(1) # terminates the program with a non-zero status to indicate an error.


def parse_pdb_file(filepath):
    # Store information in a list
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

#Prints out all the valid functions with a description of what they do and an example
def print_help():
    help_text = """
Valid commands:
    help
        Displays this help message with details about every valid command.

    atomfreq 
        Displays the frequency of each distinct atom (by element) in the file.
        Example output:
            C: 3201
            N: 918
            O: 1044
            P: 42
            S: 23

    resfreq
        Displays the frequency of each distinct residue (three-letter code) in the file.
        Example output:
            ALA: 175
            ARG: 306
            ...
            TYR: 204

    reslength <res_name> <chain_id> <res_seq_num>
        Calculates and prints the maximum Euclidean distance (in angstroms) between any two atoms
        in the specified residue.
        - <res_name>: three-letter residue name (uppercase)
        - <chain_id>: one-letter chain identifier (uppercase)
        - <res_seq_num>: integer residue sequence number
        Example:
            reslength GLU A 764

    tempcheck <decimal>
        Reports the frequency (and percentage) of atoms whose temperature factor is below, at, and above
        the specified value (between 0.00 and 100.00).
        Example:
            tempcheck 50.00

    occupancy <decimal>
        Reports the frequency (and percentage) of atoms whose occupancy is below, at, and above the
        specified value (between 0.00 and 1.00).
        Example:
            occupancy 1.00

    quit
        Exits the program.
    """
    print(help_text)

    
def atom_frequencies(atoms):

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

    #Checking for the correct number of arguments
    if len(args) != 3:
        if len(args) == 0:
            print("Missing arguments to reslength")
        else:
            print("Incorrect number of arguments to reslength")
        print("Usage: reslength <res_name> <chain_id> <num>")
        print("For details about the reslength command, use the 'help' command.")
        return

    res_name, chain_id, res_seq_str = args

    if len(res_name) != 3 or not res_name.isupper() or len(chain_id) != 1 or not chain_id.isupper():
        print("Usage: reslength <res_name> <chain_id> <num>")
        print("For details about the reslength command, use the 'help' command.")
        return

    try:
        res_seq = int(res_seq_str)
    except ValueError:
        print("Usage: reslength <res_name> <chain_id> <num>")
        print("For details about the reslength command, use the 'help' command.")
        return

    residue_atoms = [
        atom for atom in atoms
        if atom['res_name'] == res_name and
           atom['chain_id'] == chain_id and
           atom['res_seq'] == res_seq
    ]

    if not residue_atoms:
        print("No residue present.")
        return

    max_distance = 0.0
    n = len(residue_atoms)
    for i in range(n):
        for j in range(i + 1, n):
            dx = residue_atoms[i]['x'] - residue_atoms[j]['x']
            dy = residue_atoms[i]['y'] - residue_atoms[j]['y']
            dz = residue_atoms[i]['z'] - residue_atoms[j]['z']
            d = math.sqrt(dx * dx + dy * dy + dz * dz)
            if d > max_distance:
                max_distance = d

    print("{} with sequence number {} in chain {} has {:.2f} angstroms.".format(
        res_name, res_seq, chain_id, max_distance
    ))

def temp_check_command(atoms, args):

    #Checking for the correct number of arguments
    if len(args) != 1:
        if len(args) == 0:
            print("Missing arguments to tempcheck")
        else:
            print("Incorrect number of arguments to tempcheck")
        print("Usage: tempcheck <decimal>")
        print("For details about the tempcheck command, use the 'help' command.")
        return
    
    try:
        value = float(args[0])
    except ValueError:
        print("Usage: tempcheck <decimal>")
        print("For details about the tempcheck command, use the 'help' command.")
        return
    if value < 0.00 or value > 100.00:
        print("Usage: tempcheck <decimal>")
        print("For details about the tempcheck command, use the 'help' command.")
        return
    
    total = len(atoms)
    below = sum(1 for atom in atoms if atom['temp_factor'] < value)
    at_val = sum(1 for atom in atoms if math.isclose(atom['temp_factor'], value, rel_tol=1e-6, abs_tol=1e-6))
    above = total - below - at_val 

    print("Temperature factor below {:.2f}: {} / {} ({:.1f}%)".format(value, below, total, below/total*100))
    print("Temperature factor at {:.2f}: {} / {} ({:.1f}%)".format(value, at_val, total, at_val/total*100))
    print("Tempture factor above {:.2f}: {} / {} ({:.1f}%)".format(value, above, total, above/total*100))


def occupancy_command(atoms, args):
    #This part checks if there is an argument and if it's just 1 argument being passed.
    #Otherwise, prints the corresponding error message
    if len(args) != 1:
        if len(args) == 0:
            print("Misssing argument to occupancy")
        else:
            print("Incorrect number of arguments to occupancy")
        print("Usage: occupancy <decimal>")
        print("For details about the occupancy command, use the 'help' command.")
        return

    argument_1 = args[0] #terminal args[1], [0] is the fileName, but somehow it works in VScode
    occValue = None

    #There's at least 1 argument if the code ran till here.
    #This part checks if that argument contains anything besides numbers and if it within the range of (0.00-1.00)
    #Otherwise, prints the corresponding error message
    try:
        occValue = float(argument_1)
        if((occValue < 0.0) or (occValue > 1.0)):
            raise ValueError
    except ValueError as e:
        print("Usage: occupancy <decimal>\nFor details about the occupancy command, use the 'help' command.")
        return

    #Storing total, below, at_val, above as int
    total = len(atoms)
    below = 0;
    at_val = 0;
    above = 0;

    #Going through the atoms list and getting the indv atom dictionary
    #Increment the corresponding val if it's below, above, or at the occupancy value that the user inputed
    for atom in atoms:
        currentOccValue = atom['occupancy']

        if(currentOccValue > occValue):
            below+=1

        elif(currentOccValue < occValue):
            above+=1

        else:
            at_val+=1

    #Printing the result in the corresponding format
    print("Temperature factor below " + "{:.2f}".format(occValue) + ": " + str(below) + " / " + str(total) + " (" + str(below/(total)*100.0) + "%)" )
    print("Temperature factor at " + "{:.2f}".format(occValue) + ": " + str(at_val) + " / " + str(total) + " (" + str(at_val/(total)*100.0) + "%)" )
    print("Temperature factor above " + "{:.2f}".format(occValue) + ": " + str(above) + " / " + str(total) + " (" + str(above/(total)*100.0) + "%)" )

# Main function!!
def main():
    if len(sys.argv) != 2:
       usage_and_exit()
      
    # Assigning the pdb file to the variable pdb_file, this is the second
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
