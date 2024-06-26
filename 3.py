"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""
def number_to_thai_text(number):
    if number < 0 or number > 10000000:
        return "number can not less than 0"

    if number == 0:
        return "ศูนย์"

    thai_digits = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", 
                   "หก", "เจ็ด", "แปด", "เก้า"]
    thai_tens = ["", "สิบ", "ร้อย", "พัน", "หมื่น", 
                 "แสน", "ล้าน"]
    thai_positions = ["", "สิบ", "ร้อย", "พัน", "หมื่น", 
                      "แสน", "ล้าน"]

    num_text = ""
    digits = []
    
    while number > 0:
        digits.append(number % 10)
        number //= 10
    
    digits.reverse()  
    
    # Generate Thai text
    for i, digit in enumerate(digits):
        if digit > 0:
            if i == len(digits) - 1 and digit == 1 and len(digits) > 1:
                num_text += "เอ็ด"
            elif i == len(digits) - 2 and digit == 2:
                num_text += "ยี่"
            else:
                num_text += thai_digits[digit]
            
            num_text += thai_positions[len(digits) - i - 1]

    return num_text

print(number_to_thai_text(101))
print(number_to_thai_text(-1))
