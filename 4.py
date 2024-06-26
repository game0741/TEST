"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""
def number_to_roman(number):
    if number <= 0:
        return "number can not less than 0"
    
    # Define mappings for Roman numerals
    roman_numerals = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL",
        50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM",
        1000: "M"
    }
    # Define the order of keys for conversion
    sorted_keys = sorted(roman_numerals.keys(), reverse=True)

    # Convert the number to Roman numeral
    roman_text = ""
    for key in sorted_keys:
        while number >= key:
            roman_text += roman_numerals[key]
            number -= key

    return roman_text

print(number_to_roman(101))
print(number_to_roman(-1))
