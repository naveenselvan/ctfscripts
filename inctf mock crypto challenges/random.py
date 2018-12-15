import random
x = ''
for i in range(0,9):
    y = random.randint(0,1000)
    if(i%3==0):
        x+='x'
    else:
        x+= str(y^y)
print("Got the password?")
y = raw_input()
print(x)
if(x==y):
    print("Nice!")
else:
    print("Not quite")
