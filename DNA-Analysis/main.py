"""
Analyzes DNA samples to determine who the criminal is.
Author: Dinu Wijetunga
"""
from time import sleep
sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line 
  return dna_data

def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if i + 3 < len(dna):
          codons.append(dna[i:i+3])
  return codons

def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print "Number of Matches: %d. Suspect should be further investigated." % (num_matches)
  else:
    print "Number of Matches: %d. Suspect can be freed." % (num_matches)

suspects = ['suspect1.txt', 'suspect2.txt', 'suspect3.txt']

def run_analysis(source_list):
  print "Initializing FBI DNA Analysis Program...\n"
  sleep(2)
  user_input = raw_input("Enter 'A' to analyze DNA. Enter 'X' to exit: ")
  user_input = user_input.upper()
  if user_input == 'A':
    print "Analyzing DNA...\n"
    sleep(2)
    print "Analysis Successfull. Results: \n"
    sleep(1)
    suspect_num = 1
    for suspect in source_list:
      print "SUSPECT " + str(suspect_num) + ":"
      suspect_num += 1
      is_criminal(suspect)
      print
  elif user_input == 'X':
    print "Exiting Program..."
    sleep(1)
    return
  else:
    print "Error. Please restart the program."

run_analysis(suspects)
