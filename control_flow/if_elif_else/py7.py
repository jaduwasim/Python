def roman_to_digit(s):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0
    for numeral in s[::-1]:  
        value = roman_numerals[numeral] 
        if value >= prev_value:
            total = total + value 
        else:
            total = total - value
        prev_value = value

    return total

s = input("Enter a Roman numeral: ")
digit_value = roman_to_digit(s.upper())
print(f"The corresponding digit value is: {digit_value}")
