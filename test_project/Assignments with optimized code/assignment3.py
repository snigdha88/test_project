def string_length(string):
	
 count = 0

 for i in string: 
    count = count + 1
    
 return count

print "enter a string",
string = raw_input()

print ("length of string is: " + str(string_length(string)))



#------------------------optimized/Corrected Code-----------------"to run below code first Comment/Delete the above code, Save it again"-------------
def string_length(string):
	
 count = 0

 for i in string: 
    count = count + 1
    
 return count


string = raw_input("Enter a string:")
print "Length of string is: ", string_length(string)


#-------------------------------------------------------------------------
