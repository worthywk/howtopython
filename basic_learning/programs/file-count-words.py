import os


def get_words(filename):
	with open(filename, 'r') as file:
		text = file.read()
		text = text.replace('\n', ' ')
		text = text.replace(',', '').replace('.', '').replace('?', '').replace('!', '')
		text = text.lower()
		words = text.split()
		words.sort()
	return words


def get_words_dict(words):
	words_dict = dict()
	for word in words:
		if word in words_dict:
			words_dict[word] = words_dict[word] + 1
		else:
			words_dict[word] = 1
	return words_dict


File = 'sample.txt'
file_words = get_words(File)
unique_file_words = get_words_dict(file_words)

print('count words: %d' % len(file_words))
print('count unique words: %d' % len(unique_file_words))
for word in unique_file_words:
	print(word.ljust(15), unique_file_words[word])
