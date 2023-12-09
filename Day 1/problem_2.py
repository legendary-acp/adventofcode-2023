import os
import sys

cwd=os.getcwd()
rp="Day 1\\Input\\"
fn="data.txt"
cp=os.path.join(cwd, rp, fn)

with open(cp, 'r') as file:
    lines = file.readlines()

sum=0
spelled_out_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for i in lines:
    fd=sys.maxsize
    ld=sys.maxsize
    fs=sys.maxsize
    fsd=sys.maxsize
    ls=sys.maxsize
    lsd=sys.maxsize
    for index, char in enumerate(i):
        if(char.isdigit()):
            if fd==sys.maxsize:
                fd=index
            ld=index
        for ind, number in enumerate(spelled_out_numbers):
            if i[index:index+len(number)].lower() == number:
                if fs==sys.maxsize:
                    fs = index
                    fsd = ind + 1 
                ls = index
                lsd = ind + 1
    if fd < fs:
        f=i[fd]
    else:
        f=str(fsd)
    if ld > ls or ls==sys.maxsize:
        l=i[ld]
    else:
        l=str(lsd)  
    sum+=int(f+l)
                
print(sum)