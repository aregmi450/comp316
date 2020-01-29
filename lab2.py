# rstrip() method returns a copy of the string with trailing characters removed (based on the string argument passed).
# If no argument is passed, it removes trailing spaces.

import re
def regexCompile(pattern):
		return re.compile(pattern)

c_regex = regexCompile("[a-z|A-Z][a-z|A-Z|0-9]*")

in_string ="Welcome to the planet 338C Let's host @ hostages."

allRegex = [line.rstrip() for line in open("reg.txt")]

for rexp in allRegex:
		c_regex = regexCompile(rexp)
		match = c_regex.match(in_string)
if match==None:
         print ("String Is Not Valid")
else:
         print ("String Is Valid")

