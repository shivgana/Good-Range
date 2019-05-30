def addGR(num,GR):
    k = list(GR.keys())
    k.append(num)
    k=sorted(k)
    for i in range(0,len(k)):
        if(k[i]==num):
            if i==0:
                GR[k[i]] = [1,k[i+1]-1]
                GR[k[i+1]][0] =  k[i]+1
            elif i==len(k)-1:
                GR[k[i]] = [k[i-1]+1,GR[k[i-1]][1]]
                GR[k[i-1]][1] = k[i]-1
            else:
                GR[k[i]] = [k[i-1]+1,k[i+1]-1]
                GR[k[i-1]][1] = k[i]-1
                GR[k[i+1]][0] = k[i]+1
    return (dict(sorted(GR.items())))
        
def add(GR):
    tot = 0
    k = list(GR.keys())
    for i in k:
        tot = GR[i][0]+GR[i][1] + tot
    return tot
GR = {2:[1,10]}
print("2\t",add(GR))
n=9
while n>0:
    num = int(input())
    if num in GR:
        print("Already Exist.Try another number")
        continue
    GR = addGR(num,GR)
    print(num,"\t",add(GR))
    n-=1
