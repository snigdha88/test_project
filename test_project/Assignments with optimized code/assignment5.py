import string

def vowelcheck(char):
	if (char == "a" or 
		char == "e" or 
		char == "i" or 
		char == "o" or
		char == "u"):
		return True
	else:
		return False

def trans(text):

 translatedtext = ""
 non_alphabets = string.punctuation + string.digits + string.whitespace
 for char in text:
 	translatedtext = translatedtext + char
 	if not vowelcheck(char):
 		if char not in non_alphabets:
 			translatedtext = translatedtext + 'o' + char
 
 return translatedtext 
 

print ("enter text to translate")
text = raw_input()
print ("translated string is: " + str(trans(text)))

#------------------------optimized/Corrected Code-----------------"to Run below code first Comment/Delete the above code, Save it again"-------------
import string

def vowelcheck(char):
	vowels=['a','e','i','o','u']
	if char in vowels:
		return True
	else:
		return False

def trans(text):

 translatedtext = ""
 non_alphabets = string.punctuation + string.digits + string.whitespace
 for char in text:
 	translatedtext = translatedtext + char
 	if not vowelcheck(char):
 		if char not in non_alphabets:
 			translatedtext = translatedtext + 'o' + char
 
 return translatedtext 
 

text = raw_input("Enter text to translate:")
print "Translated string is: ",trans(text)

#------------------------------------another easyiest method-------"to Run below code first Comment/Delete the above both code, Save it again"--------

s=raw_input("Enter String:")
d=""
a=['a','e','i','o','u']
for i in s:
   if i not in a and i!=" ":
       d+=i+"o"+i

   elif i!=" ":
       d+=i
   else:
       d+=" "

print d
#------------------------------------------------------------------------------------------------------------------------------


