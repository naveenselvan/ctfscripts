import string
import itertools

key=[1847,1878,443,384]               #runtime-dump


source = "ТЄЂђЭБёщФКєѹЯћЅѹѺеЂЖХЌДГѸеДЙѴѕМ"        #static sring to be XOR-ed  

crypt_code=''
index=0
for i in source:
    crypt_code+=chr(ord(i)^(key[index%4]))          #XOR-ed String
    index+=1


the_string = crypt_code

possibleset = string.ascii_letters + string.digits + "_@!?-{}"



for hashind in range(4):
    print("-----------------")
    key=[]
    for p in possibleset:     #Iterate through Strings of 0,1,3,4
        testsol = ord(the_string[hashind]) ^ ord(p)  #Xor The string Index With P, First four letters are already tested
        for j in range(hashind + 4, len(the_string), 4):     #Iterate Through Particular Index Of the The String  
            if chr(testsol ^ ord(the_string[j])) not in possibleset:  #If it not Present in the Printable Ascii Range Exit from the loop ensure it matches with the appropriate index
                break
        else:
            print(testsol)
            key.append(testsol)
    print(key)
    print("-----------------")


def crypt(enc, key):
    """
    enc: encrypted (unicode)
    key: key (bytes)
    """
    c = ""
    for i in range(len(enc)):
        c += chr(ord(enc[i]) ^ key[i % len(key)])

    return c



#print(crypt(crypt_code, [892,828,1498,1446]))



l1=[[892, 891, 810],[820, 821,828],[1498,1501,1500,1503],[1440, 1441, 1446]]
for list in itertools.product(*l1):
    #index=index+1
    temp=crypt(crypt_code, list)
    if 'inctf{' in temp:
        print(temp)
        print(temp)



