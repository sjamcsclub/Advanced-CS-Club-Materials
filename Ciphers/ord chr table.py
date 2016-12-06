c2=32
c3=32
for i in range(1,13):
   if (i % 2)==1:
    s1='chr: '
   else:
    s1='asc: '
   if (s1=='chr: '):
    for j in range(0,16):
     if (j == 0):
            p1=(' ')+chr(c2)
     else:
            p1=3*(' ')+chr(c2)
     s1=s1+p1
     c2=c2+1
    print(s1)
   if (s1=='asc: '):
    for j in range(0,16):
     if(j<15):
            q2=int(ord(chr(c3)))
            if (q2<100):
               p2=(str(int(ord(chr(c3)))))+2*(' ')
            else:
               p2=(str(int(ord(chr(c3)))))+1*(' ')
     else:
            p2=(str(int(ord(chr(c3)))))
     s1=s1+p2
     c3=c3+1
    print(s1)
