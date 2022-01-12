t = int(input())
for i in range(0, t):
    S = str(input())         
    even = S[::2]
    odd = S[1::2]
    print(even,odd)
