def convert_to_base(num, base):
    if not (2 <= base <= 16):
        raise ValueError("Base must be between 2 and 16.")
    
    digits = "0123456789ABCDEF"
    
    result = ""
    while num > 0:
        remainder = num % base # Rest der ganzzahligen Division
        num = num // base # Quotient der ganzzahligen Division
        result = digits[remainder] + result
        
    return result
        

print(convert_to_base(156, 2))
print(convert_to_base(156, 8))
print(convert_to_base(156, 16))