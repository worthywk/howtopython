string = ' Hello string! :) '
print(string.isdigit())	# false
print(string.isalpha())	# false
print(string.islower()) # false
print(string.startswith('Hello')) # true

string = string.strip()
print(string) # 'Hello string! :)'
print(string.replace(":)","")) # 'Hello string!'
print(string[:string.find(':)')]) # 'Hello string!'

string = 'HELLO string'
print ('.'.join(string.split()[0][:4].lower().capitalize()).replace('.'," "))

### output steps:

# string.split - ('Hello', 'string')
# string.split[0][:4] - Hell
# 'Hell'.lower() - hell
# 'hell'.capitalize() - Hell
# '.'.join(Hell) - H.e.l.l
# 'H.e.l.l'.replace('.'," ") - H e l l


### Exercises

# 1

print('''
Write a Python program to change a given string
to a new string where the first and last chars
have been exchanged''')

string='Bomb'
def change_string(string):
	print(string[-1] + string[1:-1] + string[0])
	
change_string(string)  # bomB

# 2

print('''
Write a Python program to calculate
the length of a string''')


string='Bomb'

def len_string(string):
	
	"""
	This method count elements within the string and return length
	"""

	string_count = 0
	for i in string:
		string_count += 1
	return string_count

print(len_string(string))
print(len(string))

# 3

print('''
Write a Python program to count the number of
characters (character frequency) in a string

Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
''')

string = "google.com"

def count_items_string(string):
	words_dict = dict()
	
	for i in string:
		if i in words_dict:
			words_dict[i] += 1
		else:
			words_dict[i] = 1
	return words_dict


print(count_items_string(string))

# 4

print('''
Write a Python program to get a string made of the first 2
and the last 2 chars from a given a string.
If the string length is less than 2,
return instead of the empty string
''')

string = input("enter string: ")

def make_str(string):
	if len(string) >= 2:
		str = string[0:2] + string[-2:]
	else:
		str = "empty string"
	return str


print(make_str(string))

# 5

print(''' Write a Python program to get a string from
a given string where all occurrences of its first char
have been changed to '$', except the first char itself

sample: restart, output: resta$t

''')

string = "restart"
print(string.count(string[2]))

def xxx(string, item):
	
	if string[0] in string[1:]:
		
		first_letter = string[0]
		string = string.replace(first_letter, item)
		string = first_letter + string[1:]
	return string

# 6 ???

print(''' Write a Python program to get a string from
a given string where all occurrences of each char
have been changed to '$', except the first char of occurrence itself
''')

def xxx1(string, item):
	for i in range(len(string)):
		if  string.count(string[i]) > 1:
			
			string = string.replace(string[i], item)
	return string

print(xxx(string, 'S'))
print(xxx1(string, '$'))

print(''' Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
''')

def swap_chars(str1, str2):
	
	string = '{} {}'.format(str1, str2)
	string = string.split()
	string = string[1][:2] + string[0][2:] + " " + string[0][:2] + string[1][2:]
	return string
	
print(swap_chars(string))

# 7

print('''Write a Python program to add 'ing' at the end of a given
string (length should be at least 3). If the given string already
ends with 'ing' then add 'ly' instead. If the string length of
the given string is less than 3, leave it unchanged

Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
''')

string = input("enter string: ")

def add_ending_string(string):
	if len(string) >= 3:
		if string[-3:] != 'ing':
			string += 'ing'
		else:
			string += 'ly'
	return string

print(add_ending_string(add_ending_string(string)))