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

num = 156
for base in range(2,17):
    print(f"num: {num}, base: {base:2d} | {convert_to_base(num, base)}")
    

int('9B', 12)

0b0101010
0xAEFBC
0o7624563