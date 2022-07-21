# For this exercise, you need to write a function (hex_output)
# that takes a hex number and returns the decimal equivalent. 
# That is, if the user enters 50, you’ll assume that it’s a hex number
# (equal to 0x50) and will print the value 80 to the screen.

def hex_output(given_hexidecimal_string):
    decimal_value = 0
    #convert string to a list and reverse the order 
    hex_list = list(given_hexidecimal_string)
    reversed_hex_list = hex_list[::-1]
    
    #loop through reversed list multiplying list value by increasing powers of 16
    #and adding to the decimal value
    power = 0
    for digit in reversed_hex_list:
        decimal_value += int(digit, 16) * (16 ** power)
        power += 1
    print(decimal_value)    

        

     

hex_output(input('enter a hexidecimal number you wish to convert: '))
