#
import os.path
import shutil

from actions import action_to_String, choose_Action
from file_operations import save_new_Action_to_File
from main_chain import chain, head, tail
from show_CHAIN import draw


if __name__ == '__main__':
    
    if os.path.isdir('blocks'):
        shutil.rmtree('blocks')
    
    os.mkdir('blocks')
    
    chain.append(list( ))
    
    
    def root_BLock( ):
        return [{ 'Initial block': 'zAbAvA Block-Chain system' }]
    
    
    chain[0].append(root_BLock( ))
    
    head[0] = 0  # last head's level
    head[1] = 0  # last head's block
    
    # tail[0] = 0  # previous block's level
    # tail[1] = 0  # previous block's number
    # tail[2] = 0  # previous level's free number for block
    
    second_part = action_to_String(act_info_second_part = ['zAbAvA Block-Chain system'])
    save_new_Action_to_File(
            lineIdx = head[0],
            blockIdx = head[1],
            action_info = ['Initial block', second_part])
    
    while True:
        draw( )
        act = input('Action - "1" -- User registration,\n'
                    '       - "2" -- Transaction,\n'
                    '       - "3" -- Deleting a user\n'
                    '       - "4" -- Exit\n'
                    '       ------------------------->: ')
        res = choose_Action(act = act)
        if res == 0:
            break
        elif res == 1:
            continue
    print('====================')
    draw( )
