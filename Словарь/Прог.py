n = []
f = open("vocab.txt", "w")
for a in range(1930, 2016):
    for b in range(1, 13):
        if b < 10:
            b = "0" + str(b)
        for c in range(1,32):
            if c < 10:
                c = "0"+str(c)
            n = str(c)+ str(b)+str(a)+"\n"
            f.write(n)
f.close()
