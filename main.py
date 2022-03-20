'''Given:-
=======
name="prashanth"	name="raveena"

Expected:-
==========
res="PRAS-hanth"	res="RAVE-ena"'''
'''name=(input("enter the name:"))
out=name[:4].upper()
print(out,"-",name[4:])'''
#=============================================================================================================
'''Given:-
=======
name='arvindan'

Expected:-
==========
res='ArvindaN'''

'''name=input("enter the name:")
out=name[0].upper()+name[1:-1]+name[-1].upper()
print(out)'''
#===================================================================================================================
'''reverse the first 4 letters
reverse the last 4 letters
in bw should be as it is

Given:-
=======
name='some things todo'

Expected:-
==========
res='EMOS things ODOT'''

'''name='some things todo'
first4=name[:4].upper()[::-1]
last4=name[-4:].upper()[::-1]
mid=name[4:-4]
print(first4+mid+last4)'''
#======================================================================================================================
'''Given:-
=======
name="sample"

Expected:-
==========
res= MAS-ELP'''
'''name="sample"
print(name[-4::-1].upper()+"-"+name[3:].upper()[::-1])'''
#==========================================================================================================
'''Given:-
=======
name='abhiram'

Expected:-
==========
res='AHRM-bia'
'''
'''name='abhiram'
evn=[]
odd=[]
for i in range(0,len(name)):
       if i%2==0:
          evn.append(name[i])
       else:
         odd.append(name[i])

print("".join(evn).upper()+"-"+"".join(odd))'''
"or"
#print(name[0::2].upper()+"-"+name[1::2])

'''astr='infinite things finite'

without using replace function
replace the first occurance of "fin" as "***"

Expected:-
==========
res="in***ite things finite'''
'''astr='inite thifinngs finite'
search='fin'
position=astr.index(search)
#print(position)
first=astr[0:position]
replace="*"*len(search)
last=astr[position+len(search):]
print(first+replace+last)'''
#======================================================================================================
'''1)data="12-jan-2017"
display the month field
data="12-jan-2017"
res=data.split("-")[1]
print(res)'''
#================================================================================================
#find least repeated letter
'''a='fecklessness'
b={}
#print(b)
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
c=min(b.values())
for k,v in b.items():
    if v==c:
         print(k,end="")'''
#=========================================================================










