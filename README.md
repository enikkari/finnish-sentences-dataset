This is the finnish sentences dataset distribution v 1.0.5

This project is created to store, improve and track an open source dataset of sentences in the Finnish language.
The file yle-vaalikone-2017.txt contains currently 448403 sentences.

The dataset is based on YLE esuskuntavaalit vaalikone dataset that is available at
https://yle.fi/uutiset/3-9526290
The dataset also contains occasional sentences in swedish and english.

The original Yle data files are 
candidate_answer_data_aluekysymykset11042017.csv
candidate_answer_data_kokomaa11042017.csv
The original files have encoding issues that were solved using the (Python2) script located in fix_encoding.py

The current version has been separated into sentences by periods, question marks and exclamation marks.
The most common abbreviations have been manually collected to the file manual_abbreviations_file.txt.
Sentence boundaries are not introduced after an abbreviation.

This segmentation is lacking and the dataset will be improved in the future.
Currently the segmenter does not recognize patterns that contain digits and will segment f.ex. 123.123.123 into three separate sentences.

The sentences are located in file yle-vaalikone-2017.txt
Each sentence is separated into it's own line.

To regenerate the dataset, check the examples in the jupyter notebook sentence_notebook.ipynb

The original project files are located in github https://github.com/enikkari/finnish-sentences-dataset
. For more information or suggestions contact enikkari trough github.