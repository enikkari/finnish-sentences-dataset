import re
from collections import Counter

input_filename = 'candidate_answer_data_kokomaa11042017.csv'
output_filename = 'raw_word_list.txt'

collect_potential_abbreviations = True
potential_abbreviations_filename = 'potential_abbreviations_file.txt'

# get input from file
input_file = open(input_filename, 'r+')
text_from_file = input_file.read()
input_file.close()

# handle the raw text
tagged_text = re.sub('[0-9]+', '<d>', text_from_file) # tag numbers
#tagged_text = re.sub(' [^ ].[com/net/fi/io/]]', ' <www>', tagged_text)      # tag emails/web addresses
list_of_all_words = re.split('[; +"@()\'/,?!\xe2\n]', tagged_text)
set_of_uniq_words = Counter(list_of_all_words).most_common()

# write the output to file
output_file = open(output_filename, 'w+')
potential_abbreviations_file = open(potential_abbreviations_filename, 'w+')

for word_and_count in set_of_uniq_words:
    count = word_and_count[1]
    word = word_and_count[0]
    output_file.write(str(count) + " " + word + '\n')
    if(collect_potential_abbreviations and '.' in word):
        potential_abbreviations_file.write(str(count) + " " + word + '\n')

output_file.close()
potential_abbreviations_file.close()