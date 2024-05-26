
infile = 'input.txt'
with open(infile, 'rt') as f:
    lines = f.readlines()

def get_calibration_from_row_nums(row):
    just_nums = [char for char in list(row) if char.isnumeric()]
    fl_nums_int = int(just_nums[0]+just_nums[-1])
    return fl_nums_int

# print(f'{sum([get_calibration_from_row_nums(row) for row in lines])=}')

digits = {
    'one':      1,
    'two':      2,
    'three':    3,
    'four':     4,
    'five':     5,
    'six':      6,
    'seven':    7,
    'eight':    8,
    'nine':     9,
    'zero':     0
}


def find_all_str_digits_in_this_row(row):
    found_this_row = []
    for digit_str in digits.keys():
        try:
            index = row.index(digit_str)
            found_this_row.append((index, digit_str))
        except ValueError:
            pass
    found_this_row.sort(key=lambda pair: pair[0])
    return found_this_row

def int_str_to_num(row):
    found_this_row = find_all_str_digits_in_this_row(row)
    while len(found_this_row) != 0:
        first_index, first_digit = found_this_row[0]
        row = row[:first_index] + str(digits[first_digit]) + first_digit[1:] + row[first_index+len(first_digit):]
        found_this_row = find_all_str_digits_in_this_row(row)
    return row

# my fancy/correct way
calibrations= []
for row in lines:
    row = row.rstrip('\n')
    print(f'initial row = {row}')
    row =       int_str_to_num(row)
    print(f'replace row = {row}')
    row_cal =   get_calibration_from_row_nums(row)
    print(f'cal val: {row_cal}')
    calibrations.append(row_cal)
    print()
        
print(f'{sum(calibrations)=}')



# the stupid/incorrect way
# def find_all_int_digits_in_this_row(row):
#     all_int_digits_in_this_row = []
#     for char_index, char in enumerate(row):
#         if char.isnumeric():
#             all_int_digits_in_this_row.append((char_index, char))
#     return all_int_digits_in_this_row
            

# calibrations= []
# for row in lines:
#     row = row.rstrip('\n')
#     all_str_digits_in_this_row =    find_all_str_digits_in_this_row(row)
#     all_str_digits_in_this_row =    [(pair[0], str(digits[pair[1]])) for pair in all_str_digits_in_this_row]
    
#     all_int_digits_in_this_row =    find_all_int_digits_in_this_row(row)
    
#     all_digits_in_this_row = sorted(all_str_digits_in_this_row+all_int_digits_in_this_row, key=lambda pair: pair[0])
#     # print(f'{all_digits_in_this_row=}')
#     row_cal = int(all_digits_in_this_row[0][1] + all_digits_in_this_row[-1][1])
#     # print(f'{row_cal=}')
#     calibrations.append(row_cal)
#     # print()
        
# print(f'{sum(calibrations)=}')
