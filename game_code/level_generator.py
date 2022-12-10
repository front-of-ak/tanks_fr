import os
import random

OBJECTS = ['.', '/', '-', '@', '&']  # . - grass, / - wall, - - enemy, @ - player, & - smth
MAP_HEIGHT, MAP_WIDTH = 20, 27


def count_elems(inp_list, element):
    return sum([i.count(element) for i in inp_list])


# def wall_around(inp_list):
#     for i in range(len(inp_list)):
#         for j in range(len(inp_list[i])):
#             try:
#                 if inp_list[i - 1][j - 1] == '/':
#                     pass
#             except IndexError:


def generate(level_name):
    level_map = [['.'] * MAP_WIDTH for i in range(MAP_HEIGHT)]
    while count_elems(level_map, OBJECTS[1]) < (MAP_HEIGHT * MAP_WIDTH) * 0.2:
        temp_x, temp_y = random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)
        level_map[temp_y][temp_x] = OBJECTS[1]
        # walls delete
    while count_elems(level_map, OBJECTS[2]) < count_elems(level_map, OBJECTS[1]) * 0.07:
        temp_x, temp_y = random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)
        if level_map[temp_y][temp_x] == '.':
            level_map[temp_y][temp_x] = OBJECTS[2]
    while True:
        temp_x, temp_y = random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)
        if level_map[temp_y][temp_x] == '.':
            level_map[temp_y][temp_x] = '@'
            break
    # while count_elems(level_map, OBJECTS[4]) < count_elems(level_map, OBJECTS[0]) * 0.3:
    #     temp_x, temp_y = random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)
    #     if level_map[temp_y][temp_x] == '.':
    #         level_map[temp_y][temp_x] = '&'
    with open(os.path.join('data', 'level_maps', level_name), mode='wt', encoding='utf-8') as f:
        for i in level_map:
            f.write(''.join(i) + '\n')
    return level_name
