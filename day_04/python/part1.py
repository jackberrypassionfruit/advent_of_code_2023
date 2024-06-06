import re

with open('../src/input.txt', 'rt') as f:
    cards = f.readlines()
    
game_scores = 0
for line_index, line in enumerate(cards):
    # print(line_index)
    line = line.split(': ')[1].rstrip('\n')
    winning_nums, my_nums = line.split(' | ')
    # winning_nums =  set([int(num) for num in re.split(r'^+\s$', winning_nums)])
    # my_nums =       set([int(num) for num in re.split(r'^+\s$', my_nums)])
    
    winning_nums =  set([int(num) for num in winning_nums.split()])
    my_nums =       set([int(num) for num in my_nums.split()])
    
    my_winning_nums = winning_nums.intersection(my_nums)
    game_scores += int(2**(len(my_winning_nums) - 1))
    
    # print(f'card: {line_index+1}: {my_winning_nums=}')
    # print(f'card: {line_index+1}, score: {int(2**(len(my_winning_nums) - 1))=}')
    # print()
    
    
print(f'{game_scores=}')