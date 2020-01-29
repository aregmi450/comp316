import re

def regexCompile(pattern):
		return re.compile(pattern)

c_regex = regexCompile("[a-z|A-Z][a-z|A-Z|0-9]*")

in_string ="aregmi450@gmail.com"

match = c_regex.match(in_string)

if match==None:
		print("String Is Not Valid")
else:
		print("String Is Valid")

allRegex = [line.rstrip() for line in open("reg.txt")]

for rexp in allRegex:
		c_regex = regexCompile(rexp)
		match = c_regex.match(in_string)
if match==None:
         print ("String Is Not Valid")
else:
         print ("String Is Valid")


