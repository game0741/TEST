"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""

def find_tailing_zeroes(number):
    if number < 0:
        return "number can not be negative"
    
    factorial_result = 1
    for i in range(2, number + 1):
        factorial_result *= i

    count = 0
    while factorial_result % 10 == 0:
        count += 1
        factorial_result //= 10
    
    return count

print(find_tailing_zeroes(7))  
print(find_tailing_zeroes(-10))