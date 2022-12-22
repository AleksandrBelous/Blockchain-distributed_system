#
import random
from actions import action_to_String_with_Time_Mark
from memory_pool import pool

names = list( )


def show_Names( ):
    for name in names:
        print(name, end = ' ')
    print(end = '\n')


def reward_the_Miner( ):
    name = random.choice(names)
    act_info = ['addition', name + ' +250']
    action_key = act_info[0]
    action_value = action_to_String_with_Time_Mark(act_info_second_part = act_info[1:])
    new_line = { action_key: action_value }
    pool.append(new_line)
