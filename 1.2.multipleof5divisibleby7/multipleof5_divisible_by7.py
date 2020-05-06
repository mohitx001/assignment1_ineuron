l=list(range(2000,3201))

m=[]
for i in l:
    if(i%7==0) and (i%5==0):
        m.append(str(i))
print("\n Following are no. which are divisible by 7 and multiple of 5 \n")
print(",".join(m) )
print("\n")
print('from ' , len(l) ,' numbers there are', len(m) , 'numbers divisible by 7 and multiple of 5')


