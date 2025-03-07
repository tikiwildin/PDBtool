# PDBtool
PDBtool is a Python program that reads PDB (Protein Data Bank) files and provides interactive commands for analyzing macromolecule data. The tool extracts information about atoms and residues from the PDB file and allows users to perform various analyses such as calculating atom frequencies, residue frequencies, maximum distances within residues, and checking temperature factors and occupancy values.


## Features
+ Parse PDB Files:
  + Reads PDB files and extracts ATOM records while handling errors.
+ Interactive Interface:
  + Provides an interactive command-line mode where you can enter various commands.
  
+ Commands Include:
  + help: Display detailed help for each command.
  + atomfreq: Show the frequency of each distinct atom (by element).
  + resfreq: Display the frequency of each residue (three-letter code).
  + reslength <res_name> <chain_id> <res_seq_num>: Calculate the maximum distance between any two atoms in a specified residue.
  + tempcheck <decimal>: Report the distribution of temperature factors relative to a given threshold.
  + occupancy <decimal>: Report the distribution of occupancy values relative to a given threshold.
  + quit: Exit the application.

## Requirements
+ Python 3.x

## Installation and setup
1. Download the program and place it in your desired directory.
2. Make the script executable (if on Unix/Linux/Mac):
   ![image](https://github.com/user-attachments/assets/59a8d5d2-e58b-496f-815b-0cfcdcc89313)





## Usage
This program can be run in the terminal by typing ./PDBtool.py (while in the directory of where this program is placed)
and the pdb file desired.  
./PDBtool.py path/to/yourfile.pdb  
For example:

![image](https://github.com/user-attachments/assets/fd520cb4-97a8-4aa8-8e5b-32ffeaab4ce2)

When you run the program, it will display a welcome message along with the total number of atoms recorded. You can then enter interactive commands. For example:
![image](https://github.com/user-attachments/assets/9ea1713e-5e22-4ac4-a8ad-72a43bf35cb4)




