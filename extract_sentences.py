import re

def read_wordlist_from_file(filename):
    with open(filename, 'r+') as f:
        read_data = f.read()
    return sorted(re.findall('[0-9]* *([^0-9]*)\n', read_data)) # return without counts in the beginning

abbreviations_list_filename = "manual_abbreviations_list.txt"

abbreviations_list = read_wordlist_from_file(abbreviations_list_filename)
print abbreviations_list

# break on ; ? and !
# break on . except when .. or part of abbreavation

