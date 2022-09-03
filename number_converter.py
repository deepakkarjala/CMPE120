def nibble_to_ascii(nibble: int) -> str:
  """
  This is a comment
  Input: Nibble (4-bits)
  Output: Single character HEX as a string
  Example: Input = 10, Output = 'A'
  Example: Input = 8,  Output = '8'
  """
  table = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  return table[nibble]


def to_hex(number: int) -> str:
    """
    This is a comment
    Input: Number (integer)
    Output: String
    Example: Input = 43605, Output = "0xAA55"
    """
    answer = ""
    
    # Forever loop
    while True:
        # Integer divide using the // operator
        quotient = number // 16
        # Get the remainder using the % operator
        remainder = number % 16
        
        # Accumulate result
        answer = nibble_to_ascii(remainder) + answer

        # Set the number we need to use for next time
        number = quotient
        
        # We break the "loop" when division turns to zero
        if (quotient == 0):
            break
    
    return "0x" + answer

def to_binary(number: int) -> str:
    answer = ""
    while True:
        quotient = number // 2
        remainder = number % 2
        answer = str(remainder) + answer
        number = quotient
        if(quotient == 0):
            break
    return "0b" + answer
        
print(to_hex(123456789))
print(to_hex(0b1010101))
print(to_hex(0xDEADBEEF))
print("----------")
print(to_binary(0xF))
print(to_binary(0b11110000))
print(to_binary(85))