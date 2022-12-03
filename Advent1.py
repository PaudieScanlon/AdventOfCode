file = open("advent1Data.txt", "r")
data = file.read()
elfCal=data.split("\n")
maxLen = len(elfCal)
#print(maxLen)
for i in range(maxLen):
    if elfCal[i] == "":
        elfCal[i] = 0
calList=[]
x = 0
for i in range(maxLen):
    if elfCal[i] != 0:
        x = x + int(elfCal[i])
    else:
        calList.append(x)
        x = 0
calList = calList.sort()
print((calList[-1]))