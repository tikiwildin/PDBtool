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
2. Open a terminal
   + On macOS, use Spotlight to search for "Terminal".
   + On Linux, press Ctrl + Alt + T or search for "Terminal".
   + On Windows, open Git Bash or WSL.
3. Navigate to the folder where PDBtool.py is saved
   + Use the cd command (change directory). For example:
     ![image](https://github.com/user-attachments/assets/1878e715-dd6d-4b25-956f-30aaafd6f996)

  
5. Make the script executable (if on Unix/Linux/Mac):
   ![image](https://github.com/user-attachments/assets/59a8d5d2-e58b-496f-815b-0cfcdcc89313)

### Running on Windows (Command Prompt)

1. Open Command Prompt.
2. Navigate to the folder where `PDBtool.py` is located:
    cd path\to\your\folder
3. Run the program using Python:
   ![image](https://github.com/user-attachments/assets/3a16a1bc-fb2c-43b9-abd7-13f091bc2b37)
  - Make sure Python is installed and added to your PATH. You can check by typing python --version.
   
## Usage
This program can be run in the terminal by typing ./PDBtool.py (while in the directory of where this program is placed)
and the pdb file desired.  
./PDBtool.py path/to/yourfile.pdb  
For example:

![image](https://github.com/user-attachments/assets/fd520cb4-97a8-4aa8-8e5b-32ffeaab4ce2)

When you run the program, it will display a welcome message along with the total number of atoms recorded. You can then enter interactive commands. For example:
![image](https://github.com/user-attachments/assets/9ea1713e-5e22-4ac4-a8ad-72a43bf35cb4)

Now you can type one of the following commands:

+ help – Show available commands and usage

+ atomfreq – Show how many atoms of each element are present

+ resfreq – Show how many times each residue appears

+ reslength <res_name> <chain_id> <res_seq_num> – Measure max distance between atoms in one residue

+ tempcheck <number> – Show atom counts below/at/above a temp factor

+ occupancy <number> – Show atom counts below/at/above an occupancy value

+ quit – Exit the program

## Additional Document
https://docs.google.com/document/d/1mRITJdA88KFb5D8eGXbuA3EUgomXNhkHhAdKpUNQ8p0/edit?usp=sharing





