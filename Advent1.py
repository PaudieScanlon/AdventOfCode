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
calList.sort(reverse=True)
total = 0
for i in range (3):
    total = total+calList[i]
print(total)