#variable={key_expresion:value_expresion for iteam in itearabe if condition}


#======================================================================================================================================

#                                   # create a dictioinary number is the key and its squre  is the value

#======================================================================================================================================
# #solution 1: treditional method
# numbers=[1,2,3,4,5,6,7,8,9,10]
# sqr={}
# for i in numbers:
#     sqr[i]=i*i
# print(sqr)

#======================================================================================================================================
#solution 2: used dictionary_comperhenson method
# numbers=[1,2,3,4,5,6,7,8,9,10]
# sqr={}
# sqr={i:i**2 for i in numbers}
# print(sqr)

#Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

#======================================================================================================================================

                    # swap key and value in a dic..., dictionary is  dic={'a':1,'b':2,'c':3} to dic={1:'a',2:'b',3:'c'}

#======================================================================================================================================
#solution:

dic={'a':1,'b':2,'c':3,'d':4}
invertDic={j:i for i,j in dic.items()}
print(invertDic)









# create a dic of charectors and there ascii value from a given strung

# student name and mark in to a dic and find the count of student who get more mae=rk than 50
# update the mark of a given student in a dic
# 



