unwanted="%HAu]\\UTYXQPia\'IONGFyxqpedMLEDof!=<545ml9-/&80)(@"



cipher='yi}'[::-1]
cipher+='moo'[::-1]



for j in cipher:
    print("-----------------")
    print("\n")
    for i in range(122):
        temp=i&118
        temp=temp|105
        if chr(temp)==j:
            if chr(i) not in unwanted:
                print(chr(i))
