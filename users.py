#
import random
import time

names = ['Nemo']


def show_Names():
    for name in names:
        print(name, end=' ')
    print(end='\n')


def reward_the_Miner():
    print('( in reward_the_Miner fn...')
    name = random.choice(names)
    act_info = ['awarding', name + ' +250']
    action_key = act_info[0]
    from actions import action_to_String_with_Time_Mark
    action_value = action_to_String_with_Time_Mark(act_info_second_part=act_info[1:])
    new_line = {action_key: action_value}
    from memory_pool import pool_queue
    pool_queue.append(new_line)
    print('pool was appended')
    print('...out of in reward_the_Miner fn )')
    time.sleep(1.0)
    return True
