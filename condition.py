# age=int(input())
# if age >= 18:
#     print("yes")
# else:
#     print("no")    


num=int(input())
# print(num*num)
for i in range( 1,num):
    if(i*i==num):
        print(i)
        break;
    elif(i*i>num):
        print(i-1)    