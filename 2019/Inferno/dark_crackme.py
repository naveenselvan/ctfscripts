from itertools import chain, product

cipher = "1_4m_th3_wh1t3r0s3"

flag = ['*']* 0x24
s1 = "ADGJLQETUOZCBM10"
s2 = "sfhkwryipxvn5238"

i = 0

flag=''



def bruteforce(charset, maxlength):
    		return (''.join(candidate)
        	for candidate in chain.from_iterable(product(charset, repeat=i)
        	for i in range(1, maxlength + 1)))



combinations=(list(bruteforce(s1+s2, 2)))

combinations= [i for i in combinations if len(i)>1]


def bin_generate(checkbyte):
    mem_area= ['1']*4
    in_index = 3
    while checkbyte > 0:
        if checkbyte &1:
            mem_area[in_index]=0
        else:
            mem_area[in_index]=1
        in_index-=1
        checkbyte=int(checkbyte/2)
    return mem_area     


fl=''
for j in cipher:
    for i in combinations:
        if i[0].isupper() and i[1].islower():
            first=s1.find(i[0])
            second=s2.find(i[1])

            even=bin_generate(first)
            odd=bin_generate(second)

            temp=[0]*8
            for index in range(0,8,1):
                if index & 1:
                    temp[index] = str(odd[int(index/2)])
                else:
                    temp[index]=str(even[int(index/2)])

            n = int('0b'+''.join(temp), 2)
            if chr(n) == j:
                fl+=i


print("username: "+cipher)
print("pass: "+fl)

