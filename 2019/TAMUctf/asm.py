rbp_pointer = [65,53,53,51,77,98,49,89]

dec=""
for i in rbp_pointer:
    dec+=(chr(i))

print("gigem{%s}"%dec)
