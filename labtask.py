import re

number = raw_input("Enter the number: ")

num = re.sub(r'[^0-1]', "", number)

if num==number:
	print "It is binary"

else:
	print "it is not binary"