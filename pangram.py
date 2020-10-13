
str=(input())
str=str.lower()# to convert lowercase
l=[]
for ele in str:
    if(ele!=" " and ele not in l):#to avoid duplicate 
            l.append(ele)
            
            
    else:
        pass
if(len(l)==26):
    print("pangram")
else:
    print("not pangram")



'''i/p:
We promptly judged antique ivory buckles for the next prize
o/p:
pangram'''
