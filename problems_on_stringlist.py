'''1) check the given string is a PALINDROME
   case insensitive

   Gadag  - pal
   nitin  - pal
   ravi   - not a pal

2) check the given number is odd/even

3) check the given number is +ve/-ve/zero
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

4) check the given name last char is VOWEL/CONSO

name=raw_input("enter the string : ").lower()

if name[-1] in "aeiou":
  print "Vowel"
else:
  print "Conso"


5) check the given number is b/w 1 to 100

6) given date in dd-mm-yyyy format
                 or
                 dd/mm/yyyy format
   check whether month field is VALID'''
'''#1
inpt=input("enter:")
inpt1=inpt[::-1]
if inpt==inpt1:
    print("strn is palindrome")
else:
    print("strn is not palindrome")'''
#=================================================================================

'''#2
num=int(input("enter:"))
if num%2==0:
    print('numer is even')
else:
    print('number is  odd')'''
#====================================================================================
#4) check the given name last char is VOWEL/CONSO
'''astr=input("enter:")
a=['a','e','i','o','u']
if astr[-1] in a:
    print("last char is vowel")
else:
    print("last char is consonant")'''
#=======================================================================================
#5) check the given number is b/w 1 to 100
'''num=int(input("enter:"))
if num>100:
    print("given number is not i b/w 1 to 100")
else:
    print("given number is b/w 1 to 100")'''
#========================================================================================
'''given date in dd-mm-yyyy format
                 or
                 dd/mm/yyyy format
   check whether month field is VALID'''
'''date=str(input("enter:"))
md=date.replace("/","-").split("-")[1]
if int(md)>=1 and int(md)<=12:
    print("month field is VALID")
else:
    print("month field is not valid")'''
#==================================================================================
#check given number is ARMSTRONG number ex: 407 is armstrong

'''num=input("enter:")
pow=len(num)
mint=map(int,num)
res=sum(map(lambda x:x**pow,mint))
#print(res)
if int(num)==res:
    print("number is amstrong")
else:
    print("number is not amstrong")'''
#=======================================================================================
'''Given:-
=======
num=1234

Expected:
=========
one two three four'''
'''num=input("enter:")
astr=['zero','one','two','three','four','five','six','seven','eight','nine']
for i in num:
    res=astr[int(i)]
    print(res,end=" ")'''
#=========================================================================================
'''1)prodlst=[
         "DVD-10",
         "MON-40",
         "CPU-43",
         "KEB-27",
         "PRN-35"
        ]
total -Qty
display only prod-names >=30'''
prodlst=["DVD-10",
         "MON-40",
         "CPU-43",
         "KEB-27",
         "PRN-35"]
'''total=0
prod=[]
for i in prodlst:
    #total+=int(prodlst[i].split("-")[1])
    #prod.append((prodlst[i].split("-")[0]))
    name, qty = i.split("-")
    prod.append(name)
    total+=int(qty)
print(total)
print(prod)'''
#=============================================================================================










