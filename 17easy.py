f=open('17easy.txt')
f=f.readline()
l=[int(i) for i in f.split()]
l.sort()
l=l[::2]

s=0
for j in l:
   if j%3==0 or j%5==0:
      s+=j

print(s)







