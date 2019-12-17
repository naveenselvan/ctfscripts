#This is the encryption pattern used for Tale of the Sky
import random
import itertools

def encrypt():
	message='it{3e0_33dfnfpa_nu_c3rcjlsd7sd0.}'
	turns = 3
	ct=""
        pos=[]
        index=[]
        counter=0
        print(message)
	for i in range(turns):
		for j in range(0,len(message)-i,turns):
			ct+=message[i+j]
 			pos.append(i+j)
                        index.append(counter)
			counter+=1
	
        ju=['A']*33
	for i,j in zip(pos,index):
		ju[i]=message[j]
                print(i,j)

     	print("".join(ju))
encrypt()

