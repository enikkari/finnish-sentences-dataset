# -*- coding: utf-8 -*-
import re

def read_wordlist_from_file(filename):
    with open(filename, 'r+') as f:
        read_data = f.read()
    return sorted(re.findall('[0-9]* *([^0-9]*)\n', read_data)) # return without counts in the beginning

# TODO
def test_if_abbreviation(string, abbreviations):
    # TODO: add digits <d>
    return -1

def split_string_to_sentences(string, abbreviations):
    sentences = []
    prew_split_at = 0
    for i in range(0,len(string)):
        if(string[i] == '?' or string[i] == '!'):
            sentences.append(string[prew_split_at:i+1])
            prew_split_at = i+1
        elif (string[i] == '.'):
            # TODO : check abbreviations
            sentences.append(string[prew_split_at:i + 1])
            prew_split_at = i + 1
    return sentences

def split_string_to_sentences_with_default(string):
    # TODO
    print('abbreviations not yet supported')
    #abbreviations_list_filename = "manual_abbreviations_list.txt"
    #abbreviations_list = read_wordlist_from_file(abbreviations_list_filename)
    return split_string_to_sentences(string, [])

#abbreviations_list_filename = "manual_abbreviations_list.txt"

#abbreviations_list = read_wordlist_from_file(abbreviations_list_filename)
#print abbreviations_list

#test_s = "Testilause. Onko tämä lause?Älä huuda!.. esim. tämä ei vielä voimi"
#print (split_string_to_sentences(test_s, abbreviations_list))


