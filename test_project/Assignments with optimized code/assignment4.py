def vowel(char):
	
	if (char == "a" or 
		char == "e" or 
		char == "i" or 
		char == "o" or
		char == "u"):
		return True
	else:
		return False

print "enter a character",
char = raw_input()

print ("return: " + str(vowel(char)))

#------------------------optimized/Corrected Code-----------------"to run below code first Comment/Delete the above code, Save it again"-------------
def vowel(char):
	vowels=['a','e','i','o','u']
	if char in vowels:
		return True
	else:
		return False


char = raw_input("Enter a Character:")

print "return: ",vowel(char)


#-------------------------------------------------------------------------
