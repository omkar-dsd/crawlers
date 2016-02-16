import re

phone = "2004-959-559 # This is Phone Number"

#Delete python style coomments

num = re.sub(r'#(.*$)', "", phone)   # from hashtag to the end of line
print "Phone Num: ", num

#remove naything other than digits

num = re.sub(r'[^0-9]', "", phone)      #[^0-9] matches anything other than digits
print "Phone Num : ", num

num = re.sub(r'\D', "", phone)      #\Dmatches anything other than digits
print "Phone Num : ", num