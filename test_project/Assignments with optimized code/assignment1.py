def max(a,b):
	if a>b:
		return a
	else:
		return b

print "enter first number",
a = raw_input()
print "enter second number",
b = raw_input()

print (str(max(a,b)) + " is larger")		


#------------------------optimized/Corrected Code-----------------"to run bellow code first comment the above code"---------------

def max(a,b):
	if a > b:
		return a
	else:
		return b

a = int(raw_input("Enter first number:"))

b = int(raw_input("Enter second number:"))

print (max(a,b))," is larger"		

#-------------------------------------------------------------------------
#Note: You need to change type of input that is from 'str' to 'int' inorder to compare the numbers for larger value.
