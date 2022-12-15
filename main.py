#
import os.path
import shutil

import actions
import file_operations
from main_chain import chain
from show_CHAIN import draw


def root_BLock( ):
    return [{ 'Initial block': 'zAbAvA Block-Chain system' }]


def create_Block(prev_block_hash, lineNumber, blockNumber):
    block = list( )
    block.append({ "previous block's hash": prev_block_hash })
    second_part = actions.action_to_String([prev_block_hash])
    file_operations.save_new_Action_to_File(lineNumber, blockNumber, ["previous block's hash", second_part])
    return block


if __name__ == '__main__':
    
    if os.path.isdir('blocks'):
        shutil.rmtree('blocks')
    os.mkdir('blocks')
    
    chain.append(list( ))
    chain[0].append(root_BLock( ))
    
    second_part = actions.action_to_String(act_info_second_part = ['zAbAvA Block-Chain system'])
    file_operations.save_new_Action_to_File(
            lineNumber = 1,
            blockNumber = 1,
            action_info = ['Initial block', second_part])
    
    while True:
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
    
    draw(chain = chain)