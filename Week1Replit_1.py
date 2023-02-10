def both_ends():
    s = input("What would you like scrambled?" + '\n')
    slen = len(s)
    sSplit = [*s]
    #print(sSplit)
    if slen <= 2:
        print(s + " should yield " + "''")
    else:
        print (s + " should yield " + sSplit[0] + sSplit[1] + sSplit[-2] + sSplit[-1])
    

both_ends()

both_ends()

both_ends()

both_ends()