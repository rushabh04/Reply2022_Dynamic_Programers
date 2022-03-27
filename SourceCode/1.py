import os
def des(x,cst):
    if x[2] < x[4]: return True
    if cst>10: return True
    
if os.path.exists("../OutPut/0.txt"):
    os.remove("../OutPut/0.txt")
r = open("../OutPut/0.txt", "a")
f = open('../Input/0.txt')
i = 0
lines = f.readlines()
line = lines[i]
i+=1
PandaInfo = line.split()
cST = int(PandaInfo[0])
mST = int(PandaInfo[1])
T = int(PandaInfo[2])
D = int(PandaInfo[3])
Demons = []
pos = []
for x in range(D):
    sum = 0
    Dat = []
    D = lines[i].split()
    for j in range(4):
        Dat.append(int(D[j]))
    for j in range(4,len(D)):
        sum += int(D[j])
    Demons.append([100000000-sum,mST-Dat[0],Dat[0],Dat[1],Dat[2],x])
    i+=1
Demons.sort()
day = 0 
sR = {}
while day <=  T:
    print(cST)
    flag = False
    for x in Demons:
        if cST >= x[2] and x[0] < 100000000 and des(x,cST) :
            flag = True
            print(x)
            cST -= x[2]
            if day+x[3] in sR.keys():
                sR[day+x[3]] += x[4]
            else :
                sR[day+x[3]] = x[4]
            r.write(str(x[5]))
            r.write("\n")
            Demons.remove(x)
            break
    if flag == False:
        for x in Demons:
            if cST >= x[2] and x[2] < x[4]:
                flag = True
                print(x)
                cST -= x[2]
                if day+x[3] in sR.keys():
                    sR[day+x[3]] += x[4]
                else :
                    sR[day+x[3]] = x[4]
                r.write(str(x[5]))
                r.write("\n")
                Demons.remove(x)
                break

    if day+1 in sR.keys():
        print("increased")
        cST += sR[day+1]
    day +=1
    # print(day)