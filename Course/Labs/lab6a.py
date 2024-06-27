def factorial(num):
    sum=num
    for number in range(num):
        sum+=number
    return sum

print(factorial(5))
print(factorial(10))
