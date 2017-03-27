

def alphabet_position(letter):
	alphabet = ("abcdefghijklmnopqrstuvwxyz")
	Alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	for i in letter:
		if i in alphabet:
			return alphabet.index(letter)
			
		elif i in Alphabet:
			return Alphabet.index(letter)

			
			
    
def rotate_character(char, rot):
	
	alphabet = ("abcdefghijklmnopqrstuvwxyz")
	Alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	
	if char in alphabet:

		a = alphabet_position (char)
		b = (a + rot) % 26
		return alphabet[b]
	elif char in Alphabet:
		a = alphabet_position (char)
		b = (a + rot) % 26
		return Alphabet[b]
	else:
		return char
		
def encrypt(text, rot):
	newtext = ""
	count = 0
	for i in text:
		a = rotate_character (i,rot)
		count+=1
		newtext+=a
	return newtext
		