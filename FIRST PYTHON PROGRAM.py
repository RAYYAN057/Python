
my_list = [75,72,55,23,80,59,65,58,70,69]
print(my_list)

sum=0
counter = 0
while counter < 10:
 sum = sum + my_list[counter]
 counter = counter+1

print(sum)


average = sum/10

print(average)
 

if average > 60:
    print('B')

elif average >80:
    print ('A')


counter_1 = 1
a=my_list[0]
while counter_1<10:
    if a < my_list[counter_1]:
        a=my_list[counter_1]
    counter_1 =counter_1+1

print('Maximum value=',a)


counter_1 = 1
a=my_list[0]
while counter_1<10:
    if a > my_list[counter_1]:
        a=my_list[counter_1]
    counter_1 =counter_1+1

print('Minimum value=',a)

    
