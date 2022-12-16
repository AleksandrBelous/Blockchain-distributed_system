#
import os.path
import shutil

import actions
import file_operations
from main_chain import chain, head, tail
from show_CHAIN import draw


def root_BLock( ):
    return [{ 'Initial block': 'zAbAvA Block-Chain system' }]


def create_Block(prev_block_hash, lineNumber, blockNumber):
    block = list( )
    block.append({ "previous block's hash": prev_block_hash })
    line_second_part = actions.action_to_String([prev_block_hash])
    file_operations.save_new_Action_to_File(lineNumber, blockNumber, ["previous block's hash", line_second_part])
    return block


if __name__ == '__main__':
    
    if os.path.isdir('blocks'):
        shutil.rmtree('blocks')
    os.mkdir('blocks')
    
    chain.append(list( ))
    chain[0].append(root_BLock( ))
    
    head[0] = 1  # last head's level
    head[1] = 1  # last head's block
    
    tail[0] = 0  # previous block's level
    tail[1] = 0  # previous block's number
    tail[2] = 0  # previous level's free number for block
    
    second_part = actions.action_to_String(act_info_second_part = ['zAbAvA Block-Chain system'])
    file_operations.save_new_Action_to_File(
            lineNumber = head[0],
            blockNumber = head[1],
            action_info = ['Initial block', second_part])
    
    while True:
        draw()
        act = input('Action - "1" -- User registration,\n'
                    '       - "2" -- Transaction,\n'
                    '       - "3" -- Deleting a user\n'
                    '       - "4" -- Exit\n'
                    '       ------------------------->: ')
        res = actions.choose_Action(act = act)
        if res == 0:
            break
        elif res == 1:
            continue
    print('====================')
    draw( )
