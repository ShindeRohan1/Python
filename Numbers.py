def DisplayFactors(No):
    i = 1
    while(i <= int(No / 2)):
        if No % i == 0:
            print(i)
        i = i + 1