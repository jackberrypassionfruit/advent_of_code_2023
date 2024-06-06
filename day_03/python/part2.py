
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

def add_perimeter_symbol_coords(part_numbers_ints_w_coords):
    x_min, x_max = 0, len(schematic[0]) - 1
    y_min, y_max = 0, len(schematic) - 1

    for digit_index, digit_dict in enumerate(part_numbers_ints_w_coords):
        perimeter_symbol_coords = set()
        for coord in digit_dict['coords']:
            x_coord, y_coord = coord
            for dx in range(-1, 1+1):
                for dy in range(-1, 1+1):
                    this_coord_x, this_coords_y = x_coord+dx, y_coord+dy
                    if (this_coord_x, this_coords_y) not in digit_dict['coords'] and\
                        x_min <= x_coord+dx <= x_max and\
                        y_min <= y_coord+dy <= y_max and\
                        schematic[this_coords_y][this_coord_x] == '*':
                            
                        perimeter_symbol_coords.add((this_coord_x, this_coords_y))
                        
        part_numbers_ints_w_coords[digit_index]['perimeter_symbol_coords'] = perimeter_symbol_coords

part_numbers_ints_w_coords = get_part_numbers_ints_w_coords(schematic)   
add_perimeter_symbol_coords(part_numbers_ints_w_coords)

        
# for digit_dict in part_numbers_ints_w_coords:
# # for digit_dict in [pn for pn in part_numbers_ints_w_coords if len(pn['perimeter_symbol_coords']) > 1]:
#     print(digit_dict)


paired_gears = set()
for digit_dict in part_numbers_ints_w_coords:
    gear_buddies = [pn for pn in part_numbers_ints_w_coords if digit_dict is not pn and pn['perimeter_symbol_coords'] == digit_dict['perimeter_symbol_coords']]
    if len(gear_buddies) > 0:
        if gear_buddies[0]['perimeter_symbol_coords'] != set():
    #         x, y = list(gear_buddies[0]['perimeter_symbol_coords'])[0]
    #         if schematic[y][x] != '.':
    #             paired_gears.add(tuple(sorted([digit_dict['digit'], gear_buddies[0]['digit']])))
            paired_gears.add(tuple(sorted([digit_dict['digit'], gear_buddies[0]['digit']])))

print(paired_gears)

    
sum_gear_ratios = sum([pair[0]*pair[1] for pair in paired_gears])

print(f'{sum_gear_ratios=}')
# 84211374/5 too low