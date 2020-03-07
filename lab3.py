grammar_s = input("Enter a Grammar: ") #this input add  "R->wwr|rww|Rrw"
# grammar_s  = "R->wwr|rww|Rrw"
# print(grammar_string)
a = grammar_s[0]
allalphas = []
allbetas = []
splits = grammar_s[3:].split('|')
# print(splitted)
for s in splits:
	if a == s[0]:
    	allalphas.append(s[1:])
	else:
    	allbetas.append(s)
betas_new = [beta+a+"'" for beta in allbetas]
alphas_new = [alpha+a+'" for alpha in allalphas]
if len(allalphas)==0:    
	print("Not A Left Recursive Grammar")
else:
	print("A Left Recursive Grammar")
	print("Grammar : ")
	print(f"{a}->{'|'.join(betas_new)}")
	print(f"{a}'->{'|'.join(alphas_new)}|E")

