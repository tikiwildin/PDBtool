def print_help():
  print("List of valid commands:")
  print("  help       - Show this help message with descriptions of all commands.")
  print("  atomfreq   - Display the frequency of each atom type in the PDB file.")
  print("  resfreq    - Display the frequency of each residue in the PDB file.")
  print("  reslength  - Show the number of residues in each chain.")
  print("  tempcheck  - Check temperature factor information.")
  print("  occupancy  - Count atoms by comparing their occupancy against a given threshold.")
  print("  quit       - Exit the program.")

def main():
  print("Welcome to the pdb program.")
  print("To begin, try typing 'help' for the list of valid commands.\n")

  while True:
      user_input = input("Enter a command: ").strip().lower()

      if user_input == "help":
          print_help()
      elif user_input == "quit":
          print("Exiting program, Goodbye!")
          break
      else:
          print("Invalid command. Type 'help' for the list of valid commands.")

if __name__ == "__main__":
  main()
