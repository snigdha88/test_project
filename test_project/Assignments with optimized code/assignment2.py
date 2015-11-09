def max_of_three(a,b,c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

print "enter first number",
a = raw_input()
print "enter second number",
b = raw_input()
print "enter third number",
c = raw_input()

print ("the largest of three is: " + str(max_of_three(a,b,c)))

#------------------------optimized/Corrected Code-----------------"to run below code first Comment/Delete the above code"---------------

def max(a,b):
	if int(a)> int(b):
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

a = int(raw_input("Enter first number:"))

b = int(raw_input("Enter second number:"))

c = int(raw_input("Enter third number:"))

print (max(a,b))," is larger"		

#-------------------------------------------------------------------------
#Note: You need to change type of input that is from 'str' to 'int' inorder to compare the numbers for larger value.
