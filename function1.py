def my_newfunc(num1,num2=10) :
     return num1*num2
result1= my_newfunc(12,12)
print(result1)
result2=my_newfunc(12) # num2 value will take default value i.e num2=10 .
print(result2)