# -*- coding: utf-8 -*-
import re
from utils.trie import TrieJumper

def read_wordlist_from_file(filename):
    with open(filename, 'r+') as f:
        read_data = f.read()
    return sorted(re.findall('[0-9]* *([^0-9]*)\n', read_data)) # return without counts in the beginning

def split_string_to_sentences(text, abbreviations):
    # TODO : take into account digits <d>
    # add abbreviations to the abbreviations checker
    abb_checker = TrieJumper()
    for abb in abbreviations:
        abb_checker.add_word(abb)

    # loop trough the text and collect sentences
    sentences = []
    start_of_new_sentence = 0
    i = 0
    while i < len(text):
        # break sentence at !, . and ? - take into account a string of them. F.ex !!!??
        if text[i] in ['!', '.', '?']:
            while i < len(text) and text[i] in ['!', '.', '?']:
                i += 1
            sentences.append(text[start_of_new_sentence: i])
            start_of_new_sentence = i
        # check if we are at the beginning of a abbreviation - if so, jump to it's end
        i += abb_checker.make_jump(text[i:])
        i += 1
    # add last sentence to list (if it does not end in !?.)
    if (i != len(text)):
        sentences.append(text[start_of_new_sentence:])
    return sentences


abbreviations_list_filename = "manual_abbreviations_list.txt"
abbreviations_list = read_wordlist_from_file(abbreviations_list_filename)

test_s = "Testilause. Onko tämä lause?Älä huuda!.. esim. tämä toimii jo. Mutta numerot kuten 123.123.123 eivät."
sentences = split_string_to_sentences(test_s, abbreviations_list)
print(sentences)