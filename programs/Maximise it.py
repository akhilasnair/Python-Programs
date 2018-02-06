# Maximise it!!!
#Enter the number of lists you want to enter and a value between 1 and 1000(this is the modulo value)
a, m = input().split(' ')
a, m = [int(a), int(m)]
lists = [[] for i in range(a)]
modlist = [[] for i in range(a)]
for i in range(0, a):
    #length of the list
    n = int(input("enter length of string"))
    for j in range(n):
        #enter the values in the list
        value = int(input())
        #calculate mode of each value
        modv = value % m
        lists[i].append(value)
        #mode value list
        modlist[i].append(modv)
squarelist = []
largelist = [[] for i in range(a)]
large = 0
#find the index of the largest mode value in each list
for i in range(0, a):
    large = modlist[i].index(max(modlist[i]))
    num = large + 1
    largelist[i].append(num)
#seperate those values in the original with index same as the the largest mode value index
for i in range(0, a):
    for n in largelist[i]:
        squarelist.append(lists[i][n - 1])
sq = 0
#calculate the accumulative sum of the squares of the result and obtain the maximum value
for i in range(len(squarelist)):
    sq += (squarelist[i]*squarelist[i])
result = sq % m
print(result)
