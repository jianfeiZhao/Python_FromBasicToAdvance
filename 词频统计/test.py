f=open("threekingdoms.txt","rb")
while True:
    line=f.readline()
    if not line:
        break
    else:
        try:
            line.decode("utf-8","ignore")
        except:
            print(str(line))
