import re

with open('../src/input.txt', 'rt') as f:
    lines = f.readlines()

min_colors_reqd = []

for line in lines:
    line = line.rstrip('\n')
    game, line = line.split(': ')
    game_num = int(game[5:])
    # print(f'\n\n{game_num=}')
    
    cubes = re.split('; |, ', line)
    cubes = [(color, int(count)) for count, color in [cube.split(' ') for cube in cubes]]  
    # for cube in cubes:
    #     print(f'{cube[0]=}, {cube[1]=}')
    min_red =   max([cube[1] for cube in cubes if cube[0] == 'red'])
    min_green = max([cube[1] for cube in cubes if cube[0] == 'green'])
    min_blue =  max([cube[1] for cube in cubes if cube[0] == 'blue'])
    
    min_colors_reqd.append((min_red, min_green, min_blue))
    
# print(f'{min_colors_reqd=}')
sum_of_triplets = sum([x*y*z for x,y,z in min_colors_reqd])
print(f'{sum_of_triplets=}')
