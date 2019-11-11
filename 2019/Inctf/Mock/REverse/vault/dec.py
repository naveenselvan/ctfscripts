original='abcdefghijklmnopqrstuvwxy'
modified='adexiwmcqluhybfjnrvgkospt'

loc=[]
for i in original:
    loc.append(modified.find(i))


original='M_ToFYeY_Ch_u4h0_W_3rbiEt'


fl=''
for i in loc:
    fl+=original[i]


print(fl)        

