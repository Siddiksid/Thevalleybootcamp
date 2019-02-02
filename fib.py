def fib(x,mydict):
	if x in mydict:
		return mydict[x]
	else:
		ans=fib(x-1,mydict)+fib(x-2,mydict)
		mydict[x]=ans
		return ans
dict={0:1,1:1,2:2,3:5}
print(fib(1002,dict))

no_of_times=0
def fib1(x):
	terms=[0,1]
	no_of_times+=1
	n=2
	while n<=x:
		terms.append(terms[n-1]+terms[n-2])
		n+=1
	print(no_of_times)

	return terms

print(fib1(5000))
