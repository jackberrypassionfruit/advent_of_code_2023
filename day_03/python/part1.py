import numpy as np
with open('../src/input.txt', 'rt') as f:
    input= f.read()
schematic = input.split('\n')

def get_part_numbers_ints_w_coords(input: str) -> list:
    # get list of integers with their coords
    part_numbers_ints_w_coords = [] # to be filled with lists, of integers and their coord tuples

    for y, line in enumerate(schematic):
        current_digit = ''
        current_coords = set()
        for x, char in enumerate(line):
            if char.isnumeric():
                current_digit += char
                current_coords.add((x, y))
                
            # char may be '.' or symbol
            elif current_digit == '':   # haven't started a digit yet
                pass
            else:                       # finished a digit
                part_numbers_ints_w_coords.append({
                    'digit': int(current_digit), 
                    'coords': current_coords
                })
                current_digit = ''
                current_coords = set()
                
        # if the line ends while finishing a digit 
        if current_digit != '':
            part_numbers_ints_w_coords.append({
                'digit': int(current_digit), 
                'coords': current_coords
            })
            
    return part_numbers_ints_w_coords

def add_perimeter_chars(part_numbers_ints_w_coords):
    x_min, x_max = 0, len(schematic[0]) - 1
    y_min, y_max = 0, len(schematic) - 1

    for digit_index, digit_dict in enumerate(part_numbers_ints_w_coords):
        perimeter_coords = set()
        perimeter_chars = set()
        for coord in digit_dict['coords']:
            x_coord, y_coord = coord
            for dx in range(-1, 1+1):
                for dy in range(-1, 1+1):
                    this_coord_x, this_coords_y = x_coord+dx, y_coord+dy
                    if (this_coord_x, this_coords_y) not in digit_dict['coords'] and\
                        x_min <= x_coord+dx <= x_max and\
                        y_min <= y_coord+dy <= y_max:
                        perimeter_coords.add((this_coord_x, this_coords_y))
                        perimeter_chars.add(schematic[this_coords_y][this_coord_x])
        perimeter_coords = sorted(list(perimeter_coords))
        # part_numbers_ints_w_coords[digit_index]['perimeter_coords'] = perimeter_coords
        part_numbers_ints_w_coords[digit_index]['perimeter_chars'] = perimeter_chars


part_numbers_ints_w_coords = get_part_numbers_ints_w_coords(schematic)   
add_perimeter_chars(part_numbers_ints_w_coords)

# part_numbers_ints_w_coords = [pn for pn in part_numbers_ints_w_coords if all([True for x_coord, y_coord in pn['perimeter_coords'] if schematic[y_coord][x_coord] == '.']) ]
part_numbers_ints_w_coords = [pn for pn in part_numbers_ints_w_coords if pn['perimeter_chars'] != set({'.'})]


# for digit in part_numbers_ints_w_coords:
#     print(digit)
    
pn_sum = sum([pn['digit'] for pn in part_numbers_ints_w_coords])
print(f'{pn_sum=}')