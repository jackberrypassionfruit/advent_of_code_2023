import re

with open('../src/input.txt', 'rt') as f:
    lines = f.readlines()
    
maxes = dict({
    'red':      12,
    'green':    13,
    'blue':     14
})

feas_games = []

for line in lines:
    breakout = False
    line = line.rstrip('\n')
    game, line = line.split(': ')
    game_num = int(game[5:])
    print(f'\n\n{game_num=}')
    
    cubes = re.split('; |, ', line)
    cubes = [ (color, count) for count, color in [ cube.split(' ') for cube in cubes ] ]  
    
    for color, count in cubes:
        print(f'{color=}, {count=}')
        if int(count) > maxes[color]:
            breakout = True
            continue
    if not breakout:
        feas_games.append(game_num)
    
print(f'{sum(feas_games)=}')