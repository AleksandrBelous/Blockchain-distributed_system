#

import string
import random
import hashlib


def set_New_Block(prev_block_hash, lineIdx, blockIdx):
    block = list( )
    block.append({ "previous block's hash": prev_block_hash })
    from actions import action_to_String_with_Time_Mark
    line_second_part = action_to_String_with_Time_Mark([prev_block_hash])
    from file_operations import save_new_Action_to_File
    save_new_Action_to_File(lineIdx, blockIdx, ["previous block's hash", line_second_part])
    return block


def set_Nonce_to_Block(levelIdx, blockIdx):
    nonce = None
    
    def random_String( ):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(6))
    
    while True:
        nonce = random_String( )
        # make copy of block-file
        from block_getters import get_Block_Info
        copy_block_info = get_Block_Info(levelIdx, blockIdx)
        copy_block_info += nonce
        pr_hash = hashlib.md5(copy_block_info.encode( )).hexdigest( )
        from main_chain import nonce_requirements
        if pr_hash.count('0') == nonce_requirements:
            break
    return nonce


def set_All_New_Actions_to_Block(levIdx, blockIdx):
    print(f'i={levIdx}, j={blockIdx}')
    from main_chain import chain
    cur_block = chain[levIdx][blockIdx]
    # save all new actions to block and to it's file
    from memory_pool import pool
    for dict_line in pool:
        cur_block.append(dict_line)
        action_key = action_value = None
        for k, v in dict_line.items( ):
            action_key, action_value = k, v
        # save to file
        from file_operations import save_new_Action_to_File
        save_new_Action_to_File(
                lineIdx = levIdx,
                blockIdx = blockIdx,
                action_info = [action_key, action_value])
    pool.clear( )


# def set_One_New_Action(levIdx, blockIdx):
#     cur_block = chain[levIdx][blockIdx]
#     # save one action from pool
#     dict_line = pool[0]
#     cur_block.append(dict_line)
#     action_key = action_value = None
#     for k, v in dict_line.items( ):
#         action_key, action_value = k, v
#     # save to file
#     save_new_Action_to_File(
#             lineIdx = levIdx,
#             blockIdx = blockIdx,
#             action_info = [action_key, action_value])
#     pool.pop(0)
