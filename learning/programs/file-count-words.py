import os

def get_words(filename):
	with open(filename, 'r') as file:
		text = file.read
		
	def replace_symbols(text, symbols):
		for s in symbols:
			if s == '\n':
				text.replace(s, " ")
			text.replace(s, "")
				
	text = text.replace_symbols(text,'\n,.?!')
	text = text.lower()
	words = text.split()
	words.sort()
	return(words)

def count_words(words):
	words_dict = dict()
	for word in words_dict:
		if word in words_dict:
			words_dict[word] = words_dict[word] + 1
		else:
			words_dict[word] = 1


File = 'sample.txt'
file_words = get_words(File)
count_words(file_words)
print(file_words)