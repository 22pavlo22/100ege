f=open('17hard.txt')
f=f.readline()
l=[int(i) for i in f.split()]
l.sort(reverse=True)
l=l[1::2]
s=0
k=0
for j in l:
   if j%3==0 or j%5==0:
      s+=j
      k+=1

print(s,k)







