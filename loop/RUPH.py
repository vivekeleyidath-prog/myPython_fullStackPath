# # x=input("enter:")
# # print(x.upper())

# st=input("enter a string:")
# letc={}
# for let in st:
#     if let not in letc:
#         letc[let]=1
#     else:
#         letc[let]+=1
# print(letc)
# print(f"the letter that most in this word is: {max(letc)} that apeare {letc[max(letc)]} times")




#==================================================================================================================
#problom:

                                # CREATE A SIMPLE CALCULATOR WITH function
                                # NB: saprate functions for each operators
                                #   : the calculator should work in a single line input 
                                #   : eg: 34+55
                                #       : 89


#==================================================================================================================
#solution:

def add(n1,n2):
    return float(n1)+float(n2)

def substract(n1,n2):
    return float(n1)-float(n2)

def mul(n1,n2):
    return float(n1)*float(n2)

def div(n1,n2):
    return float(n1)/float(n2)

st=input("YOU CAN SIMPLY ENTER OPERATION IN THE SAME LINE(LIKE 1+5,etc..):")
ops="+ - * / %"
op=""
n1=""
n2=""
reach_op=False

for ch in st:
    if ch ==" ":
        continue
    if ch not in ops :
        if not reach_op:
            n1+=ch
    if ch in ops:
        op+=ch
        reach_op=True
    if ch not in ops and  reach_op:
        n2+=ch
if op == '+':
    print(add(n1,n2))
elif op == '-':
    print(substract(n1,n2))
elif op == '*':
    print(mul(n1,n2))
elif op == '/':
    print(div(n1,n2))
else:
    print("syntax error")



    