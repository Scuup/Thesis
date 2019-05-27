#f = open("testun10000.txt", "r")
#print(f.read())
f  = open('Ratinkaantov2.txt', 'r+')
f1 = open('Ratinkaantov2Converted.txt','a')
i=0
for line in f.readlines():
    #print (len(line[17:70]))
    data = line.split(",")
    #print(len(data))
    if len(data)==14:
        f1.write(line)
        print("removed")
        i=i+1

print(i)
f.close()
f1.close()
