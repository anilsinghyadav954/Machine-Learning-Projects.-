#____________LIST______________

list1 = [1,2,3,4,5]
sum = 0
print("The element in the list is : ",end=' ')
for i in list1:
    print(i,end=" ")
    sum += i
print()
even_count = 0
odd_count = 0
for i in list1:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even no is : ",even_count," & Odd count is : ",odd_count)   

total_Count = even_count + odd_count

avg = sum / total_Count

print("Average of all list element is : ",avg)



"""
_______________METHODS IN LIST_______________
1.append() 
2.insert()
3.remove()
4.pop()
5.len()
6.extend()
7.reverse()
8.sort
9.clear()
10.copy()
11.count()
_________________END_______________
"""