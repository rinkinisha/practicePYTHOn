# marks = list(map(int,input().split()))
# higest=marks[0]
# for i in range(len(marks)):
#     if marks[i]>higest:
#         higest=marks[i]
# print(higest)

# low=marks[0]
# for mark in marks:
#     if mark < low:
#         low=mark
# print(low)        

# sum=0
# count=0
# for i in range(len(marks)):
#      sum+=marks[i]
#      count=count+1
# avg=sum/count
# print(avg)


# newArr=[]
# for i in range(len(marks)):
#     if marks[i] > 60:
#         newArr.append(marks[i])
# print(newArr)        

# count=0
# newArr=[]
# for i in range(len(marks)):
#     if marks[i] < 60:
#         newArr.append(marks[i])
#         count=count+1
# print(newArr)
# print(count)

# for i in range(len(marks)):
#      marks.sort(reverse=True)

# print(marks[1])

# largest=-1
# second_lar=-1
# for i in range(len(marks)):
#     if marks[i]>largest:
#         second_lar=largest
#         largest=marks[i]
# print(second_lar)        

# Add data
# Update data
# Delete data
# Loop through dictionary
# Nested dictionaries
# List of dictionaries

# students=[]
# n=int(input())
# for i in range(n):
#     name,marks=input().split()
#     student={}
#     student["name"]=name
#     student["marks"]=int(marks)
#     students.append(student)
# print(students)



students={}
name =input()
age=int(input())
students["name"]=name
students["age"]=age
print(students)


# import json
# students=json.loads(input())
# print(students)



