# Indexing a string

string = 'anoux jadur'

for character in range(len(string)):
    print(string[character], end=' ')

print('\n')

# Iterating a string

string2 = 'bruno jadur'

for character in string2:
    print(character, end=' ')
    
print('\n')

# Using in operator

string3 = 'leila jadur'

alphabet = list(map(chr, range(ord('a'), ord('z')+1)))

for letter in alphabet:
    if letter in string3:
        print('the letter "' + letter + '" is in the string3')
    else:
        print('the letter "' + letter + '" is not in the string3')
 
print('\n')

# # Using not in operator

alphabet = list(map(chr, range(ord('a'), ord('z')+1)))

for letter in alphabet:
    if letter not in string:
        print('the letter "' + letter + '" is not in the string')
    else:
        print('the letter "' + letter + '" is in the string')