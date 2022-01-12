# Enter your code here. Read input from STDIN. Print output to STDOUT
dict = {}
t = int(input().strip())
for i in range(t):
    txt = input().split()
    dict[txt[0]] = txt[1]

for i in range(t):
    key = str(input())
    if (key in dict):
        print(key,"=",dict[key],sep="")
    else:
        print("Not found")