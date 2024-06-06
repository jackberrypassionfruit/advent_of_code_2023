with open('../src/test_input.txt', 'rt') as f:
    cards = f.readlines()
    
qty_cards = [1] * len(cards)
for line_index, line in enumerate(cards):
    line = line.split(': ')[1].rstrip('\n')
    winning_nums, my_nums = line.split(' | ')
    
    winning_nums =  set([int(num) for num in winning_nums.split()])
    my_nums =       set([int(num) for num in my_nums.split()])
    
    my_winning_nums = winning_nums.intersection(my_nums)
    score = len(my_winning_nums)
    print(f'{score=}')
    qty_cards = [qty + qty_cards[line_index] if line_index < qty_index <= line_index+score else qty for qty_index, qty in enumerate(qty_cards)]
    print(f'{qty_cards=}')
    
    
print(f'{sum(qty_cards)=}')
    

