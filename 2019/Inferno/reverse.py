#Source:https://github.com/ByteBandits/writeups/blob/master/inferno-ctf-2019/rev/darkcrackme/exp.py
def rev_bs(s) -> int:
    return ~int(s, 2) & 0xf


stri = "1_4m_th3_wh1t3r0s3"

flag = ['*']* 0x24
s1 = "ADGJLQETUOZCBM10"
s2 = "sfhkwryipxvn5238"

i = 0
while i < len(stri):
    print(i)
    b = ord(stri[i]) #decimal value
    # b = bin(ord(b))[2:]
    b = f'{b:08b}'   #converted binary in 8 digit
    print("Converted Binary : "+stri[i]+" "+str(ord(stri[i])))
    print(b)

    t1 = ''
    t2 = ''

    for idx in range(len(b)):         #iterate in binary
        if idx %2:                  #index mod 2
            t2 += b[idx]            #odd
        else:
            t1 += b[idx]            #even
    print("t1 t2 is")
    print(t1, t2)

    flag[i*2] = s1[rev_bs(t1)]
    flag[i*2+1] = s2[rev_bs(t2)]
    i+=1

print(''.join(flag))
flag = ''.join(flag)

