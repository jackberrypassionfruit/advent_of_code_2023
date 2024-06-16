import json, sys

with open('../src/input.txt', 'rt') as f:
    lines = iter(f.read().split('\n\n'))

input_seeds_str, *maps = lines

# print(f'{input_seeds=}')

input_seeds_list = [int(val) for val in input_seeds_str.split(': ')[1].split(' ')]

# range1 = list(range(input_seeds_list[0], input_seeds_list[0]+input_seeds_list[1]))
# range2 = list(range(input_seeds_list[2], input_seeds_list[2]+input_seeds_list[3]))

# input_seeds_list = range1 + range2

# create a new approach that doesn't map every inidividual input, 
# but instead ranges with the same delta

# even smarter approach
# pre-calculae what seed mappings would get the smallest output location val
# have to be somewhat greedy to be able to test the smallest sample size possible
# of that list, intersect it with the input seeds. Also greedily

def mapping_fn(val, mappings_list_list):
    for dest_head, src_head, range_val in mappings_list_list:
        dest_src_delta = dest_head - src_head
        if src_head <= val < src_head + range_val:
            return val + dest_src_delta
    return val

def mapping_fn_reversed(val, mappings_list_list):
    for dest_head, src_head, range_val in mappings_list_list:
        dest_src_delta = dest_head - src_head
        if dest_head <= val < dest_head + range_val:
            return val - dest_src_delta
    return val

def is_seed_in_list(val, input_seeds_list):
    for range_start, range_len in zip(input_seeds_list[::2], input_seeds_list[1::2]):
        return range_start <= val < range_start+range_len
        

def smarter(input_seeds_list, maps):
    mappings = dict()
    '''
    usage: 
    mappings[dest]["src"] =                 src
    mappings[dest]["mappings_list_list"] =   mappings_list_list
    '''
        
    for map_str in maps:
            
        map_lines = map_str.split('\n')
        map_src_dest_str, *mappings_str_list = map_lines
        
        map_src, map_dest = map_src_dest_str.rstrip(' map:').split('-to-')
        mappings[map_dest] = dict()
        mappings[map_dest]["src"] = map_src
        
        mappings_list_list = [ [int(val) for val in mapping.split(' ')] for mapping in mappings_str_list]
        mappings_list_list.sort( key=lambda line: line[1], reverse=True ) # for readability
        
        mappings[map_dest]["mappings_list_list"] = mappings_list_list
        
        # print(f'{map_src=}, {map_dest=}')
        # for mapping in mappings_list_list:
        #     print(mapping)
        # print(f'TEST - {mapping_fn(79, mappings_list_list)=}')
        # print()
        
    
    small_location_order = []
    for map_dest, map_src, map_range in mappings['location']['mappings_list_list']:
        map_tuples = [(dest, src) for dest, src in zip(range(map_dest, map_dest+map_range), range(map_src, map_src+map_range))]
        small_location_order += map_tuples
    small_location_order.sort(key=lambda t: t[0])
    small_location_order = [(dest, src) for dest, src in zip(range(small_location_order[0][0]), range(small_location_order[0][0]))] + small_location_order
    print(small_location_order)
    
    # for location_min_src in [n[1] for n in small_location_order]:
    #     src = 'humidity'
    #     val = location_min_src
    #     print(f'{location_min_src=}')
    #     while src != 'seed': # TESTING - should be seed
    #         val = mapping_fn_reversed(val, mappings[src]['mappings_list_list'])
    #         src = mappings[src]["src"]
            
    #     # if val in input_seeds_list:
    #     if is_seed_in_list(val, input_seeds_list):
    #         return location_min_src
    
min_location = smarter(input_seeds_list, maps)
print(f'{min_location=}')
