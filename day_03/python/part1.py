import numpy as np
with open('../src/test_input.txt', 'rt') as f:
    input= f.read()
schematic = input.split('\n')

def get_part_numbers_ints_w_coords(input: str) -> list:
    # get list of integers with their coords
    part_numbers_ints_w_coords = [] # to be filled with lists, of integers and their coord tuples

    for y, line in enumerate(schematic):
        current_digit = ''
        current_coords = []
        for x, char in enumerate(line):
            if char.isnumeric():
                current_digit += char
                current_coords.append((x, y))
                
            # char may be '.' or symbol
            elif current_digit == '':   # haven't started a digit yet
                pass
            else:                       # finished a digit
                part_numbers_ints_w_coords.append((int(current_digit), current_coords))
                current_digit = ''
                current_coords = []
                
        # if the line ends while finishing a digit 
        if current_digit != '':
            part_numbers_ints_w_coords.append((int(current_digit), current_coords))
            
    return part_numbers_ints_w_coords



# part_numbers_ints_w_coords = get_part_numbers_ints_w_coords(schematic)   
# for digit, coords in part_numbers_ints_w_coords:
#     print(f'{digit=}, {coords=}')