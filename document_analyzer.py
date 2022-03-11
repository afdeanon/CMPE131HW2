import operator

f1 = open("document.txt", "r")
d={}
for i in f1:
    for j in i.split():
        if j[len(j)-1]=="." or j[len(j)-1]=="," or j[len(j)-1]==":" or j[len(j)-1]==";":
            j=j[:len(j)-2:]
        if j not in d:
            d[j]=1
        else:
            d[j]+=1

sort_val = {val[0] : val[1] for val in sorted(d.items(), key = lambda x: (-x[1], x[0]))}

sorted_dict=dict(sorted(sort_val.items(),key=operator.itemgetter(1),reverse=True))

c=0
for i,j in sorted_dict.items():
    if c<5:
        print(i,":",j)
    else:
        break
    c+=1
