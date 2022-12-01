file = open("elfCalories.txt", "r")
data = file.read()
elfCal=data.split("\n")
maxLen = len(elfCal)
#print(maxLen)
for i in range(maxLen):
    if elfCal[i] == "":
        elfCal[i] = 0
        i -=1
calList=[]
x = 0
for i in range(maxLen):
    if elfCal[i] != 0:
        x = x + int(elfCal[i])
    else:
        calList.append(x)
        x = 0
print(max(calList))