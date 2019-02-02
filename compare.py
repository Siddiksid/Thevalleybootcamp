def isin(char,astr):
	if astr=='':
		return False
	if len(astr)==1:
		return char==astr
	midindex=len(astr)//2
	midchar=astr[midindex]
    
    if char==midchar:
    	return True
    elif char<midchar:
    	return isin(char,astr[:midindex])
    else:
    	return isin(char,astr[midindex+1:])

print(isin('a','abcdefgh'))