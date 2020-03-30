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

print('''
Write a Python program to change a given string
to a new string where the first and last chars
have been exchanged''')

string='Bomb'
def change_string(string):
	print(string[-1] + string[1:-1] + string[0])
	
change_string(string)  # bomB
