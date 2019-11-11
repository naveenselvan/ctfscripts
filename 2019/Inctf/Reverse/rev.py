import string
import random
from itertools import chain, product

def push(x):
    
	upper = string.ascii_uppercase
	lower = string.ascii_lowercase
	digits = string.digits
	n = []
	a = ""
	for i in x:
		if i.isupper() is True:
			n.append(upper[(upper.index(i)+3)%26])
		elif i.islower() is True:
			n.append(lower[(lower.index(i)+3)%26])
		elif i.isdigit() is True:
			n.append(digits[(digits.index(i)+3)%10])
	
	for j in n:
		a+=j

	return a
    

def sage(x): 
	final=[] 
        #print("I am in sage function")
	for i in range(0,len(x),4):
		temp=x[i:i+4].encode('utf-8').hex()
                #print(temp)
		k=int(temp,16)
		final.append(k)
	return k

if __name__=="__main__":
	
	print("Please Enter The input")																	 																								
	#x = input().encode('utf-8').hex() #User_Input
	check = [959592808, 959852599, 960049253, 926430775, 892811314, 946419251, 929576502, 946419765, 909391664, 925972535, 892613940, 912864564, 12391] #Check_List
	ALL = [] #ALL List
	#ALL=sage(push(x))      #Returns a python_list of hex_encoded String
	count = 0
        
	#flag='inctf{E4$Y_0N3_R1GHT!!?!}'
        
        
	def bruteforce(charset, maxlength):
    		return (''.join(candidate)
        	for candidate in chain.from_iterable(product(charset, repeat=i)
        	for i in range(1, maxlength + 1)))
        
	combinations=(list(bruteforce('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;?@_{}', 2))[27:])

	for j in check: 
	    for i in combinations:
	        temp=i.encode('utf-8').hex()
	        ret=sage(push(temp))
	        #print(ret)
	        if ret==j:
	            print(i,end='')       



	#for i in range(len(ALL)):
	#	if check[i] == ALL[i]:
	#		count+=1        #If ALL Check Passes Count Will be 13 
