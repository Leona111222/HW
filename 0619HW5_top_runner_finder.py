file=open("runners.txt",'r') 
wholeTextLines=file.readlines()
#print(wholeTextLines)
for k in range(len(wholeTextLines)):
    wholeTextLines[k] = wholeTextLines[k].strip('\n')  
    wholeTextLines[k] = wholeTextLines[k].split(',')
wholeTextLines.sort(key=lambda s:s[1]) #用lamda指定每個index的value
print(f"ranking list={wholeTextLines}")


number=int(input("pls input one num:"))
for i in range(len(wholeTextLines)):
    try:
        name=wholeTextLines[number-1][0]
        #print(name)
    except:
        number=int(input("pls input another num:"))
    continue
print(name)

