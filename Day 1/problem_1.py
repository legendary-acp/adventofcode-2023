import os

cwd=os.getcwd()
rp="Day 1\\Input\\"
fn="data.txt"
cp=os.path.join(cwd, rp, fn)

with open(cp, 'r') as file:
    lines = file.readlines()

sum=0

for i in lines:
    f=""
    l=""
    for j in i:
        if(j.isdigit()):
            if(f==""):
                f=j
            l=j      
    sum+=int(f+l)

print(sum)