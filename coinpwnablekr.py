from pwn import *


p= remote("localhost","9007")

print(p.recv())




for q in range(100):
        r=(p.recv())
        N=int((r.split(" ")[0])[2:])
        C=int((r.split(" ")[1])[2:])
        print(N)
        print(C)

        min = 0
        max = N -1


        for x in range(0,C):
                mid = (max -min)/2 + min
                msg = ' '.join([str(x) for x in range(min,mid)])
                print(msg)
                p.sendline(msg)
                result=p.recv()
                print(result)
                if int(result)%10 == 0:
                        min =mid
                else:
                        max = mid
        p.sendline(str(min))
        p.recv()
        print("loop",q)
print("final")
print(p.recv())
