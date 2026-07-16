#[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] *  METRIX  * ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]


# metrix1=[[1,2,3], [4, 5, 6],[7,8,9]]
# # print(metrix1)
# for i in metrix1:
#     for j in i:
#         print(j,end="    ")
#     print()   # for print in next line

#output: 1    2    3    
#        4    5    6    
#        7    8    9  
#========================================================================================================================================

#PROBLOM 1 :   READ TWO METRIX AND PRINT ITS RESULT METRIX.

#=========================================================================================================================================
# #solution:


# metri1  =[]
# metri2  =[]
# metri_sum=[]
# row=int(input("how many row in your metrix   :"))
# col=int(input("how many column in your metrix:"))

# for i in range(row):
#     sub1=[]
#     for j in range(col):
#         data=int(input(f"enter data for first metrix==> [ {i}:{j} ] :"))
#         sub1.append(data)
#     metri1.append(sub1)


# for i in range(row):
#     sub1=[]
#     for j in range(col):
#         data=int(input(f"enter data for  metrix==> [ {i}:{j} ] :"))
#         sub1.append(data)
#     metri2.append(sub1)

# for i in range(row):
#     temp=[]
#     for j in range(col):
#         temp.append(metri1[i][j] + metri2[i][j])
#     metri_sum.append(temp)


# print("\n FIRST METRIX:\n------------------------------------\n")
# for i in range(row):
#     for j in range(col):
#         print(metri1[i][j],end="   ")
#     print("\n")
    
# print("\n SECOND METRIX:\n------------------------------------\n")

# for i in range(row):
#     for j in range(col):
#         print(metri2[i][j], end="  ")
#     print("\n")

# print("\n RESULT METRIX:\n------------------------------------\n")

# for i in range(row):
#     for j in range(col):
#         print(metri_sum[i][j], end="  ")
#     print("\n")
#========================================================================================================================================

#PROBLOM 2 :   READ TWO METRIX AND PRINT ITS DEFFERENCE METRIX.(SUBSTACTION)

#=========================================================================================================================================
#solution:


# metri1  =[]
# metri2  =[]
# metri_sum=[]
# row=int(input("how many row in your metrix   :"))
# col=int(input("how many column in your metrix:"))

# for i in range(row):
#     sub1=[]
#     for j in range(col):
#         data=int(input(f"enter data for first metrix==> [ {i}:{j} ] :"))
#         sub1.append(data)
#     metri1.append(sub1)


# for i in range(row):
#     sub1=[]
#     for j in range(col):
#         data=int(input(f"enter data for  metrix==> [ {i}:{j} ] :"))
#         sub1.append(data)
#     metri2.append(sub1)

# for i in range(row):
#     temp=[]
#     for j in range(col):
#         temp.append(metri1[i][j] - metri2[i][j])
#     metri_sum.append(temp)


# print("\n FIRST METRIX:\n------------------------------------\n")
# for i in range(row):
#     for j in range(col):
#         print(metri1[i][j],end="     ")
#     print("\n") 
    
# print("\n SECOND METRIX:\n------------------------------------\n")

# for i in range(row):
#     for j in range(col):
#         print(metri2[i][j], end="    ")
#     print("\n")

# print("\n RESULT METRIX:\n------------------------------------\n")

# for i in range(row):
#     for j in range(col):
#         print(metri_sum[i][j], end="    ")
#     print("\n")

#=========================================================================================================================================
#PROBLOM 3 : [3 X 3] METRIX MULTIPLICATION

#=========================================================================================================================================
#solution:

#-------------------#         #-------------------#             #--------------------------#
#       1   2   1   |         #       2   1   0   |             #           9    3    2    |
#  [M1] 0   1   2   |    X    #  [M2] 3   0   1   | ========>   # [result]  5    4    1    |        
#       3   0   2   |         #       1   2   0   |             #           8    7    0    |      
#-------------------#         #-------------------#             #--------------------------#    
m1=[[1, 2, 1], [0, 1, 2], [3, 0, 2]]
m2=[[2, 1, 0], [3, 0, 1], [1, 2, 0]]
result_main_lst=[]
for i in range(3):
    sub_lst=[]

    for j in range(3):
        r=0
        for k in range(3):
            r+=m1[i][k]*m2[k][j]
        sub_lst.append(r)
    result_main_lst.append(sub_lst)
for r in range(3):
    for c in range(3):
        print(result_main_lst[r][c],end="   ")
    print()

#output:   9   3   2   
#          5   4   1   
#          8   7   0  
#=========================================================================================================================================
        
            

    

    
    



        


