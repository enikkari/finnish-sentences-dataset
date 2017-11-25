input_filename = 'yle-vaalikone-2017.txt'

text = open(input_filename, 'r+').read().decode('utf-8','ignore').encode("utf-8")

print text

file = open('resave.txt', 'w+')
file.write(text)


