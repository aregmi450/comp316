# Module Regular Expression is imported using _import_().
# compile() creates regular expression character class [a-z].
# match checks the validity of the expression.

import re
p = re.compile('[a-z|A-Z][A-Z|a-z|0-9]*')
s1 = "aB1, AZ, Z9"
match = p.match(s1)
if match==None:
		print("String s1 is not accepted.")
else:
		print("String s1 is accepted.")
s2 = "9B, 9_AB5"
match = p.match(s2)
if match==None:
		print("String s2 is not accepted.")
else:
		print("String s2 is accepted.")

