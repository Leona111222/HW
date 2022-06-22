file=open("runners.txt",'r') 
wholeTextLines=file.readlines()
#print(wholeTextLines)
for k in range(len(wholeTextLines)):
    wholeTextLines[k] = wholeTextLines[k].strip('\n')  
    wholeTextLines[k] = wholeTextLines[k].split(',')
wholeTextLines.sort(key=lambda s:s[1]) #用lamda指定每個index的value
print(f"ranking list={wholeTextLines}")


number=int(input("pls input one num:"))
while True:
    try: 
        name=wholeTextLines[number-1][0]
        #print(name)
    except: #mistake
        number=int(input("pls input another num:"))
    else: #no mistake
        break
print(name)

