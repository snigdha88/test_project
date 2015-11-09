def sum(List):
	sumtotal = 0
	for i in List:
		sumtotal =  int(sumtotal) + int(List[i-1])
	return sumtotal

def mul(List):
	multiply = 1
	for i in List:
		multiply = multiply * int(List[i-1])
	return multiply

List = [1,2,3,4]

print ("sum of all the numbers in the list is: " + str(sum(List)))
print ("multiplying all the numbers in the list gives us: " + str(mul(List)))


#------------------------optimized/Corrected Code-----------------"to Run below code first Comment/Delete the above code, Save it again"-------------
def sum(Listt):
	sumtotal = 0
	for i in List:
		sumtotal =  int(sumtotal) + int(List[i-1])
	return sumtotal

def mul(Listt):
	multiply = 1
	for i in List:
		multiply = multiply * int(List[i-1])
	return multiply

Listt = list(raw_input("Enter list:"))

print "sum of all the numbers in the list is: ",sum(Listt)
print "multiplying all the numbers in the list gives us: ",mul(Listt)
#---------------------------------------------------------------------------------------------------------------------------------------------------
