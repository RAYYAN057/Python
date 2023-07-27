
my_list = []
b= input('Please enter the total number of values:')
print(type(int(b)))
count = 0
for count in range (int(b)) :
    temp = int(input('Please enter a value to store in the list:'))
    my_list.append(temp)
    count = count + 1

sum=0
counter = 0
for counter in range (int(b)):
    sum = sum + my_list[counter]
    counter = counter + 1 

print(sum)


average = sum/10

print(average)
 

if average > 60:
    print('B')

elif average >80:
    print ('A')


counter_1 = 1
a=my_list[0]
for counter_1 in range (int(b)):
    if a < my_list[counter_1]:
        a=my_list[counter_1]
    counter_1 =counter_1+1

print('Maximum value=',a)


counter_1 = 1
a=my_list[0]
for counter_1 in range (int(b)):
    if a > my_list[counter_1]:
        a=my_list[counter_1]
    counter_1 =counter_1+1

print('Minimum value=',a)




    
