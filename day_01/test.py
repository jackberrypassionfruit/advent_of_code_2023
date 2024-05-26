
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

row = 'three8eight4fivefourfourfivecxzkqf'

def find_all_digits_in_this_row(row):
    found_this_row = []
    for digit_str in digits.keys():
        try:
            index = row.index(digit_str)
            found_this_row.append((index, digit_str))
        except ValueError:
            pass
    found_this_row.sort(key=lambda pair: pair[0])
    return found_this_row

print(f'{row=}')
found_this_row = find_all_digits_in_this_row(row)
print(f'{found_this_row=}')

while len(found_this_row) != 0:
    first_index, first_digit = found_this_row[0]
    row = row[:first_index] + str(digits[first_digit]) + row[first_index+len(first_digit):]
    print(f'Replacing "{first_digit}" with "{str(digits[first_digit])}"')
    print(f'{row=}')
    
    found_this_row = find_all_digits_in_this_row(row)
    print(f'{found_this_row=}')
    


