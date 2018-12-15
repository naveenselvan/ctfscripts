converted_input=[]


secret=[105, 110, 99, 116, 102, 123, 116, 104, 101, 95, 49, 95, 80, 77, 95, 111, 102, 95, 73, 110, 100, 105, 97, 95, 74, 97, 119, 97, 104, 97, 114, 108, 97, 108, 95, 78, 101, 104, 114, 117, 95, 114, 97, 105, 115, 101, 100, 95, 116, 104, 101, 95, 110, 97, 116, 105, 111, 110, 97, 108, 95, 102, 108, 97, 103, 125]

print "ENTER THE FLAG........"

your_input=raw_input()
for i in your_input:
	converted_input.append(ord(i))

print(converted_input)	
f=0
if (len(secret)==len(converted_input)):
	print "You are on the right track...Keep going..."
	for k in range(len(secret)):
		if(converted_input[k]!=secret[k]):
			f=1
			break
else:
	f=2
	print "Try harder..\n"

if(f==1):
	print "Try again kiddo...\n"
if(f==0):
	print "YAAYY!!! You are a genius...\n You got the flag..."
		
