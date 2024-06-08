import json

with open('../src/input.txt', 'rt') as f:
    lines = iter(f.read().split('\n\n'))

input_seeds_str, *maps = lines

# print(f'{input_seeds=}')

input_seeds_list = input_seeds_str.split(': ')[1].split(' ')
input_seeds_list = [int(val) for val in input_seeds_list]

mappings = dict()
'''
usage: 
mappings[src]["dest"] =     dest
mappings[src]["map"][val_str] = map_value
'''

for map_str in maps:
    map_lines = map_str.split('\n')
    map_src_dest_str, *mappings_str_list = map_lines
    map_src, map_dest = map_src_dest_str.rstrip(' map:').split('-to-')
    # print(f'{map_src=}, {map_dest=}')
    mappings[map_src] = dict()
    mappings[map_src]["dest"] = map_dest
    
    map_vals_this_src = dict()
    for mappings_str in mappings_str_list:
        ranges = [ int(val) for val in mappings_str.split(' ') ]
        src_range =  range(ranges[1], ranges[1]+ranges[2])
        dest_range = range(ranges[0], ranges[0]+ranges[2])
        
        map_vals_this_src.update(zip(src_range, dest_range))
    
    mappings[map_src]["map"] = map_vals_this_src
    
# print("mappings:\n", json.dumps(mappings, indent=4))
locations = []

for seed in input_seeds_list:
    dest = 'seed'
    val = seed
    while dest != 'location':
        if val in mappings[dest]["map"].keys():
            val = mappings[dest]["map"][val]
        dest = mappings[dest]["dest"]
    # print(f'{val=}')
    locations.append(val)

print(f'{min(locations)=}')
    