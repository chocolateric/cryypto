from pwn import *
import math


conn = remote('140.114.77.172', 8011)


for i in range(10000):
    S = conn.recvlineS()
    Slist = S.split()
    a = Slist[0]
    b = Slist[3]

    r1 = int(a)
    r2 = int(b)
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1

    while(r2 > 0):
        q = math.floor(r1/r2)
        r = r1 - q*r2
        r1 = r2
        r2 = r

        s = s1 - q*s2
        s1 = s2
        s2 = s

        t = t1 - q*t2
        t1 = t2
        t2 = t

    g = r1
    s = s1
    t = t1

    conn.send(str(g) + " " + str(s) + " " + str(t) + "\n")
    print("finish number " + str(i))

S1 = conn.recvlineS()

print(S1)



conn.close()
