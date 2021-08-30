
# Let's Code Loops !
# Write a Python program to print all positive numbers in a range.
# Stored in a list

def positive_number(list1):
    output=[]
    for number in list1:
        if(number>0):
            output.append(number)


    return output



num=int(input("Enter the total numbers in list :"))
list2=[]
print("Enter the ",num," numbers")
for i in range(0,num):
    list2.append(int(input()))


result=positive_number(list2)
print(result)