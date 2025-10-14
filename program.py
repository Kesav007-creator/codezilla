#TASK 4 : DSA FUNDAMENTALS(PYTHON)
'''
#D1 : count how many times 'l' appears in "hello world"
print("count how many times 'l' appears in 'hello world'")
a = "hello world"
count=0
for i in a:
    if i =="l":
        count+=1
print("number of times 'l' appeared in 'hello world' is -",count)

#D2 : find the smallest value in an array of 8 integers
print("\nfind the smallest value in an array of 8 integers")
l=[]
for i in range(8):
    a=int(input("enter number >"))
    l.append(a)
min =l[0]
for i in range(len(l)):
    if min> l[i]:
        min=l[i]
print("\nthe smallest value in the array is",min)


#D3 : manually find the 2nd largest number in an array
print("\n manually find the 2nd largest number in an array")
l=[]
n = int(input("enter number of elements u want to enter into array"))
if n<2:
    print("enter 2 or more numbers")
else:
    for i in range(n):
        a=int(input("enter number >"))
        l.append(a)
    print(l)

    if l[0] > l[1]:
        max = l[0]
        sec = l[1]
    else:
        max = l[1]
        sec = l[0]
    
    for i in range(2,len(l)):
        if max<l[i]:
            sec=max
            max=l[i]
        elif sec<l[i] and l[i]!=max:
            sec=l[i]
    print("the second largest number in an array is : ",sec)
 '''     
