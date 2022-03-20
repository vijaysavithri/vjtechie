'''2)sent="today is a friday"
first-word
last-word
first words last char
last words first char'''

'''sent="today is a friday"
wordlst=sent.split()
print(wordlst)
print(wordlst[0])
print(wordlst[3])
print(wordlst[0][-1])
print(wordlst[3][0])'''
#========================================================
'''3)data="10|20|30|40|50|60|70|80"
display the first 4 fields
display the last 4 fields'''
'''data="10|20|30|40|50|60|70|80"
res=data.split("|")
print(res)
print(res[0:4])
print(res[-4:])'''
#==================================================================
'''4)data="12,13,14 15,16 17 18"
display the except first2 & last2'''
'''data="12,13,14 15,16 17 18"
res=data.replace(","," ").split(" ")[2:-2]
print(res)'''
#==================================================================
'''5)data="12-may-2017 16:45:20"
display the no of hours'''
'''data="12-may-2017 16:45:20"
res=data.split(" ")[1]
print(res.split(":")[0])'''
#=======================================================================
'''6)data="ravi-cse-blr-10,20,30  - find total marks'''
'''data="ravi-cse-blr-10,20,30"
res=data.replace("-",",").split(",")[-3:]
mlst=map(int,res)
print(sum(mlst))'''
#========================================================================
'''map-lambda
1)alst=["arun","ravi","mani","john"]
#convert all the name to uppercase
'''
'''alst=["arun","ravi","mani","john"]
#convert all the name to uppercase
print(list(map(str.upper, alst)))
print(list(map(lambda x : x.upper(), alst)))'''
#============================================================================
#2)
'''alst=["arun","ravi","mani","john"]
#collect all the first chars
print(list(map(lambda x:x[0],alst )))
#collect all the first & last chars
print(list(map(lambda x:x[0]+x[-1],alst)))'''
#=====================================================================
'''4)numlst=[10,20,30,40,50,60]
# find the sum of all the first digits'''
'''numlst=[105,208,30,40,50,60]
#print(sum(list(map(lambda x:x//10,numlst))))
print(sum(map(lambda x:int(str(x)[0]),numlst)))'''
#==========================================================================
'''5)dates=["12-jan","13-feb","14-mar","15-apr"]
# collect all the months'''
'''dates=["12-jan","13-feb","14-mar","15-apr"]
print(list(map(lambda x:x.split("-")[1],dates)))'''
#===========================================================================
'''6)studs=["arun,10","ravi,20","chet,30"]
# total marks'''
'''studs=["arun,10","ravi,20","chet,30"]
print(sum(map(lambda x:int(x.split(",")[1]),studs)))'''
#============================================================================
'''7)numlst=[10,20,30,40,50]
# incr every element by 5'''
'''numlst=[10,20,30,40,50]
print(list(map(lambda x:x+5,numlst)))'''
#=================================================================================
'''namelst=["arun","guru","hari","yash"]
# swap the first & last letter'''
'''namelst=["arun","guru","hari","yash"]
print(list(map(lambda x:x[-1]+x[1:-1]+x[0],namelst)))'''
#=================================================================================
''''''



