import json

with open('../src/test_input.txt', 'rt') as f:
    lines = iter(f.read().split('\n\n'))

input_seeds_str, *maps = lines

# print(f'{input_seeds=}')

input_seeds_list = [int(val) for val in input_seeds_str.split(': ')[1].split(' ')]

def naive(input_seeds_list, maps):
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

    return min(locations)
    
# print(naive(input_seeds_list, maps))



# create a new approach that doesn't map every inidividual input, 
# but instead ranges with the same delta

def mapping_fn(val, mappings_list_list):
    for mapping_list in mappings_list_list:
        dest_head, src_head, range_val = mapping_list
        dest_src_delta = dest_head - src_head
        if src_head <= val < src_head + range_val:
            return val + dest_src_delta
    return val


def smarter(input_seeds_list, maps):
    mappings = dict()
    '''
    usage: 
    mappings[src]["dest"] =                 dest
    mappings[src]["mappings_list_list"] =   mappings_list_list
    '''
        
    for map_str in maps:
            
        map_lines = map_str.split('\n')
        map_src_dest_str, *mappings_str_list = map_lines
        
        map_src, map_dest = map_src_dest_str.rstrip(' map:').split('-to-')
        mappings[map_src] = dict()
        mappings[map_src]["dest"] = map_dest
        
        mappings_list_list = [ [int(val) for val in mapping.split(' ')] for mapping in mappings_str_list]
        mappings_list_list.sort( key=lambda line: line[1], reverse=True ) # for readability
        
        mappings[map_src]["mappings_list_list"] = mappings_list_list
        
        # print(f'{map_src=}, {map_dest=}')
        # for mapping in mappings_list_list:
        #     print(mapping)
        # print(f'TEST - {mapping_fn(79, mappings_list_list)=}')
        # print()
        
    # print('\n\n\n')

    locations = []
    for seed in input_seeds_list:
        dest = 'seed'
        val = seed
        while dest != 'location': # TESTING - should be location
            val = mapping_fn(val, mappings[dest]['mappings_list_list'])
            dest = mappings[dest]["dest"]
        locations.append(val)

    return locations
locations = smarter(input_seeds_list, maps)
print(f'{locations=}')
print(f'{min(locations)=}')